# stdlib
import abc


class SyncController(metaclass=abc.ABCMeta):
    """Abstract synchronous controller class"""

    @abc.abstractmethod
    def __call__(self, *args, **kwargs):
        raise NotImplementedError


class AsyncController(abc.ABC):
    """Abstract asynchronous controller class"""

    @abc.abstractmethod
    async def __call__(self, *args, **kwargs):
        raise NotImplementedError
