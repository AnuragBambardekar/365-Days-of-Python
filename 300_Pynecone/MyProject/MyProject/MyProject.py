# increasing/decreasing a counter using buttons

import pynecone as pc

# defining a state
class State(pc.State):
    count = 0
    color = "red"
    color_list = ["red","green","blue","orange","purple"]
    color_index = 0
    text = "hello world"

    def increment(self):
        self.count += 1
        
    def decrement(self):
        self.count -= 1

    def backwards(self):
        self.color_index -= 1
        self.color_index %= 5
        self.color = self.color_list[self.color_index]

    def forward(self):
        self.color_index += 1
        self.color_index %= 5
        self.color = self.color_list[self.color_index]

    @pc.var
    def myText(self):
        return self.text.upper()

# building a UI
def index():
    return pc.hstack(
        pc.button("-", color_scheme="red", border_radius="1em",
                  on_click=State.decrement),
        pc.heading(State.count, font_size="2em"),
        pc.button("+", color_scheme="green", border_radius="1em",
                  on_click=State.increment)
    )

def colorPage():
    return pc.vstack(
        pc.button("<", color_scheme="gray", border_radius="1em",
                  on_click=State.backwards),
                  pc.heading("Hello World", color=State.color, font_size="2em"),
        pc.button(">", color_scheme="gray", border_radius="1em",
                  on_click=State.forward)
    )

def other():
    return pc.vstack(
        pc.heading(State.myText),
        pc.input(on_blur=State.set_text)
    )

app = pc.App(state=State)
app.add_page(index, title="counter", route="/")
app.add_page(colorPage, title="colorPage", route="/test")
app.add_page(other, title="other", route="/test2")

app.compile()