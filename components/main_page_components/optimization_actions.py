import optuna
import streamlit as st

from models.model import Model
from models.models import Run
from services.hp_framework_service import HPFrameworkService
from utils.session_manager import SessionManager


class OptimizationActions:
    """
    Implements run related actions:
        1. displaying trials (if exist) for a selected run;
        2. refreshing existing runs;
        3. creating a new run;
        4. deleting an existing run with confirmation;
    """

    def __init__(self, session_manager: SessionManager, hp_framework_service: HPFrameworkService):
        self.session_manager = session_manager
        self.hp_framework_service = hp_framework_service

    def _display_run_optuna_button(self):
        run = self.session_manager.get_session_state("selected_run")
        if run:
            st.write(f"Selected run: {run.study.study_name}")
        else:
            st.warning("Please select a study before running optimization.")
            return

        if st.button(f"Run Optimization"):
            self.run_optimization(run)

    def run_optimization(self, run: Run):
        # noinspection PyArgumentList
        study = optuna.load_study(study_name=run.study.study_name, storage=self.hp_framework_service.db_url)
        model = Model(
            model_type=st.session_state["model_type"],
            split_ratio=st.session_state["split_ratio"],
            random_state=st.session_state["random_state"],
        )

        study.optimize(model.objective, n_trials=10)

        st.write(f"Optimization completed for Study: {run.study.study_name}")
        st.write("Best Trial Parameters:", study.best_trial.params)
        st.write("Best Accuracy Score:", study.best_value)

        st.subheader("Confusion Matrix")
        st.write(model.get_confusion_matrix())

        st.subheader("Classification Report")
        st.write(model.get_classification_report())
