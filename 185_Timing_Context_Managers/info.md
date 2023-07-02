# Class-Based Context Manager
To create a class-based context manager, the dunder methods __enter__ and __exit__ need to be implemented. The first one is called when entering a context (manager), the latter is called when leaving the context.

With this knowledge we can create a Timer class implementing both methods. When entering the context, we want to get the current time and save it to a start instance variable. If we leave the context, we want to get the current time and subtract the start time from it. The result is printed.

# Generator-Based Context Manager
The generator-based approach is a bit more straightforward. Basically, we create a generator function containing the program flow (taking start and end time as well as printing the elapsed time). Then, we utilize the contextlib's @contextmanager decorator to turn the generator function into a proper context manager.