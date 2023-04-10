class LogicGate:
    def __init__(self, input_count):
        self.input_count = input_count
        self.inputs = [0] * input_count
        self.output = None

    def set_input(self, input_num, value):
        self.inputs[input_num] = value

    def get_output(self):
        return self.output


class AndGate(LogicGate):
    def __init__(self):
        super().__init__(2)

    def evaluate(self):
        self.output = self.inputs[0] and self.inputs[1]


class OrGate(LogicGate):
    def __init__(self):
        super().__init__(2)

    def evaluate(self):
        self.output = self.inputs[0] or self.inputs[1]


class NotGate(LogicGate):
    def __init__(self):
        super().__init__(1)

    def evaluate(self):
        self.output = not self.inputs[0]


# Example usage of the logic gates
if __name__ == "__main__":
    # AND gate
    and_gate = AndGate()
    and_gate.set_input(0, 1) # (input_num, value)
    and_gate.set_input(1, 0)
    and_gate.evaluate()
    print("AND gate output: ", and_gate.get_output()) # 1 AND 0 = 0

    # OR gate
    or_gate = OrGate()
    or_gate.set_input(0, 1)
    or_gate.set_input(1, 0)
    or_gate.evaluate()
    print("OR gate output: ", or_gate.get_output()) # 1 OR 0 = 0

    # NOT gate
    not_gate = NotGate()
    not_gate.set_input(0, 1)
    not_gate.evaluate()
    print("NOT gate output: ", not_gate.get_output()) # NOT 1 = False
