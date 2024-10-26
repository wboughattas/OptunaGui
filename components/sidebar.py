import streamlit as st
from services.optuna_service import OptunaService


class Sidebar:
    def __init__(self):
        self.optuna_service = OptunaService()

    def display(self):
        st.sidebar.header("Experiment Management")
        self._study_input()
        self.optuna_service.load_studies()

    def _study_input(self):
        st.sidebar.text_input(
            "Enter New Study Name",
            key="new_study_name",
            placeholder="New Study",
            on_change=self.optuna_service.create_new_study
        )
