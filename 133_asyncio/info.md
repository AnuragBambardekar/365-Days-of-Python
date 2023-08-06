# Asynchronous Programming
- It is not multi-threading
- It is not multi-processing
- It is concurrent programming

```python
func1()
func2()
func3()

# synchronous means
# We will call func1(), then func2() when func1() returns, then func3() when func2() returns

# in multithreading
# we will define 3 threads and create an illusion of three functions executing simultaneously

# with async programming
# if func1() starts executing and waits for some data from a Database for example, then we don't want to waste the CPU cycles.
# We want to load func2() on the CPU eventhough func1() has not returned yet/sleeping/waiting/being unproductive
```

In python, we can load the ```asyncio``` library.