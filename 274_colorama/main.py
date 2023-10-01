"""
pip install colorama
"""

from colorama import Fore, Back, Style, init
init(autoreset=True)
# color changes automatically reset after each print, 
# so you don't have to manually reset the colors.

print(Fore.RED + 'This text is red' + Fore.RESET)
print(Fore.GREEN + Back.YELLOW + 'Green text on yellow background' + Style.RESET_ALL)

# Text styles
print(Style.BRIGHT + 'This text is bold and bright')
print(Style.NORMAL + 'This text is normal')
print(Style.DIM + 'This text is dim')

# Background colors
print(Back.BLUE + 'Blue background')
print(Back.WHITE + Fore.BLACK + 'White text on black background')

# Mixing styles
print(Fore.YELLOW + Style.BRIGHT + 'Bold and bright yellow text')

# custom colors
# Define custom RGB colors using ANSI escape codes
custom_fg_color = f'\033[38;2;255;100;0m'  # Custom RGB foreground color
custom_bg_color = f'\033[48;2;0;0;255m'   # Custom RGB background color
reset_color = '\033[0m'                   # Reset to default color

# Create a custom colored string
custom_colored_text = f'{custom_fg_color}{custom_bg_color}Custom RGB Color{reset_color}'

# Print the custom colored string
print(custom_colored_text)