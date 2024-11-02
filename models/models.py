from dataclasses import dataclass

from optuna.study._frozen import FrozenStudy
from optuna.trial import FrozenTrial


@dataclass
class Run:
    study: FrozenStudy
    trials: list[FrozenTrial]


@dataclass
class Runs:
    runs: list[Run]

    def __iter__(self):
        return iter(self.runs)

    def append(self, new_run: Run) -> 'Runs':
        self.runs.append(new_run)
        return self
