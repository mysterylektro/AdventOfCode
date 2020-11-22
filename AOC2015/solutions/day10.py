def look_and_say(input_string: str) -> str:

    def count_numbers(idx, input_str):
        cnt = 1
        val = input_str[idx]
        idx += 1
        while idx < len(input_str):
            if input_str[idx] == input_str[idx - 1]:
                cnt += 1
            else:
                break
            idx += 1

        return idx, cnt, val

    output_str = ''
    index = 0
    while index < len(input_string):
        index, count, value = count_numbers(index, input_string)
        output_str += str(count) + value

    return output_str


string = '1113122113'
for _ in range(40):
    string = look_and_say(string)

print(f"Part 1 Answer: {len(string)}")

for _ in range(10):
    string = look_and_say(string)

print(f"Part 2 Answer: {len(string)}")
