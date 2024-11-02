import re

import optuna
from unidecode import unidecode

from config import DB_URL
from models.models import Run, Runs


class HPFrameworkService:
    def __init__(self):
        self.db_url = DB_URL

    def get_runs(self) -> Runs:
        storage = optuna.storages.get_storage(storage=self.db_url)
        studies = storage.get_all_studies()
        runs = [Run(study=study, trials=storage.get_all_trials(study._study_id)) for study in studies]
        return Runs(runs=runs)

    # todo: use database service (use st.connection)
    # todo: @st.cache_data (when loading data), @st.cache_resource (for ML, connections)

    def create_new_study(self, study_name):
        new_study_name = unidecode(re.sub(r"\s{2,}", " ", study_name.strip()))
        if new_study_name:
            try:
                # noinspection PyArgumentList
                return optuna.study.create_study(direction="maximize", storage=self.db_url, study_name=new_study_name)
            except optuna.exceptions.DuplicatedStudyError:
                raise Exception(f"A study with the name '{new_study_name}' already exists.")

    def delete_study(self, study_name):
        try:
            # noinspection PyArgumentList
            optuna.delete_study(study_name=study_name, storage=self.db_url)
        except Exception:
            raise Exception(f"Cannot delete study '{study_name}'.")
