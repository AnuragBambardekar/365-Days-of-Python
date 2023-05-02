# pip install python-dotenv
from dotenv import load_dotenv, dotenv_values
import os

config = {
    **dotenv_values("129_Environment_Variables/.env.shared"),
    **dotenv_values("129_Environment_Variables/.env.secret"),
    # **os.environ
}
print(config)

# Now we can share the .env.shared file and not make the secret key public

