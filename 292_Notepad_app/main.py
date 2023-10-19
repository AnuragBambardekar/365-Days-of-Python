# pip install flet

from flet import (UserControl, TextField,
                  InputBorder, Page, ControlEvent, app)

# import flet as ft

class TextEditor(UserControl):
    def __init__(self) -> None:
        super().__init__()
        self.textField = TextField(multiline=True,
                                   autofocus=True,
                                   border=InputBorder.NONE,
                                   min_lines=40,
                                   on_change=self.save_text,
                                   content_padding=30,
                                   cursor_color='yellow')
        
    
    def save_text(self, e) -> None:
        with open('save.txt','w') as f:
            f.write(self.textField.value)
    
    def read_text(self) -> str | None:
        try:
            with open('save.txt','r') as f:
                return f.read()
        except FileNotFoundError:
            self.textField.hint_text = "Welcome to the Text Editor"

    def build(self) -> TextField:
        self.textField.value = self.read_text()
        return self.textField
    
def main(page:Page) -> None:
    page.title = 'Text Editor'
    page.scroll = True

    page.add(TextEditor())

if __name__ == '__main__':
    app(target=main)