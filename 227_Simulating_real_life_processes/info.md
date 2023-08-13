# SimPy

SimPy is a powerful tool for modeling and analyzing complex systems, such as manufacturing processes, transportation systems, and more. It allows you to gain insights into how different components interact and how changes in parameters can affect the overall system behavior.

- Processes: In SimPy, you model entities or processes that interact with each other. A process is defined as a Python generator function. Each process can create other processes and interact with shared resources.

- Events: Events are points in time where something significant happens in the simulation. Processes can yield to an event, causing the process to pause until that event occurs.

- Resources: SimPy provides mechanisms for modeling shared resources such as queues, servers, and more. Processes can request and release resources, and SimPy manages the allocation and scheduling of resources.

- Environment: The core of a SimPy simulation is the Environment. It manages the scheduling of events, processes, and resources. You create an instance of the Environment class to run your simulation.

### Movie theater simulation - explanation

Theater: This class definition serves as a blueprint for the environment you want to simulate. It determines some information about that environment, like what kinds of resources are available, and what processes are associated with them.

go_to_movies(): This function makes explicit requests to use a resource, goes through the associated process, and then releases it to the next moviegoer.

run_theater(): This function controls the simulation. It uses the Theater class blueprint to create an instance of a theater, and then calls on go_to_movies() to generate and move people through the theater.

get_average_wait_time(): This function finds the average time it takes a moviegoer to make it through the theater.

calculate_wait_time(): This function ensures the final output is easy for the user to read.

get_user_input(): This function allows the user to define some parameters, like how many cashiers are available.

main(): This function ensures that your script runs properly in the command line.

### Airport simulation - explanation

- Airport Class:

The Airport class represents the different resources (check-in desks, security gates, immigration officers, and boarding gates) at the airport. It's initialized with the number of each resource available.
Each resource is represented as a simpy.Resource object that simulates the availability and usage of that resource.

- Passenger Processes:

check_in(self, passenger): Simulates the check-in process for a passenger. The passenger waits for an available check-in desk, then spends a random amount of time (between 2 to 5 minutes) checking in.
security_check(self, passenger): Simulates the security check process for a passenger. Similar to check-in, the passenger waits for an available security gate and spends a random amount of time (between 1 to 3 minutes) being checked by security.
immigration_process(self, passenger): Simulates the immigration process for a passenger. The passenger waits for an available immigration officer and spends a random amount of time (between 3 to 6 minutes) going through immigration.
board_plane(self, passenger): Simulates the boarding process for a passenger. The passenger waits for an available boarding gate and spends a random amount of time (between 2 to 4 minutes) boarding the plane.

- Passenger Flow Process:

passenger_flow(env, passenger, airport): Represents the entire sequence of processes a passenger goes through at the airport. The passenger arrives, checks in, goes through security, immigration, and boards the plane. The total time taken is recorded in the wait_times list.

- Airport Simulation Process:

airport_simulation(env, num_checkin_desks, num_security_gates, num_immigration_officers, num_boarding_gates): Sets up the airport simulation environment. It creates an Airport instance and initializes the simulation with a fixed number of initial passengers (10 in this case). It then generates new passengers at intervals of 5 simulated minutes.

- Average Wait Time Calculation:

get_average_wait_time(wait_times): Calculates the average wait time of passengers based on the recorded wait_times list. It calculates the mean of the wait times and converts it to a readable format of minutes and seconds.

- Main Function:

main(): This is the main entry point of the simulation. It initializes the random number generator, sets the number of resources available at the airport, creates a simulation environment, runs the simulation for a specified time (120 simulated minutes), calculates and displays the average wait time.