from .cycle.cycle_repo import CycleRepository
from .config import Config


if __name__ == "__main__":
    repo = CycleRepository()
    repo.save_and_load("foo")