from colorama import just_fix_windows_console
from termcolor import colored

# use Colorama to make Termcolor work on Windows too
just_fix_windows_console()

# then use Termcolor for all colored text output
print(colored('Hello, World!', 'green', 'on_red'))