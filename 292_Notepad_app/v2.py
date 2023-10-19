# text saved after 5 seconds also after Ctrl + S

from flet import UserControl, TextField, InputBorder, Page, ControlEvent, app
import threading
import time

class TextEditor(UserControl):
    def __init__(self) -> None:
        super().__init__()
        self.textField = TextField(multiline=True, autofocus=True, border=InputBorder.NONE, min_lines=40, content_padding=30, cursor_color='yellow')
        self.autosave_timer = None

    def save_text(self) -> None:
        with open('save.txt', 'w') as f:
            f.write(self.textField.value)

    def autosave(self):
        while True:
            self.save_text()
            time.sleep(5)

    def start_autosave(self):
        self.autosave_timer = threading.Thread(target=self.autosave)
        self.autosave_timer.daemon = True
        self.autosave_timer.start()

    def read_text(self) -> str | None:
        try:
            with open('save.txt', 'r') as f:
                return f.read()
        except FileNotFoundError:
            self.textField.hint_text = "Welcome to the Text Editor"

    def build(self) -> TextField:
        self.textField.value = self.read_text()
        self.start_autosave()
        return self.textField

    def handle_event(self, event: ControlEvent) -> None:
        if event.type == ControlEvent.KEY_DOWN:
            if event.key == 's' and event.modifiers.get('ctrl'):
                self.save_text()

def main(page: Page) -> None:
    page.title = 'Text Editor'
    page.scroll = True
    page.add(TextEditor())

if __name__ == '__main__':
    app(target=main)
