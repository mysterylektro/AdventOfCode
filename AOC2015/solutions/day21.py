import numpy as np


weapon_input = """Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0""".splitlines()

armor_input = """Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5""".splitlines()

ring_input = """Damage+1    25     1       0
Damage+2    50     2       0
Damage+3   100     3       0
Defense+1   20     0       1
Defense+2   40     0       2
Defense+3   80     0       3""".splitlines()

weapons = {}
armors = {}
rings = {}
for line in weapon_input:
    name, cost, damage, armor = line.split()
    weapons[name] = tuple(map(int, (cost, damage, armor)))

for line in armor_input:
    name, cost, damage, armor = line.split()
    armors[name] = tuple(map(int, (cost, damage, armor)))

for line in ring_input:
    name, cost, damage, armor = line.split()
    rings[name] = tuple(map(int, (cost, damage, armor)))

weapon_values = [weapons[key][0] / weapons[key][1] for key in weapons]
armor_values = [armors[key][0] / armors[key][2] for key in weapons]
ring_values = [rings[key][0] / (rings[key][1] + rings[key][2]) for key in weapons]

def best_purchase():


    return purchase_type, purchase_name


class Player:
    def __init__(self, weapon):
        self.hp = 100
        self.weapon = weapon
        self.armor = 'none'
        self.ring1 = 'none'
        self.ring2 = 'none'
        self.damage = None
        self.defense = None

    @property
    def damage(self):
        dmg = weapons[self.weapon][1]
        if self.ring1 != 'none':
            dmg += rings[self.ring1][1]
        if self.ring2 != 'none':
            dmg += rings[self.ring2][1]
        return dmg

    @damage.setter
    def damage(self, value):
        self._damage = value

    @property
    def defense(self):
        val = 0
        if self.armor != 'none':
            val += armors[self.armor][2]
        if self.ring1 != 'none':
            val += rings[self.ring1][2]
        if self.ring2 != 'none':
            val += rings[self.ring2][2]
        return val

    @defense.setter
    def defense(self, value):
        self._defense = value

    def equipment_cost(self):
        cost = weapons[self.weapon][0]
        if self.armor != 'none':
            cost += armors[self.armor][0]
        if self.ring1 != 'none':
            cost += rings[self.ring1][0]
        if self.ring2 != 'none':
            cost += rings[self.ring2][0]

        return cost


class Boss:
    def __init__(self, hp, dmg, defense):
        self.hp = hp
        self.damage = dmg
        self.defense = defense


def does_player_win(player, boss):
    player_damage_per_turn = player.damage - boss.defense
    boss_damage_per_turn = boss.damage - player.defense

    player_turns = int(np.ceil(boss.hp / player_damage_per_turn))
    boss_turns = int(np.ceil(player.hp / boss_damage_per_turn))

    print(player_turns, boss_turns)

    return player_turns <= boss_turns


with open('../inputs/day21.txt') as f:
    lines = f.readlines()

hp = 0
dmg = 0
arm = 0
for line in lines:
    name, val = line.strip().split(': ')
    if name == 'Hit Points':
        hp = int(val)
    elif name == 'Damage':
        dmg = int(val)
    elif name == 'Armor':
        arm = int(val)
    else:
        raise ValueError("Incorrect input file")

boss = Boss(hp, dmg, arm)

initial_weapon = 'Dagger'
p = Player(initial_weapon)



while not (does_player_win(p, boss):


