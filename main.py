import streamlit as st

from components.main_page import MainPage
from components.sidebar import Sidebar
from components.study_components import StudyComponents
from services.optuna_service import OptunaService
from utils.session_manager import SessionManager


class App:
    def __init__(self):
        self.session_manager = SessionManager()
        self.main_page = MainPage()
        self.sidebar = Sidebar()
        self.study_components = StudyComponents()
        self.optuna_service = OptunaService()

    def run(self):
        st.title("Hyperparameter Tuning with Optuna (Iris Dataset)")
        self.session_manager.initialize_session_state()

        self.main_page.display()
        self.sidebar.display()
        self.study_components.display_study_list()

        if st.session_state.get("run_optuna"):
            self.optuna_service.run_optimization()
