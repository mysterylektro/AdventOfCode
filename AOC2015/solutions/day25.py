row = 2981
column = 3075

num_times = column + sum(range(row + column - 1)) - 1

start_val = 20151125
multiplier = 252533
divisor = 33554393

val = start_val
for _ in range(num_times):
    val = divmod(val * multiplier, divisor)[1]

print(val)