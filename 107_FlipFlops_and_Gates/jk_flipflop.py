"""
JK flipflop can also be considered a better and modified version of SR flip-flop with J input corresponding to SET and K input 
corresponding to RESET of the JK flipflop. The invalid inputs of the SR flip-flops are used in this type of flipflop for a meaning 
full function.

When both inputs are high the output status is toggled during each clock cycle. When the inputs are same, the JK flip-flop retains 
its original status even after clock pulses.

In the JK flip-flop, the J and K inputs are used to toggle the output state. 
When J and K are both 0, the output state remains unchanged. When J is 1 and K is 0, the output state is set to 1. 
When J is 0 and K is 1, the output state is set to 0. When both J and K are 1, the output state is toggled.

J	K	Q(t)	Q(t+1)
0	0	Q	      Q
0	1	Q	      0
1	0	1	      0
1	1	~Q	      Q
"""

class JKFlipFlop:
    def __init__(self):
        self.Q = 0
        self.Qbar = 1

    def clock(self, J, K):
        if J == 0 and K == 1:
            self.Q = 0
            self.Qbar = 1
        elif J == 1 and K == 0:
            self.Q = 1
            self.Qbar = 0
        elif J == 1 and K == 1:
            self.Q = 1 - self.Q
            self.Qbar = 1 - self.Qbar
        # added condition to maintain previous state if J=0 and K=0
        elif J == 0 and K == 0:
            pass

# Sample test cases
ff = JKFlipFlop()

# Initial state should be Q=0 and Qbar=1
print("Initial state:")
print(f"Q = {ff.Q}")
print(f"Qbar = {ff.Qbar}")

# Set J=1 and K=0, Q should become 1 and Qbar should become 0
ff.clock(1, 0)
print("After setting J=1 and K=0:")
print(f"Q = {ff.Q}")
print(f"Qbar = {ff.Qbar}")

# Set J=0 and K=1, Q should become 0 and Qbar should become 1
ff.clock(0, 1)
print("After setting J=0 and K=1:")
print(f"Q = {ff.Q}")
print(f"Qbar = {ff.Qbar}")

# Set J=1 and K=1, Q should toggle to 0 and Qbar should toggle to 1
ff.clock(1, 1)
print("After setting J=1 and K=1:")
print(f"Q = {ff.Q}")
print(f"Qbar = {ff.Qbar}")

# Set J=0 and K=0, should maintain previous state
ff.clock(0, 0)
print("After setting J=0 and K=0:")
print(f"Q = {ff.Q}")
print(f"Qbar = {ff.Qbar}")
