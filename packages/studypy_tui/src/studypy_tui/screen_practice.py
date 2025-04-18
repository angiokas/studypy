from textual.app import ComposeResult
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Footer, Header, Static

from .widgets.base_widgets import Sidebar


class PracticeScreen(Screen):
    def compose(self) -> ComposeResult:
            yield Header()
            yield Sidebar()
            yield Container(  # Content on the right
                Static("One", classes="box"),
                Static("Two", classes="box"),
                Static("Three", classes="box"),
            )        
            yield Footer()