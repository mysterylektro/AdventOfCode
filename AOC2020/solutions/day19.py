def check_sub_rule(rule, string):
    for i, r in enumerate(rule):
        if r[0] == '"':
            if string and r[1] == string[0]:
                string = string[1:]
            else:
                return False
        else:
            return check_rule([t + rule[i + 1:] for t in rules[r]], string)
    return not string


def check_rule(rule, string):
    return any(check_sub_rule(r, string) for r in rule)


rules, messages = open('../inputs/day19.txt').read().split('\n\n')
messages = messages.split('\n')[:-1]
rules = {i: [num.split() for num in rule.split('|')] for i, rule in [r.split(': ') for r in rules.split('\n')]}


count = 0
for message in messages:
    count += 1 if check_rule(rules['0'], message) else 0
print(count)

# Part2
rules['8'] += [['42', '8']]
rules['11'] += [['42', '11', '31']]

count = 0
for message in messages:
    count += 1 if check_rule(rules['0'], message) else 0
print(count)
