"""
The name SR represents the SET and RESET function of the flipflop. This type of flip flop has two inputs named S & R for SET & RESET 
respectfully & and two outputs name Q & Q’, whereas Q’ is the invert of Q.

The SET function represents when output Q is high & Q’ is low. RESET function represents clear function when output Q low & Q’ High.

At each trigger pulse, the output of SR flipflop sets when the input S is high and input R is low. And clears the output when the input 
R is HIGH & S is low. When both inputs R & S are LOW, the output status Q & Q’ Remains unchanged.

Both HIGH input combination is considered forbidden (invalid) as they will produce race condition (indetermined state) which causes 
ambiguity in the system.

S	R	Q(t)	Q(t+1)
0	0	Q	      Q
0	1	Q	      0
1	0	0	      1
1	1	Q	undefined
"""
class SRFlipFlop:
    def __init__(self):
        self.Q = 0
        self.Qbar = 1

    def clock(self, S, R):
        if S == 0 and R == 0:
            pass
        elif S == 0 and R == 1:
            self.Q = 0
            self.Qbar = 1
        elif S == 1 and R == 0:
            self.Q = 1
            self.Qbar = 0
        elif S == 1 and R == 1:
            self.Q = None
            self.Qbar = None
            raise ValueError("Invalid input: S and R cannot be both 1")

# Sample test cases
ff = SRFlipFlop()

# Initial state should be Q=0 and Qbar=1
print("Initial state:")
print(f"Q = {ff.Q}")
print(f"Qbar = {ff.Qbar}")

# Set S=1 and R=0, Q should become 1 and Qbar should become 0
ff.clock(1, 0)
print("After setting S=1 and R=0:")
print(f"Q = {ff.Q}")
print(f"Qbar = {ff.Qbar}")

# Set S=0 and R=1, Q should become 0 and Qbar should become 1
ff.clock(0, 1)
print("After setting S=0 and R=1:")
print(f"Q = {ff.Q}")
print(f"Qbar = {ff.Qbar}")

# Set S=1 and R=1, should raise ValueError
try:
    ff.clock(1, 1)
except ValueError as e:
    print("After setting S=1 and R=1:")
    print(f"Error: {e}")
else:
    raise AssertionError("Expected ValueError not raised")

