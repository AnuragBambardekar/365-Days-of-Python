from alive_progress import alive_bar
import time

# Create a custom progress bar
"""
bars could be one of the following:
('smooth', 'classic', 'classic2', 'brackets', 'blocks', 'bubbles', 'solid', 'checks', 'circles', 'squares', 'halloween', 'filling', 'notes', 'ruler', 'ruler2', 'fish', 'scuba')
"""
with alive_bar(100, title="Processing", bar="bubbles", spinner="dots_waves") as bar:
    for i in range(100):
        time.sleep(0.05)
        bar()  # Advance the progress bar
