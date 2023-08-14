# Using Makefiles in Python

- Create a ```package``` with a ```main.py``` and ```__init__.py``` file.
- Create a ```setup.py``` file outside the ```package```
- From the terminal, run:
```cmd
python setup.py build bdist_wheel
```
- Create a ```requirements.txt``` file and then you can install the requirements using:
```cmd
pip install -r requirments.txt
```
- You can also do a cleanup by running the following commands in CMD:
```cmd
rd /s /q build
rd /s /q dist
rd /s /q myprojectname.egg-info
```

- So, let's create a Makefile to automate this process
