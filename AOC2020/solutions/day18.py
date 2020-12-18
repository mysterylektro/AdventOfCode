import operator
import re

operations = {'+': operator.add,
              '*': operator.mul}


def innermost_parenthesis(expression):
    s = [m.start() for m in re.finditer(r'\(', expression)]
    e = [m.start() for m in re.finditer(r'\)', expression)]
    if len(s) > 0:
        e = e[0]
        s = max([i for i in s if i < e])
        return s, e
    else:
        return None, None


def evaluate_p1(expression):
    def evaluate(expr):
        items = expr.split(' ')
        a = int(items.pop(0))
        while len(items) > 0:
            op = operations.get(items.pop(0))
            b = int(items.pop(0))
            a = op(a, b)
        return a

    start, end = innermost_parenthesis(expression)
    while start is not None:
        res = str(evaluate(expression[start + 1:end]))
        expression = expression[:start] + res + expression[end + 1:]
        start, end = innermost_parenthesis(expression)
    return evaluate(expression)


def evaluate_p2(expression):
    tokens = expression.split(' ')
    indices = [i for i, j in enumerate(tokens) if j == '+']
    for i in indices:
        tokens[i-1] = '(' + tokens[i-1]
        tokens[i+1] = tokens[i+1] + ')'
    return eval(' '.join(tokens))


p1, p2 = 0, 0
for line in [line.strip() for line in open('../inputs/day18.txt')]:
    p1 += evaluate_p1(line)
    p2 += evaluate_p2(line)

print(f"Part 1 Answer: {p1}")
print(f"Part 2 Answer: {p2}")
