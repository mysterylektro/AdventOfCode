from collections.abc import Iterable


def get_sum(obj: Iterable, no_red=False):

    def loop_items(cnt, items):
        for item in items:
            if isinstance(item, Iterable) and not isinstance(item, str):
                cnt += get_sum(item, no_red=no_red)
            elif isinstance(item, int):
                cnt += item
            else:
                continue
        return cnt

    count = 0
    if isinstance(obj, dict):
        keys, values = obj.keys(), obj.values()
        if no_red:
            if 'red' in keys or 'red' in values:
                return 0
        count = loop_items(count, values)
    else:
        count = loop_items(count, obj)

    return count


with open('../inputs/day12.txt') as f:
    line = f.readline()

struct = eval(line)
print(f"Part 1 Answer: {get_sum(struct)}")
print(f"Part 2 Answer: {get_sum(struct, no_red=True)}")
