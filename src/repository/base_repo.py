from abc import abstractmethod
from typing import Generic, TypeVar


ModelType = TypeVar("ModelType")
Entity = TypeVar("Entity")

class ABSRepository(Generic[ModelType, Entity]):
    @abstractmethod
    def save(self, obj):
        ...

    @abstractmethod
    def load(self, obj_id):
        ...