from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Button, TextArea, MarkdownViewer, Static
from textual.containers import Vertical, VerticalScroll


def flashcard(front: str, back: str) -> VerticalScroll:
  
    container = VerticalScroll(
        Static("Front", classes="flashcard-header"),
        MarkdownViewer(front, classes="flashcard-content", show_table_of_contents=False),
        Static("Back", classes="flashcard-header"), 
        MarkdownViewer(back, classes="flashcard-content", show_table_of_contents=False),
        classes="flashcard-container",
    )
    return container


def studyset(name: str):
    return Static(name, classes="studyset")


EXAMPLE_FRONT = "When did the Berlin Wall fall, and what was its significance?"
EXAMPLE_BACK = """\
# November 9, 1989
The Berlin Wall fell on November 9, 1989. This event marked the end of the division between East and West Germany, 
symbolizing the collapse of the communist regime in Eastern Europe and the eventual reunification of Germany. 
It was a key moment in the end of the Cold War.
"""
studysets = ["studyset1", "studyset2", "studyset3"]

class FlashcardManager(Widget):
    def compose(self) -> ComposeResult:
        yield flashcard(EXAMPLE_FRONT, EXAMPLE_BACK)
        yield Vertical(
        TextArea.code_editor(language="markdown"),
        Button("Add Flashcard", name="add_flashcard"),
        Button("Add Studyset", name="add_studyset"),
        id="flashcard-input-area"
        )
        


class StudysetManager(Widget):
    def compose(self) -> ComposeResult:
        yield TextArea.code_editor(language="markdown")
        yield Button("Add Flashcard", name="add_flashcard")
        yield Button("Add Studyset", name="add_studyset")
