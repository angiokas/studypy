from textual import on
from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widget import Widget
from textual.widgets import Button


class Sidebar(Widget):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Button("Home", id="home"),
            Button("Flashcards", id="flashcards"),
            Button("Practice", id="practice"),
            Button("Stats", id="stats"),
            Button ("Settings", id="settings"),
            classes="sidebar"
        )

    @on(Button.Pressed)
    def handle_nav(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id in {"home", "flashcards", "practice", "stats", "settings"}:
            self.app.switch_mode(button_id)