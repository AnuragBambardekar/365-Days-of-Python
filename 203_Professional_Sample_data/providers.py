from faker import Faker
from faker.providers import BaseProvider
import random

f = Faker()

class BambaProvider(BaseProvider):
    def video_category(self):
        return random.choice(["ML","DL","Linux","Finance"])
    
f.add_provider(BambaProvider)
print(f.video_category())