# import datetime
# import time

# def get_day_progress():
#     now = datetime.datetime.now()
#     start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
#     end_of_day = now.replace(hour=23, minute=59, second=59, microsecond=999999)
#     total_seconds_in_day = (end_of_day - start_of_day).total_seconds()
#     elapsed_seconds = (now - start_of_day).total_seconds()
#     progress_percentage = (elapsed_seconds / total_seconds_in_day) * 100
#     return progress_percentage

# while True:
#     progress = get_day_progress()
#     print(f"Day progress: {progress:.2f}%")
#     # Wait for 1 second before updating the progress
#     time.sleep(1)

## pip install alive-progress
## pip install progress

# import time
# import datetime
# from alive_progress import alive_bar

# def get_day_progress():
#     now = datetime.datetime.now()
#     start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
#     end_of_day = now.replace(hour=23, minute=59, second=59, microsecond=999999)
#     total_seconds_in_day = (end_of_day - start_of_day).total_seconds()
#     elapsed_seconds = (now - start_of_day).total_seconds()
#     progress_percentage = (elapsed_seconds / total_seconds_in_day) * 100
#     return progress_percentage

# with alive_bar(100) as bar:
#     while True:
#         progress = get_day_progress()
#         bar(progress)
#         # Wait for 1 second before updating the progress
#         time.sleep(1)

# now = datetime.datetime.now()

# # Define the start and end time of the day
# start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
# end_of_day = now.replace(hour=23, minute=59, second=59, microsecond=999999)

# # Calculate the total time in a day
# total_seconds_in_day = (end_of_day - start_of_day).total_seconds()

# print(total_seconds_in_day)

# old_prog_val = 0

# with alive_bar(100) as bar:
#     while True:

#         # Calculate the current progress based on the elapsed time
#         current_time = datetime.datetime.now()
#         elapsed_seconds = (current_time - start_of_day).total_seconds()
#         progress = elapsed_seconds / total_seconds_in_day * 100

#         bar_prog = progress - old_prog_val
#         print(bar_prog)

#         # Update the progress bar
#         bar(bar_prog)

#         old_prog_val = progress
#         progress = 0
        
#         # Check if the day has ended
#         if current_time >= end_of_day:
#             print("Day Completed!")
#             break

#         time.sleep(0.1)


import datetime
import time
from progress.bar import Bar, FillingSquaresBar, PixelBar

def get_day_progress():
    now = datetime.datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day = now.replace(hour=23, minute=59, second=59, microsecond=999999)
    total_seconds_in_day = (end_of_day - start_of_day).total_seconds()
    elapsed_seconds = (now - start_of_day).total_seconds()
    progress_percentage = (elapsed_seconds / total_seconds_in_day) * 100
    return progress_percentage

bar = FillingSquaresBar('Day progress:', max=100)

while True:
    remaining_seconds = (datetime.datetime.now().replace(hour=23, minute=59, second=59, microsecond=999999) - datetime.datetime.now()).total_seconds()
    remaining_hours = int(remaining_seconds // 3600)  # Calculate remaining hours
    remaining_minutes = int((remaining_seconds % 3600) // 60)  # Calculate remaining minutes

    progress = get_day_progress()
    
    bar.goto(progress)
    print(f" Progress: {progress:.3f}%, Current Date and Time: {datetime.datetime.now().strftime('%H:%M:%S')}, Remaining Time till Midnight: {remaining_hours} hours and {remaining_minutes} minutes.")

    # Wait for 1 second before updating the progress
    time.sleep(1)

    # If the progress reaches 100%, break the loop
    if progress >= 100:
        break

bar.finish()
