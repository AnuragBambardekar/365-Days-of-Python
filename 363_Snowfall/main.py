import sys
import os
import random
import time
import shutil

def is_arg(t, as_, al):
    return t == as_ or t == al

# Clear the terminal
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Sleep function
def sleep(t):
    time.sleep(t / 1000)

if __name__ == "__main__":
    # Get the actual terminal size
    term_size = shutil.get_terminal_size()
    ww, wh, ssc, sd = term_size.columns, term_size.lines, 3, 300  # Initialize with terminal size

    random.seed(time.time())
    w = [' ' if i % ww else '\n' for i in range(wh * ww)]  # Create world & populate with emptiness

    while True:
        cls()  # Clear frame
        print(''.join(w))  # Render world
        # Iterate (backwards to make snow fall properly)
        for i in range(wh * ww - 1, -1, -1):
            # Make snowflakes fall
            if w[i] == '*' or w[i] == '+' or w[i] == '.':
                if i + ww < wh * ww and w[i + ww] == ' ':
                    if i + ww * 2 < wh * ww:
                        w[i + ww] = w[i]
                        w[i] = ' '
                    else:
                        w[i] = ' '  # Despawn the snowflake if it reaches the bottom
            # Spawn snowflakes (focus *) under the right conditions
            if i < ww and 0 <= i + ww < wh * ww and w[i + ww] == ' ' and random.randint(0, 99) <= ssc:
                w[i] = random.choice(['*', '.', '+', '✵'])

        sleep(sd)  # Sleep
