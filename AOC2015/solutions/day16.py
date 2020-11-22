class Sue:
    def __init__(self,
                 number: int,
                 children: int = None,
                 cats: int = None,
                 samoyeds: int = None,
                 pomeranians: int = None,
                 akitas: int = None,
                 vizslas: int = None,
                 goldfish: int = None,
                 trees: int = None,
                 cars: int = None,
                 perfumes: int = None):
        self.number = number
        self.children = children
        self.cats = cats
        self.samoyeds = samoyeds
        self.pomeranians = pomeranians
        self.akitas = akitas
        self.vizslas = vizslas
        self.goldfish = goldfish
        self.trees = trees
        self.cars = cars
        self.perfumes = perfumes

    def match(self, **kwargs) -> bool:
        for key, value in kwargs.items():
            try:
                if self.__getattribute__(key) is None:
                    continue
                elif self.__getattribute__(key) != value:
                    return False
            except AttributeError:
                continue
        return True

    def real_match(self, **kwargs) -> bool:
        operation = {'cats': '<=',
                     'trees': '<=',
                     'pomeranians': '>=',
                     'goldfish': '>='}

        for key, value in kwargs.items():
            try:
                if self.__getattribute__(key) is None:
                    continue
                op = operation.get(key, '!=')
                cmd = f"{self.__getattribute__(key)} {op} {value}"
                failed = eval(cmd)
                if failed:
                    return False
            except AttributeError:
                continue
        return True


attributes = {'children': 3,
              'cats': 7,
              'samoyeds': 2,
              'pomeranians': 3,
              'akitas': 0,
              'vizslas': 0,
              'goldfish': 5,
              'trees': 3,
              'cars': 2,
              'perfumes': 1}

with open('../inputs/day16.txt') as f:
    lines = f.readlines()

sue_list = []
for line in lines:
    line = line.strip().replace(', ', ': ')
    tokens = line.split(': ')
    name = tokens.pop(0)
    _, number = name.split(' ')
    number = int(number)
    parameters = {'number': number}
    for param, val in zip(tokens[::2], tokens[1::2]):
        parameters[param] = int(val)
    sue_list.append(Sue(**parameters))

matching_sue = None
for sue in sue_list:
    if sue.match(**attributes):
        matching_sue = sue
        break

if matching_sue is not None:
    print(f"Part 1 Answer: {matching_sue.number}")

matching_sue = None
for sue in sue_list:
    if sue.real_match(**attributes):
        matching_sue = sue
        break

if matching_sue is not None:
    print(f"Part 2 Answer: {matching_sue.number}")
