from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Placeholder


class Header(Placeholder):  
    pass


class Footer(Placeholder):  
    pass


class TweetScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(id="Header")  
        yield Footer(id="Footer")  

class Footer(Placeholder):
    pass

class ManagerToolApp(App):
    def on_mount(self) -> None:
        self.push_screen(TweetScreen())

if __name__ == "__main__":
    app = ManagerToolApp()
    app.run()