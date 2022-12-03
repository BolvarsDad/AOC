import string

def score(char):
    return ord(char) - ord('a') + 1 if char.islower() else ord(char) - ord('A') + 27

bsum = 0

with open("input.txt") as file:
    rucksacks = file.read().splitlines()

    for i in range(0, len(rucksacks), 3):
        elf1 = set(rucksacks[i])
        elf2 = set(rucksacks[i + 1])
        elf3 = set(rucksacks[i + 2])

        match = elf1 & elf2 & elf3

        bsum += sum(map(score, match))

    print(bsum)
