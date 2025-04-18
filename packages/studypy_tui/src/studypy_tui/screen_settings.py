from textual.app import ComposeResult
from textual.screen import Screen

from .widgets.base_widgets import Sidebar


class SettingsScreen(Screen):
    CSS_PATH = "gui.tcss"
    def compose(self) -> ComposeResult:
        yield Sidebar()