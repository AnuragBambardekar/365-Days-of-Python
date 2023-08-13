# A simple simulation

import simpy

def customer(env, name, counter):
    print(f"{name} arrives at {env.now}")
    with counter.request() as req:
        yield req

        print(f"{name} starts being served at {env.now}")
        yield env.timeout(1)  # Time it takes to serve a customer

        print(f"{name} finishes at {env.now}")

env = simpy.Environment()
counter = simpy.Resource(env, capacity=2) # number of counters

for i in range(3):
    env.process(customer(env, f"Customer {i}", counter))

env.run()
