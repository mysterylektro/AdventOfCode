OPERATORS = {'LSHIFT': '<<',
             'RSHIFT': '>>',
             'AND': '&',
             'OR': '|',
             'NOT': '~'}

memo = {}


def memoize(func: callable):
    def wrapper(obj):
        if obj not in memo:
            memo[obj] = func(obj)
        return memo[obj]
    return wrapper


class Source:
    def __init__(self):
        self.value = None

    def set_value(self, value):
        self.value = value

    @memoize
    def get_value(self):
        return self.value


class Wire(Source):
    def __init__(self, name):
        self.name = name
        self.source = None
        super().__init__()

    @memoize
    def get_value(self):
        if self.source is not None:
            return self.source.get_value()
        else:
            return None


class Gate(Source):
    def __init__(self,
                 gate_type: str,
                 output: Wire):
        self.gate_type = gate_type
        self.input1 = None
        self.input2 = None
        super().__init__()

    def get_operator(self):
        return OPERATORS.get(self.gate_type)

    def num_inputs(self):
        return 1 if self.gate_type in ['NOT'] else 2

    def set_input1(self, value: Source):
        self.input1 = value

    def set_input2(self, value: Source):
        self.input2 = value

    @memoize
    def get_value(self):
        input1 = self.input1.get_value()
        if self.num_inputs() == 1:
            if input1 is None:
                return None
            return eval(self.get_operator() + str(input1))

        input2 = self.input2.get_value()
        if self.num_inputs() == 2:
            if [input1, input2].count(None) > 0:
                return None
            return eval(str(input1) +
                        self.get_operator() +
                        str(input2))


def add_wire(name, wire_set, wire_dict):
    if name not in wires:
        wire = Wire(name)
        wire_set.add(name)
        wire_dict[name] = wire


def handle_three_tokens(wire_set, wire_dict, tokens, output_wire):
    input1, operation, input2 = tokens
    gate = Gate(operation, output_wire)
    output_wire.source = gate
    if input1.isnumeric():
        source = Source()
        source.value = int(input1)
        gate.set_input1(source)
    else:
        add_wire(input1, wire_set, wire_dict)
        gate.set_input1(wire_dict[input1])

    if input2.isnumeric():
        source = Source()
        source.value = int(input2)
        gate.set_input2(source)
    else:
        add_wire(input2, wire_set, wire_dict)
        gate.set_input2(wire_dict[input2])


def handle_two_tokens(wire_set, wire_dict, tokens, output_wire):
    operation, input1 = tokens
    gate = Gate(operation, output_wire)
    output_wire.source = gate
    if input1.isnumeric():
        source = Source()
        source.value = int(input1)
        gate.set_input1(source)
    else:
        add_wire(input1, wire_set, wire_dict)
        gate.set_input1(wire_dict[input1])


def handle_one_token(wire_set, wire_dict, tokens, output_wire):
    if tokens[0].isnumeric():
        source = Source()
        source.set_value(int(tokens[0]))
    else:
        add_wire(tokens[0], wire_set, wire_dict)
        source = wire_dict[tokens[0]]
    output_wire.source = source


wires = set()
wire_dict = {}

with open('../inputs/day7.txt') as f:
    lines = f.readlines()

for line in lines:
    tokens = line.split('->')
    expression = tokens[0].strip()
    output_wire_name = tokens[1].strip()
    add_wire(output_wire_name, wires, wire_dict)

    output_wire = wire_dict[output_wire_name]

    options = {1: handle_one_token,
               2: handle_two_tokens,
               3: handle_three_tokens}

    expression = expression.split(' ')
    f = options.get(len(expression))
    f(wires, wire_dict, expression, output_wire)

print(f"Part 1 Answer: {wire_dict['a'].get_value()}")

source = Source()
source.set_value(wire_dict['a'].get_value())
wire_dict['b'].source = source
memo = {}

print(f"Part 2 Answer: {wire_dict['a'].get_value()}")
