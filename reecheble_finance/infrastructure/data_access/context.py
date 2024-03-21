from abc import ABC, abstractmethod
from contextlib import contextmanager
from typing import TypeVar

__all__ = [
    "ServiceContext"
]


Context = TypeVar("Context")


class ServiceContext(ABC):
    context: Context = None

    def __init__(self, context: Context) -> None:
        self.context: Context = self.__class__.context or context

    @contextmanager
    def get_context(self):
        try:
            yield self.context
        finally:
            self.close()

    @abstractmethod
    def close(self) -> None: ...

    @abstractmethod
    def commit(self) -> None: ...

    @abstractmethod
    def rollback(self) -> None: ...
