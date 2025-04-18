from textual.app import ComposeResult
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Label

from .widgets.base_widgets import Sidebar


class HomeScreen(Screen):
    CSS_PATH = "gui.tcss"
    def compose(self) -> ComposeResult:  # Horizontal layout with Sidebar on the left and content on the right
            yield Sidebar()  # Sidebar on the left
            yield Container(Label("blablbala"), classes="box")