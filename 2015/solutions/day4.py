import hashlib

line = 'ckczppom'

count = 0
hash_output = hashlib.md5(bytes(line + str(count), 'UTF-8'))
while hash_output.hexdigest()[:5] != '00000':
    count += 1
    hash_output = hashlib.md5(bytes(line + str(count), 'UTF-8'))

print(f"Part 1 Answer: {count}")

count = 0
while hash_output.hexdigest()[:6] != '000000':
    count += 1
    hash_output = hashlib.md5(bytes(line + str(count), 'UTF-8'))

print(f"Part 2 Answer: {count}")
