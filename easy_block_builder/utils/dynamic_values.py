from datetime import datetime
from collections import defaultdict
from pydantic import BaseModel, Field
from typing import Self
import re

DYNAMIC_VALUES_PATTERN = re.compile(r"\{\{\s*(.+?)\s*\}\}") # захват внутри {{ ... }}, допускаем спецсимволы, ленивый захват

class DynamicValuesMixin(BaseModel):
    __dynamic_values__: dict[str, int | str | bool | datetime | None] = Field(
        default_factory=lambda: defaultdict(lambda: None))
    
    def get_all_dynamic_variable_names(self) -> set[str]:
        """
        Вернуть множество имён динамических переменных из этого объекта и всех вложенных объектов/контейнеров.
        Рекурсивно обходит поля, списки, кортежи, множества и словари, предотвращая зацикливание.
        Также извлекает имена переменных из строк вида {{название переменной}} — в названии допускаются спецсимволы.
        """

        result: set[str] = set()
        visited_ids: set[int] = set()

        def _process_value(value):
            # BaseObject -> рекурсивно обрабатывать
            if isinstance(value, Self):
                _recurse(value)
                return
            # str -> извлечь шаблонные переменные {{...}}
            if isinstance(value, str):
                for m in DYNAMIC_VALUES_PATTERN.findall(value):
                    result.add(m.strip())
                return
            # dict -> обработать ключи и значения
            if isinstance(value, dict):
                vid = id(value)
                if vid in visited_ids:
                    return
                visited_ids.add(vid)
                for k, v in value.items():
                    _process_value(k)
                    _process_value(v)
                return
            # список/кортеж/множество -> обработать элементы
            if isinstance(value, (list, tuple, set)):
                vid = id(value)
                if vid in visited_ids:
                    return
                visited_ids.add(vid)
                for item in value:
                    _process_value(item)
                return
            # примитивы и прочее пропустить

        def _recurse(obj: Self):
            oid = id(obj)
            if oid in visited_ids:
                return
            visited_ids.add(oid)
            # собрать ключи из __dynamic_values__, если есть
            dyn = getattr(obj, "__dynamic_values__", None)
            if isinstance(dyn, dict):
                for k in dyn.keys():
                    if isinstance(k, str):
                        result.add(k)
            # обойти все поля объекта (кроме __dynamic_values__)
            for name, value in getattr(obj, "__dict__", {}).items():
                if name == "__dynamic_values__":
                    continue
                _process_value(value)

        _recurse(self)
        return result
