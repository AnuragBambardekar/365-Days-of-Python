from datetime import datetime
from croniter import croniter
import sys

def interpret_cron_expression(cron_expression):
    parts = cron_expression.split()
    
    if len(parts) != 5:
        print("Invalid cron expression. It should have five fields separated by spaces.")
        sys.exit(1)

    minute, hour, day_of_month, month, day_of_week = parts

    print("Cron Expression:")
    print(f"Minute: {minute}")
    print(f"Hour: {hour}")
    print(f"Day of Month: {day_of_month}")
    print(f"Month: {month}")
    print(f"Day of Week: {day_of_week}\n")

    now = datetime.now()

    try:
        cron = croniter(cron_expression, now)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(f"Next execution time: {cron.get_next(datetime)}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <cron_expression>")
        sys.exit(1)

    cron_expression = sys.argv[1]
    interpret_cron_expression(cron_expression)
