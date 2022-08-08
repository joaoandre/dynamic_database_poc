from typing import Generic, TypeVar
from .base_repo import ABSRepository


ModelType = TypeVar("ModelType")
Entity = TypeVar("Entity")

class FSRepo(ABSRepository[ModelType, Entity]):
    def save(self, obj):
        print(f"Saving {obj} with FSRepo")
    
    def load(self, obj_id):
        print(f"Retrieving object {obj_id} with FSRepo")