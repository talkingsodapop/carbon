import os.path
import toml

from typing import *

config = {}

def load_config(path) -> None:
    loaded_toml = toml.load(path)
    config.update(loaded_toml)

def try_load_config(path) -> bool:
    if os.path.isfile(path):
        try:
            load_config(path)
            return True
        except Exception as e:
            return e
    return False

def _traverse_to(key: List[str], modify: bool = True) -> dict:
    level = config
    for k in key[:-1]:
        next_level = level.get(k)
        if next_level == None:
            if modify:
                level[k] = {}
                next_level = level[k]
            else:
                return {}
        level = next_level
    return level

def set_config(key: str, value: Any = None) -> None:
    key = key.split(".")
    _traverse_to(key)[key[-1]] = value

def get_config(key: str, default: Any = None) -> Any:
    key = key.split(".")
    if val := _traverse_to(key, modify=False).get(key[-1]):
        return val
    else:
        return default

def get_path(key: str, default: str) -> str:
    val = get_config(key, default)
    if not os.path.isabs(val):
        val = os.path.join(os.getcwd(), val)
    val = os.path.abspath(val)
    return val