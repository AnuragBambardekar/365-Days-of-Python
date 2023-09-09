from alive_progress import alive_it
import time

# Create a list of items to process
items = range(10)

# Wrap the items with alive_it
for item in alive_it(items):
    # Simulate processing each item
    time.sleep(0.5)
    print(f"Processing item {item}")

print("Processing completed.")
