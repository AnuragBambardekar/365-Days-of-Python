# Further Improvements
# - Add State Capitals feature

from tkinter import *
from PIL import ImageTk, Image
from random import randint

root = Tk()
root.title('Flashcards')
root.geometry("650x650")

# create randomizing state
def random_state():
    # create a list of state names
    global our_states
    our_states = [
        "alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut", "delaware",
        "florida", "georgia", "hawaii", "idaho", "illinois", "indiana",
        "iowa", "kansas", "kentucky", "louisiana", "maine", "maryland", "massachusetts", "michigan",
        "minnesota", "mississippi", "missouri", "montana", "nebraska", "nevada", "newhampshire", "newjersey",
        "newmexico", "newyork", "northcarolina", "northdakota", "ohio", "oklahoma",
        "oregon", "pennsylvania", "rhodeisland", "southcarolina", "southdakota", "tennessee", "texas", "utah",
        "vermont", "virginia", "washington", "westvirginia", "wisconsin", "wyoming"
    ]

    # generate a random number
    global rando
    rando = randint(0, len(our_states)-1)
    state_name = our_states[rando]
    state_image_path = f"images/{state_name}.png"

    # resize the image
    global state_img
    state_img = resize_image(state_image_path)
    show_state.config(image=state_img, bg="white")

# resize image to fit window
def resize_image(image_path, width=400, height=400):
    # Open the image and resize it
    img = Image.open(image_path)
    img = img.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)

# create answer function
def state_answer():
    answer = answer_input.get()
    answer = answer.replace(" ", "")

    # Determine if our answer is correct or not
    if answer.lower() == our_states[rando]:
        response = "Correct!! " + our_states[rando].title()
    else:
        response = "Incorrect! " + our_states[rando].title()
    
    answer_label.config(text=response)
    # clear the entry box
    answer_input.delete(0,'end')
    random_state()

def states():
    hide_all_frames()
    state_frame.pack(fill="both", expand=1)

    # create our state images
    global show_state
    show_state = Label(state_frame)
    show_state.pack(pady=15)
    random_state()

    # Create button to randomize state images
    global answer_input
    answer_input = Entry(state_frame, font=("helvetica", 18), bd=2)
    answer_input.pack(pady=15)

    # create button to randomize state images
    rando_button = Button(state_frame, text="Pass", command=states)
    rando_button.pack(pady=10)

    # Create a button to answer the question
    answer_button = Button(state_frame, text="Answer", command=state_answer)
    answer_button.pack(pady=5)

    # create a label to tell us if we got the correct answer or not
    global answer_label
    answer_label = Label(state_frame, text="", font=("helvetica", 18), bg="white")
    answer_label.pack(pady=15)

# hide previous frames
def hide_all_frames():
    for widget in state_frame.winfo_children():
        widget.destroy()

    state_frame.pack_forget()

# create frames
state_frame = Frame(root, width=500, height=500, bg="white")

# Call the states function directly to show the States flashcards
states()

root.mainloop()
