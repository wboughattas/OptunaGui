import time

import streamlit as st

from models.models import Run
from services.hp_framework_service import HPFrameworkService
from utils.session_manager import SessionManager


class RunActions:
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

    @staticmethod
    def display_run(run):
        if st.button(run.study.study_name, key=f"toggle_study_{run.study.study_name}"):
            st.session_state["selected_run"] = run
            if st.session_state.get("expanded_run") == run:
                st.session_state["expanded_run"] = None
            else:
                st.session_state["expanded_run"] = run

    @staticmethod
    def display_trials(run):
        if st.session_state.get("expanded_run") == run:
            if trials := run.trials:
                for trial in trials:
                    if st.sidebar.button(f"Trial {trial._trial_id}", key=f"trial_{trial._trial_id}"):
                        st.session_state["selected_trial"] = trial._trial_id
                        st.toast(f"Selected trial: {trial._trial_id}")
            else:
                st.sidebar.write("No experiments found.")

    def display_refresh_button(self):
        if st.button("⟳", key="refresh_button"):
            self.session_manager.update_session_state("requires_load_runs", True)
            self._refresh_runs()

    def _refresh_runs(self):
        try:
            if self.session_manager.get_session_state("requires_load_runs"):
                runs = self.hp_framework_service.get_runs()
                self.session_manager.add_runs(runs)
                st.toast("Runs are loaded and saved in session memory.")
                self.session_manager.update_session_state("requires_load_runs", False)
        except Exception as e:
            st.sidebar.error(f"Error loading runs: {e}")

    def display_new_run_textbox(self):
        st.text_input(
            "Enter New Run Name",
            key="new_run_name",
            placeholder="New Run",
            label_visibility="collapsed",
            on_change=self._create_new_run
        )

    def _create_new_run(self):
        run_name = self.session_manager.get_session_state("new_run_name")
        if run_name:
            try:
                new_study = self.hp_framework_service.create_new_study(run_name)
                new_run = Run(study=new_study, trials=[])
                self.session_manager.add_run(new_run)
                st.toast(f"Created new run: {new_study.study_name}")
                self.session_manager.update_session_state("selected_run", new_run)
            except Exception as e:
                st.sidebar.error(f"Error creating new run: {e}")
            finally:
                self.session_manager.update_session_state("new_run_name", "")

    def display_delete_button(self, run):
        if st.button("➖", key=f"delete_run_{run.study._study_id}"):
            self.session_manager.update_session_state("run_to_delete", run)

    def confirm_run_deletion(self):
        run = st.session_state.get("run_to_delete")

        if run:
            confirm_input = st.sidebar.text_input(
                f"Type DELETE to confirm deletion of '{run.study.study_name}'",
                key="delete_confirmation_input"
            )

            if confirm_input and confirm_input != "DELETE":
                st.toast(f"Wrong input. Type DELETE to confirm deletion")

            if confirm_input == "DELETE":
                self._delete_run(run)
                self.session_manager.update_session_state("run_to_delete", None)

    def _delete_run(self, run):
        try:
            self.hp_framework_service.delete_study(run.study.study_name)
            self.session_manager.delete_run(study_id=run.study._study_id)

            st.toast(f"Deleted Run: {run.study.study_name}")
            self.session_manager.update_session_state("run_to_delete", None)
            if self.session_manager.get_session_state("selected_run") == run:
                self.session_manager.update_session_state("selected_run", None)

            time.sleep(1)
            st.rerun()
        except Exception as e:
            st.sidebar.error(f"Error deleting study '{run.study.study_name}': {e}")
