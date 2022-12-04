import string

bsum = 0
alphabet = string.ascii_lowercase + string.ascii_uppercase
charset = set(alphabet)

with open("input.txt") as file:
    rucksacks = file.read().splitlines()

    for i in range(0, len(rucksacks), 3):
        elf1, elf2, elf3 = map(set, rucksacks[i:i+3])

        priorities = [alphabet.index((elf1 & elf2 & elf3).pop()) + 1]

        for typeval in priorities:
            bsum += typeval

    print(bsum)
