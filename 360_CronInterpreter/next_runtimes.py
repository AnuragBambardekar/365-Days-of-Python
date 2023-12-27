# pip install croniter

from datetime import datetime
from croniter import croniter
import sys

def cron_interpreter(cron_expression, num_iterations=5):
    now = datetime.now()

    try:
        cron = croniter(cron_expression, now)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(f"Next {num_iterations} executions of the cron expression '{cron_expression}':")
    
    for _ in range(num_iterations):
        next_execution = cron.get_next(datetime)
        print(next_execution)
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <cron_expression>")
        sys.exit(1)

    cron_expression = sys.argv[1]
    cron_interpreter(cron_expression)

"""
python .\main.py "* * * * *"
Next 5 executions of the cron expression '* * * * *':
2023-12-27 06:53:00
2023-12-27 06:54:00
2023-12-27 06:55:00
2023-12-27 06:56:00
2023-12-27 06:57:00
"""