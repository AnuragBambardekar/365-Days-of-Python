import simpy
import random
import statistics

wait_times = []

class Theater(object):
    def __init__(self, env, num_cashiers, num_servers, num_ushers):
        self.env = env
        self.cashier = simpy.Resource(env, num_cashiers)
        self.server = simpy.Resource(env, num_servers)
        self.usher = simpy.Resource(env, num_ushers)

    def purchase_ticket(self, moviegoer):
        yield self.env.timeout(random.randint(1, 3)) # average time of 1-3 minutes

    def check_ticket(self, moviegoer):
        yield self.env.timeout(3 / 60) # Since simpy works in minutes, average time of 3 seconds needs to be passed as a fraction of a minute

    def sell_food(self, moviegoer):
        yield self.env.timeout(random.randint(1, 5)) # average time of 1-5 minutes



# The setup
def go_to_movies(env, moviegoer, theater):
    # Moviegoer arrives at the theater
    arrival_time = env.now

    # Simulation: Buy Ticket
    with theater.cashier.request() as request:
        yield request #  moviegoer waits for a cashier to become available if all are currently in use. 
        
        # moviegoer uses an available cashier to complete the given process.
        yield env.process(theater.purchase_ticket(moviegoer))

        # After a resource is used, it must be freed up for the next agent to use. 
        # You could do this explicitly with release(), but in the code above, you use a with statement instead. 
        # This shortcut tells the simulation to automatically release the resource once the process is complete.

    # Simulation: Check Ticket
    with theater.usher.request() as request:
        yield request
        yield env.process(theater.check_ticket(moviegoer))

    # Not all moviegoers buy food, so introduce randomness
    # Simulation: Buy Food
    if random.choice([True, False]):
        with theater.server.request() as request:
            yield request
            yield env.process(theater.sell_food(moviegoer))

    # Moviegoer heads into the theater
    wait_times.append(env.now - arrival_time)

# Start the Theater simulation
def run_theater(env, num_cashiers, num_servers, num_ushers):
    """
    the simulation will generate 3 moviegoers to start and begin moving them through the theater with go_to_movies(). 
    After that, new moviegoers will arrive at the theater with an interval of 12 seconds and move through the theater in their own time.
    """
    theater = Theater(env, num_cashiers, num_servers, num_ushers)

    # initialize the first 3 moviegoers
    for moviegoer in range(3):
        env.process(go_to_movies(env, moviegoer, theater)) # populate the theater with 3 moviegoers
    
    while True:
        yield env.timeout(0.20) # moviegoers arrive every 12 seconds so, 12/60 = 0.20

        moviegoer += 1
        env.process(go_to_movies(env, moviegoer, theater))

# Get the average wait time
def get_average_wait_time(wait_times):
    average_wait = statistics.mean(wait_times)

    # Make the average wait time readable
    minutes, frac_minutes = divmod(average_wait, 1)
    seconds = frac_minutes * 60
    return round(minutes), round(seconds)


# Get the inputs pertaining to the theater
def get_user_input():
    num_cashiers = input("Input # of cashiers working: ")
    num_servers = input("Input # of servers working: ")
    num_ushers = input("Input # of ushers working: ")
    params = [num_cashiers, num_servers, num_ushers]
    if all(str(i).isdigit() for i in params):  # Check input is valid
        params = [int(x) for x in params]
    else:
        print(
            "Could not parse input. The simulation will use default values:",
            "\n1 cashier, 1 server, 1 usher.",
        )
        params = [1, 1, 1]
    return params

def main():
    # Setup
    random.seed(42)
    num_cashiers, num_servers, num_ushers = get_user_input()

    # Run the simulation
    env = simpy.Environment()
    env.process(run_theater(env, num_cashiers, num_servers, num_ushers))
    env.run(until=20)

    # View the results
    mins, secs = get_average_wait_time(wait_times)
    print(
        "Running simulation...",
        f"\nThe average wait time is {mins} minutes and {secs} seconds.",
    )

if __name__ == '__main__':
    main()