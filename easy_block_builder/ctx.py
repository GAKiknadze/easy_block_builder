from logging import getLogger, Logger
from copy import copy, deepcopy


VARS_TYPE = dict[str, object]


class Context:
    _path: str
    _vars: VARS_TYPE

    _logger: Logger

    __slots__ = ("_path", "_vars", "_logger")

    def __init__(self, path: str, vars: dict | None = None) -> None:
        self._logger = getLogger(f"{__name__}.{self.__class__.__name__}")

        self._path = path
        self._vars = {self._normalize_key(key): value for key, value in (vars or {}).items()}

        self._logger.debug(
            f"Initialized with path: {path} and arguments: {vars}"
        )

    @property
    def path(self) -> str:
        return copy(self._path)
    
    @property
    def vars(self) -> VARS_TYPE:
        return deepcopy(self._vars)

    @staticmethod
    def _normalize_key(key: str) -> str:
        return key.upper()

    def __setitem__(self, key: str, value) -> None:
        key = self._normalize_key(key)
        self._vars[key] = deepcopy(value)
        self._logger.debug(
            f"Set argument '{key}' to '{value}' with type '{type(value).__name__}'"
        )

    def __getitem__(self, key: str):
        key = self._normalize_key(key)
        value = self._vars.get(key, None)
        self._logger.debug(
            f"Getting argument '{key}' with value '{value}' and type '{type(value).__name__}'"
        )
        return value
