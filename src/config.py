import os.path
import toml
from typing import *

config = {}

# Load a new TOML config.
def load_config(path) -> None:
    loaded_toml = toml.load(path)
    config.update(loaded_toml)

# Try to load a new TOML config. Returns True on success, returns False or
# an exception on failure.
def try_load_config(path) -> bool:
    if os.path.isfile(path):
        try:
            load_config(path)
            return True
        except Exception as e:
            return e
    return False

# Find a nested dictionary.
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

# Set a config key.
def set_config(key: str, value: Any = None) -> None:
    key = key.split(".")
    _traverse_to(key)[key[-1]] = value

# Get a config key.
def get_config(key: str, default: Any = None) -> Any:
    key = key.split(".")
    if val := _traverse_to(key, modify=False).get(key[-1]):
        return val
    else:
        return default

# Get an absolute path from the config. Converts relative paths to absolute
# paths based on working directory.
def get_path(key: str, default: str) -> str:
    val = get_config(key, default)
    if not os.path.isabs(val):
        val = os.path.join(os.getcwd(), val)
    val = os.path.abspath(val)
    return val