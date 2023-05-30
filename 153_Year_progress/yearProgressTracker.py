import time
import datetime
from tqdm import tqdm

# Define the start and end dates of the year
start_date = datetime.date(datetime.datetime.now().year, 1, 1)
end_date = datetime.date(datetime.datetime.now().year, 12, 31)

# Calculate the total number of days in the year
total_days = (end_date - start_date).days + 1

print(start_date)
print(end_date)
print(total_days)

# Iterate over each day of the year
with tqdm(total=total_days, desc="Year Progress", unit="day") as pbar:
    for _ in range(total_days):
        # Calculate the current progress based on the elapsed time
        current_date = datetime.date.today()
        elapsed_days = (current_date - start_date).days
        progress = elapsed_days / total_days * 100

        # Update the progress bar
        pbar.update(elapsed_days - pbar.n)
        pbar.set_postfix({"Progress": f"{progress:.2f}%"})

        time.sleep(0.1)

print(f"Year Progress: {progress}")