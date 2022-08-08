from src.repository.fs_repo import FSRepo
from src.repository.sql_repo import SQLRepo
from src.config import Config
from .cycle import Cycle, CycleModel


class CycleFSRepo(FSRepo[CycleModel, Cycle]):
    ...


class CycleSQLRepo(SQLRepo[CycleModel, Cycle]):
    ...

class CycleRepositorySelector:

    _REPOSITORY_MAP = {"default": CycleFSRepo, "sql": CycleSQLRepo}

    @classmethod
    def select_repository(cls):
        repo = cls._REPOSITORY_MAP.get(Config.repository_type)

        if not repo:
            return cls._REPOSITORY_MAP.get("default")()

        return repo()