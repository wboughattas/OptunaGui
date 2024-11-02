from components.main_page import MainPage
from components.sidebar import Sidebar
from services.hp_framework_service import HPFrameworkService
from utils.session_manager import SessionManager


class App:
    def __init__(self):
        """Initializes the session manager, main_page, sidebar, and components"""
        self.session_manager = SessionManager()
        self.hp_framework_service = HPFrameworkService()
        self.main_page = MainPage(self.session_manager, self.hp_framework_service)
        self.sidebar = Sidebar(self.session_manager, self.hp_framework_service)

    def run(self):
        """Displays the main_page, sidebar, and components"""
        self.main_page.display()
        self.sidebar.display()
