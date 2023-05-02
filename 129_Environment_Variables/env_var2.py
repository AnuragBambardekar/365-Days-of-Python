# pip install python-dotenv
from dotenv import load_dotenv, dotenv_values
import os

config = dotenv_values("129_Environment_Variables/.env")
print(config["MY_SECRET_KEY"])
