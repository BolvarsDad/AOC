with open("input.txt") as handle:
    rounds = [(ord(x[0]) - ord('A'), ord(x[1]) - ord('X')) for x in map(str.split, handle.readlines())]

print(sum(y + 1 + (y - x + 1) % 3 * 3 for x, y in rounds))
print(sum((x + y - 1) % 3 + 1 + y * 3 for x, y in rounds))
