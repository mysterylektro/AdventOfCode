from collections import Counter
two_count, three_count = 0, 0
for line in open('../inputs/day2.txt').readlines():
    count = Counter(line.strip())
    two_count += 1 if 2 in count.values() else 0
    three_count += 1 if 3 in count.values() else 0
    
print(two_count * three_count)