# pip install python-dotenv
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

print(os.getenv("MY_SECRET_KEY"))
print(os.getenv("COMBINED"))
print(os.getenv("MAIL"))


"""
It is a popular library used for loading environment variables from a file named .env into os.environ for use in a Python application. 
The library is particularly useful in scenarios where you need to keep sensitive information such as API keys, passwords, 
and other credentials outside of your codebase.

With dotenv, you can define environment variables in a .env file in the root directory of your project, and then load them into your Python script using 
the load_dotenv() function. Once the variables are loaded, you can access them using os.getenv().
"""