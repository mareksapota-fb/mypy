# Stubs for functools

# NOTE: These are incomplete!

from typing import Callable, Any

# TODO implement as class; more precise typing
# TODO cache_info and __wrapped__ attributes
# TODO None valid as value for maxsize
def lru_cache(maxsize: int = 100) -> Callable[[Any], Any]: pass

# TODO more precise typing?
def wraps(func: Any) -> Any: pass
