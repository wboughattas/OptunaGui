import streamlit as st


class StudyComponents:
    def __init__(self):
        pass

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
                st.session_state[f"show_confirm_{study_id}"] = True

        if st.session_state.get(f"show_confirm_{study_id}", False):
            self._confirm_deletion(study_id, study_name)

    def _toggle_study(self, study_id):
        if st.session_state.get("expanded_study_id") == study_id:
            st.session_state["expanded_study_id"] = None
        else:
            st.session_state["expanded_study_id"] = study_id
            st.session_state["selected_study_id"] = study_id

    def _confirm_deletion(self, study_id, study_name):
        confirm_input = st.sidebar.text_input(
            f"Type DELETE to confirm deletion of '{study_name}'",
            key=f"confirm_{study_id}"
        )
        if confirm_input == "DELETE":
            self.optuna_service.delete_study(study_id, study_name)
