def find_distinct(message, n):
    for i in range(len(message)-n):
        if len(set(message[i:i+n])) == n:
            return i+n
    return None

contents = open("input.txt").read()
print("Part 1:", find_distinct(contents, 4))
print("Part 2:", find_distinct(contents, 14))
