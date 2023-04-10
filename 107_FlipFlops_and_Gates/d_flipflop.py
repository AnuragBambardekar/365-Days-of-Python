"""
You can say that D flip-flop is a modified form of SR flip flop because design-wise, D flip flop is the same as SR flip flop 
with only a minor change. 
In D flip-flop, the inputs of SR flip flop are combined together into a single input D with one of the input R inverted.

This configuration eliminates the invalid inputs combinations as there cannot be the same inputs.

During the clock pulse, D flipflops SET output when its input is High & Resets when the input is LOW. It is easier to configure as 
compared to SR Flip flop because there are no Invalid inputs.

D	Q(t)	Q(t+1)
0	Q	      0
1	Q	      1

In the D flip-flop, the output state is set to the value of the D input. When D is 0, the output state is set to 0. 
When D is 1, the output state is set to 1.
"""

class DFlipFlop:
    def __init__(self):
        self.Q = 0
        self.Qbar = 1

    def clock(self, D):
        if D == 0:
            self.Q = 0
            self.Qbar = 1
        else:
            self.Q = 1
            self.Qbar = 0

# Sample test cases
ff = DFlipFlop()

# Initial state should be Q=0 and Qbar=1
print("Initial state:")
print(f"Q = {ff.Q}")
print(f"Qbar = {ff.Qbar}")

# Set D=1, Q should become 1 and Qbar should become 0
ff.clock(1)
print("After setting D=1:")
print(f"Q = {ff.Q}")
print(f"Qbar = {ff.Qbar}")

# Set D=0, Q should become 0 and Qbar should become 1
ff.clock(0)
print("After setting D=0:")
print(f"Q = {ff.Q}")
print(f"Qbar = {ff.Qbar}")
