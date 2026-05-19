#!/usr/bin/env python3
from textual.app import App, ComposeResult, RenderResult
from textual.containers import Container
from textual.widget import Widget


class Hello(Widget):

    def render(self) -> RenderResult:
        return "_________________________________________\n" \
        "|                                       |\n" \
        "|                                       |\n" \
        "|                                       |\n" \
        "|            Hi dear user!              |\n" \
        "|                                       |\n" \
        "|                                       |\n" \
        "|_______________________________________|"

class Notes(Widget):

    def render(self) -> RenderResult:
        return "__________________Notes_________________\n" \
        "| You can add some notes here           |\n" \
        "|                                       |\n" \
        "|                                       |\n" \
        "|                                       |\n" \
        "|                                       |\n" \
        "|_______________________________________|"


class ScheduleManagerApp(App):
    CSS_PATH = "main.tcss"

    BINDINGS = [
        ("q", "quit", "Quit the app"),
    ]


    def compose(self) -> ComposeResult:
        yield Hello()
        yield Notes()


if __name__ == "__main__":
    app = ScheduleManagerApp()
    app.run()