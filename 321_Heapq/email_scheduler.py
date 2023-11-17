import datetime
import heapq
import time
from itertools import islice

class EmailScheduler:
    def __init__(self):
        self.fast_email = self.email(datetime.timedelta(minutes=15), "fast email")
        self.slow_email = self.email(datetime.timedelta(minutes=40), "slow email")
        self.unified = heapq.merge(self.fast_email, self.slow_email)

    def email(self, frequency, details):
        current = datetime.datetime.now()
        while True:
            current += frequency
            yield current, details

    def send_email(self, email_details):
        # Replace this with actual email sending logic
        print(f"Sending email: {email_details} at {datetime.datetime.now()}")

    def schedule_emails(self, num_emails):
        for _, details in islice(self.unified, num_emails):
            self.send_email(details)
            time.sleep(1)  # Optional: Add a delay between sending emails

if __name__ == "__main__":
    email_scheduler = EmailScheduler()
    email_scheduler.schedule_emails(num_emails=10)
