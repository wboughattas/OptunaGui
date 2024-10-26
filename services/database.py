import sqlite3


class DatabaseService:
    def __init__(self, db_url):
        self.db_url = db_url

    def connect(self):
        return sqlite3.connect(self.db_url.replace("sqlite:///", ""))

    def execute_query(self, query, params=()):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute(query, params)
            return cur.fetchall()

    def fetch_studies(self):
        query = "SELECT study_id, study_name FROM studies"
        return self.execute_query(query)

    def fetch_trials(self, study_id):
        query = "SELECT trial_id FROM trials WHERE study_id = ?"
        return self.execute_query(query, (study_id,))
