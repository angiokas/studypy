from textual.screen import Screen
from .widgets.base_widgets import Sidebar
from .widgets.flashcards_widgets import FlashcardManager
from textual.app import ComposeResult
from textual.widgets import Header, Footer


        
class FlashcardsScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Sidebar()
        yield FlashcardManager()
        yield Footer()

