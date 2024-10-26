import streamlit as st
from services.optuna_service import OptunaService


class MainPage:
    def __init__(self):
        self.optuna_service = OptunaService()

    def display(self):
        self._display_run_optuna_button()

    def _display_run_optuna_button(self):
        if st.button("Run Optuna Optimization"):
            if st.session_state.get("selected_study_id"):
                self.optuna_service.run_optimization()
            else:
                st.warning("Please select a study before running the optimization.")
