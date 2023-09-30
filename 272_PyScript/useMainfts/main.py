import datetime as dt
import js # provided by pyscript
print("hello world from main.py")

def show_time():
    Element("today").write(str(dt.date.today()))
    print(dt.date.today())

show_time()

a_python = 10 # use this in JS
print(js.name)
print(js.addTwoNos(1,3))