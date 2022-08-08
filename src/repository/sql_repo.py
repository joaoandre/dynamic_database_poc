from typing import Generic, TypeVar
from .base_repo import ABSRepository


ModelType = TypeVar("ModelType")
Entity = TypeVar("Entity")

class SQLRepo(ABSRepository[ModelType, Entity]):
    def save(self, obj):
        print(f"Saving {obj} with SQLRepo")
    
    def load(self, obj_id):
        print(f"Retrieving object {obj_id} with SQLRepo")