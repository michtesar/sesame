from typing import Any, Dict

from sesame.logging import logger

YAML = Dict[str, Any]


def remove_nested_variables(data: YAML) -> None:
    for key, value in list(data.items()):
        if isinstance(value, dict):
            logger.debug(f"Removing secret '{key}' because it is nested")
            data.pop(key)


def remove_empty_variables(data: YAML) -> None:
    for key, value in list(data.items()):
        if not value:
            logger.debug(f"Removing secret '{key}' because it is empty")
            data.pop(key)


SECRET = Dict[str, str]
