import time

import optuna
import streamlit as st


class StudyComponents:
    def display_study_list(self):
        studies = st.session_state.get("studies", [])
        for study_id, study_name in studies:
            self._display_study(study_id, study_name)

    def _display_study(self, study_id, study_name):
        container = st.sidebar.container()
        col1, col2 = container.columns([4, 1])

        with col1:
            if st.button(study_name, key=f"toggle_study_{study_id}"):
                self._toggle_study(study_id)

        with col2:
            if st.button("➖", key=f"delete_study_{study_id}"):
                current_state = st.session_state.get(f"show_confirm_{study_id}", False)
                st.session_state[f"show_confirm_{study_id}"] = not current_state  # Toggle confirmation input visibility

        if st.session_state.get(f"show_confirm_{study_id}", False):
            self._confirm_deletion(study_id, study_name)

        if st.session_state.get("expanded_study_id") == study_id:
            self._display_trials(study_id)

    def _display_trials(self, study_id):
        trials = self._get_trials_for_study(study_id)

        st.toast(f"Found {len(trials)} trials for Study ID: {study_id}")

        if trials:
            for trial_id in trials:
                if st.sidebar.button(f"Experiment {trial_id}", key=f"exp_{trial_id}"):
                    st.session_state["selected_experiment"] = trial_id
                    st.toast(f"Selected Experiment: {trial_id}")

    @staticmethod
    def _get_trials_for_study(study_id):
        import sqlite3
        conn = sqlite3.connect("optuna_experiments.db")
        cur = conn.cursor()
        cur.execute("SELECT trial_id FROM trials WHERE study_id = ?", (study_id,))
        experiments = [row[0] for row in cur.fetchall()]
        return experiments

    @staticmethod
    def _confirm_deletion(study_id, study_name):
        confirm_input = st.sidebar.text_input(
            f"Type DELETE to confirm deletion of '{study_name}'",
            key=f"confirm_{study_id}"
        )
        if confirm_input == "DELETE":
            # noinspection PyArgumentList
            optuna.delete_study(study_name=study_name, storage="sqlite:///optuna_experiments.db")
            st.toast(f"Deleted Study: {study_name}")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def _toggle_study(study_id):
        if st.session_state.get("expanded_study_id") == study_id:
            st.session_state["expanded_study_id"] = None
        else:
            st.session_state["expanded_study_id"] = study_id
            st.session_state["selected_study_id"] = study_id
