from .cycle_repositories import CycleRepositorySelector
from .cycle import Cycle, CycleModel
from ..repository.base_repo import ABSRepository


class CycleRepository(ABSRepository[CycleModel, Cycle]): # type: ignore
    def __init__(self) -> None:
        super().__init__()
        self.repo = CycleRepositorySelector.select_repository()
    
    def save(self, obj):
        self.repo.save(obj)
    
    def load(self, obj_id):
        self.repo.load(obj_id)

    def save_and_load(self, obj):
        self.save(obj)
        self.load("obj_id")
