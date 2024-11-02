import streamlit as st
from components.sidebar_components.run_actions import RunActions
from services.hp_framework_service import HPFrameworkService
from utils.session_manager import SessionManager


class Sidebar:
    def __init__(self, session_manager: SessionManager, hp_framework_service: HPFrameworkService):
        self.run_actions = RunActions(session_manager, hp_framework_service)

    def display(self):
        st.sidebar.header("Historical Studies")
        self.run_actions._refresh_runs()

        with st.sidebar:
            input_col, refresh_col = st.columns([4, 1])
            with input_col:
                self.run_actions.display_new_run_textbox()
            with refresh_col:
                self.run_actions.display_refresh_button()

            run_col, delete_col = st.columns([4, 1])
            runs = self.run_actions.session_manager.get_session_state("runs")

            for run in runs:
                with run_col:
                    self.run_actions.display_run(run)
                    self.run_actions.display_trials(run)
                with delete_col:
                    self.run_actions.display_delete_button(run)

            self.run_actions.confirm_run_deletion()
