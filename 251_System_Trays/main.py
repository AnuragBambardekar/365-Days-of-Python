# pip install pystray

import pystray
import PIL.Image

image = PIL.Image.open("251_System_Trays/dog.png")

def on_clicked(icon, item):
    if str(item) == "Say Hello":
        print("Hello World!") 
    elif str(item) == "Exit":
        icon.stop()
    elif str(item) == "SubItem-1":
        print("SubItem-1") 
    else:
        print("Not Implemented yet!")

icon = pystray.Icon("Dog", image, menu=pystray.Menu(
    pystray.MenuItem("Say Hello", on_clicked),
    pystray.MenuItem("Exit", on_clicked),
    pystray.MenuItem("Sub-Menu", pystray.Menu(
        pystray.MenuItem("SubItem-1", on_clicked),
        pystray.MenuItem("SubItem-2", on_clicked),
    )),
))

icon.run()