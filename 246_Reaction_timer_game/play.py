import time
import random

def get_reaction_time():
    input("Press Enter to start...")
    
    # Wait for a random delay before prompting the user to react
    delay = random.uniform(1, 5)  # Change the range as needed
    time.sleep(delay)
    
    start_time = time.time()
    
    input("Press Enter again as fast as you can!")
    
    end_time = time.time()
    
    reaction_time = end_time - start_time
    return reaction_time

if __name__ == "__main__":
    print("Welcome to the Reaction Time Game!")
    input("Press Enter to begin...")
    
    reaction_time = get_reaction_time()
    
    print(f"Your reaction time: {reaction_time:.2f} seconds")
