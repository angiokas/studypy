from textual.app import App

from studypy_tui.screen_flashcards import FlashcardsScreen
from studypy_tui.screen_home import HomeScreen
from studypy_tui.screen_practice import PracticeScreen
from studypy_tui.screen_settings import SettingsScreen
from studypy_tui.screen_stats import StatsScreen


class MainApp(App):
    
    MODES = {
            "home": HomeScreen,
            "flashcards": FlashcardsScreen,
            "practice": PracticeScreen,
            "stats": StatsScreen,
            "settings": SettingsScreen
            }
    DEFAULT_MODE = "home"

    def on_mount(self) -> None:
        self.switch_mode("home")

def main():
    MainApp().run()

if __name__ == "__main__":
    main()