from tqdm import trange
import random
import time

with trange(1000) as t:
    for i in t:
        t.set_description(f"Iteration Number: {i+1}")
        sleeping_time = random.randint(1,100)/100
        t.set_postfix(something=random.randint(0,100),
                        sleeping_time=sleeping_time) 
        # show something sensible here, like loss, mean, standard deviation, training a neural network (just change "something" to desired variable)
        time.sleep(sleeping_time)

        if i%100 == 0:
            for _ in range(10):
                time.sleep(0.5)
