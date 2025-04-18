from textual.app import ComposeResult
from textual.screen import Screen

from .widgets.base_widgets import Sidebar


class StatsScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Sidebar()
 