def bezout_coefficients(a, b):
    x, y, u, v = 1, 0, 0, 1

    while b != 0:
        q = a // b
        x, y = y, x - q * y
        u, v = v, u - q * v
        a, b = b, a - q * b

    return x, u


def sequenced_departure(bus_list):
    busses = [(bus, (bus - i) % bus) for i, bus in enumerate(bus_list) if bus > 0]
    bus_cycle, time = busses[0]
    for next_bus_cycle, next_offset in busses[1:]:
        x, y = bezout_coefficients(bus_cycle, next_bus_cycle)
        time = (next_offset * x * bus_cycle) + (time * y * next_bus_cycle)
        bus_cycle = bus_cycle * next_bus_cycle
        time %= bus_cycle

    return time


def earliest_time(start_time, bus_list):
    i = 0
    mod_values = [(start_time+i) % bus for bus in bus_list]
    while 0 not in mod_values:
        i += 1
        mod_values = [(start_time+i) % bus for bus in bus_list]
    idx = mod_values.index(0)
    return bus_list[idx], i


lines = [line.strip() for line in open('../inputs/day13.txt')]
start_time = int(lines[0].strip())
bus_list = [int(bus) if bus != "x" else 0 for bus in lines[1].strip().split(',')]

bus, departure = earliest_time(start_time, [x for x in bus_list if x > 0])
print(f"Part 1 Answer: {bus * departure}")

earliest_departure_time = sequenced_departure(bus_list)
print(f"Part 2 Answer: {earliest_departure_time}")
