import streamlit as st

from components.main_page_components.optimization_actions import OptimizationActions
from services.hp_framework_service import HPFrameworkService
from utils.session_manager import SessionManager


class MainPage:
    def __init__(self, session_manager: SessionManager, hp_framework_service: HPFrameworkService):
        self.optimization_actions = OptimizationActions(session_manager, hp_framework_service)

    def display(self):
        st.title("Hyperparameter Tuning with Optuna")
        self.optimization_actions._display_run_optuna_button()
