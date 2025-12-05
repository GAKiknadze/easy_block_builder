from logging import getLogger, Logger
from .ctx import Context
import re


_VARS_PATTERN = re.compile(r"{{\s*(.*?)\s*}}")


class BaseBlock:
    _type: str = "base"
    _props: dict[str, object]
    
    _logger: Logger
    
    __slots__ = ("_props", "_logger")
    
    def __init__(self, properties: dict[str, object]) -> None:
        self._logger = getLogger(f"{__name__}.{self.__class__.__name__}")
        self._props = properties
        self._logger.debug(f"Initialized block of type: {self._type} with properties: {self._props}")
    
    def build(self, ctx: Context) -> dict[str, object]:
        """Build the block by replacing variables with their values from context.
        
        Args:
            ctx: Context object containing variables to substitute
            
        Returns:
            Dictionary with built properties where variables are replaced by their values
        """
        def _build_value(val):
            """Recursively build values by replacing variables."""
            if isinstance(val, BaseBlock):
                return val.build(ctx)
            elif isinstance(val, str):
                def replace_var(match):
                    var_name = match.group(1).strip()
                    value = ctx[var_name]
                    if value is None:
                        self._logger.warning(f"Variable '{var_name}' not found in context: {ctx.vars}")
                    return str(value)
                
                return _VARS_PATTERN.sub(replace_var, val)
            elif isinstance(val, dict):
                return {k: _build_value(v) for k, v in val.items()}
            elif isinstance(val, list):
                return [_build_value(item) for item in val]
            elif isinstance(val, tuple):
                return tuple(_build_value(item) for item in val)
            elif isinstance(val, set):
                return {_build_value(item) for item in val}
            else:
                return val
        
        result = {key: _build_value(value) for key, value in self._props.items()}
        self._logger.debug(f"Built block of type {self._type}: {result}")
        return result
    
    @property
    def type(self) -> str:
        return self._type
    
    def get_vars(self) -> set[str]:
        """Collect all variables used in this block and nested blocks."""
        vars_set = set()

        def _collect(val):
            if isinstance(val, BaseBlock):
                vars_set.update(val.get_vars())
            elif isinstance(val, str):
                for match in _VARS_PATTERN.findall(val):
                    if match.strip():
                        vars_set.add(match.strip())
            elif isinstance(val, dict):
                for v in val.values():
                    _collect(v)
            elif isinstance(val, (list, tuple, set)):
                for item in val:
                    _collect(item)

        for value in self._props.values():
            _collect(value)

        self._logger.debug(f"Collected variables: {vars_set}")
        return vars_set
