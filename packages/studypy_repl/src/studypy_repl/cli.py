import cmd

from rich.console import Console

from studypy_core.db_operations import create_flashcard, get_all_flashcards

console = Console()

STYLES = {
    "default": "bold cyan",
    "error": "bold red",
    "success": "bold green",
    "warning": "bold yellow",
    "background": "on blue",
}


def print_command(message, style="default"):
    """Helper function to print messages with predefined styles."""
    console.print(message, style=STYLES.get(style, STYLES["default"]))


class SquirrelShell(cmd.Cmd):
    intro = print_command("Hello!")
    prompt = "> "

    def do_hello(self, arg):
        print_command("Hello!!", "success")

    def do_new_flashcard(self, arg):
        f_question = input("Enter the flashcard question: ")
        f_answer = input("Enter the flashcard answer: ")
        create_flashcard(f_question, f_answer)

    def do_list_flashcards(self, arg):
        get_all_flashcards()

    def do_exit(self, arg):
        print_command("Exiting the app.")
        return True
