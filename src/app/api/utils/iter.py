from collections.abc import Iterable
import itertools
from typing import Generator, Union, Tuple


def chunked_iterable(iterable: Iterable, size: int) -> Union[Generator, Tuple]:
    """
    Convert the iterable into one that returns items grouped
    together in chunks of size {size}.
    """
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, size))
        if not chunk:
            break
        yield chunk
