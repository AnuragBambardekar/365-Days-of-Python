import simpy
import random
import statistics

wait_times = []

class Airport(object):
    def __init__(self, env, num_checkin_desks, num_security_gates, num_immigration_officers, num_boarding_gates):
        self.env = env
        self.checkin_desk = simpy.Resource(env, num_checkin_desks)
        self.security_gate = simpy.Resource(env, num_security_gates)
        self.immigration_officer = simpy.Resource(env, num_immigration_officers)
        self.boarding_gate = simpy.Resource(env, num_boarding_gates)

    def check_in(self, passenger):
        yield self.env.timeout(random.randint(2, 5))  # Average check-in time of 2-5 minutes

    def security_check(self, passenger):
        yield self.env.timeout(random.randint(1, 3))  # Average security check time of 1-3 minutes

    def immigration_process(self, passenger):
        yield self.env.timeout(random.randint(3, 6))  # Average immigration process time of 3-6 minutes

    def board_plane(self, passenger):
        yield self.env.timeout(random.randint(2, 4))  # Average boarding time of 2-4 minutes

def passenger_flow(env, passenger, airport):
    arrival_time = env.now

    with airport.checkin_desk.request() as request:
        yield request
        yield env.process(airport.check_in(passenger))

    with airport.security_gate.request() as request:
        yield request
        yield env.process(airport.security_check(passenger))

    with airport.immigration_officer.request() as request:
        yield request
        yield env.process(airport.immigration_process(passenger))

    with airport.boarding_gate.request() as request:
        yield request
        yield env.process(airport.board_plane(passenger))

    wait_times.append(env.now - arrival_time)

def airport_simulation(env, num_checkin_desks, num_security_gates, num_immigration_officers, num_boarding_gates):
    airport = Airport(env, num_checkin_desks, num_security_gates, num_immigration_officers, num_boarding_gates)

    for passenger in range(10):  # Start with 10 passengers
        env.process(passenger_flow(env, passenger, airport))

    while True:
        yield env.timeout(5)  # New passengers arrive every 5 minutes
        passenger += 1
        env.process(passenger_flow(env, passenger, airport))

def get_average_wait_time(wait_times):
    average_wait = statistics.mean(wait_times)
    minutes, frac_minutes = divmod(average_wait, 1)
    seconds = frac_minutes * 60
    return round(minutes), round(seconds)

def main():
    random.seed(42)
    num_checkin_desks, num_security_gates, num_immigration_officers, num_boarding_gates = 3, 2, 2, 1

    env = simpy.Environment()
    env.process(airport_simulation(env, num_checkin_desks, num_security_gates, num_immigration_officers, num_boarding_gates))
    env.run(until=120)  # Run the simulation for 120 simulated minutes

    mins, secs = get_average_wait_time(wait_times)
    print(
        "Running simulation...",
        f"\nThe average wait time is {mins} minutes and {secs} seconds.",
    )

if __name__ == '__main__':
    main()
