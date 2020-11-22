class Reindeer:
    def __init__(self,
                 name,
                 speed,
                 fly_duration,
                 rest_duration):
        self.name = name
        self.speed = speed
        self.fly_duration = fly_duration
        self.rest_duration = rest_duration
        self.distance_travelled = 0
        self.points_earned = 0
        self.state = 'flying'
        self.fly_time = 0
        self.rest_time = 0

    def increment_time(self):
        if self.state == 'flying':
            self.fly_time += 1
            self.distance_travelled += self.speed
            if self.fly_time == self.fly_duration:
                self.rest_time = 0
                self.state = 'resting'
        elif self.state == 'resting':
            self.rest_time += 1
            if self.rest_time == self.rest_duration:
                self.state = 'flying'
                self.fly_time = 0


def emulate_race(reindeer_list,
                 total_seconds):
    time = 0
    while time <= total_seconds:
        time += 1
        distances = {}
        for reindeer in reindeer_list:
            reindeer.increment_time()
            distances[reindeer.distance_travelled] = reindeer

        largest_distance = max(distances.keys())
        distances[largest_distance].points_earned += 1


with open('../inputs/day14.txt') as f:
    lines = f.readlines()

list_of_reindeer = []

for line in lines:
    name, _, _, speed, _, _, duration, _, _, _, _, _, _, rest, _ = line.split(' ')
    speed, duration, rest = map(int, [speed, duration, rest])
    list_of_reindeer.append(Reindeer(name, speed, duration, rest))

number_seconds = 2503
emulate_race(list_of_reindeer, number_seconds)

max_distance = max([reindeer.distance_travelled for reindeer in list_of_reindeer])
max_points = max([reindeer.points_earned for reindeer in list_of_reindeer])

print(f"Part 1 Answer: {max_distance}")
print(f"Part 2 Answer: {max_points}")
