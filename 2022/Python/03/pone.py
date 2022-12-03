import string

psum = 0
alphabet = string.ascii_lowercase + string.ascii_uppercase
charset = set(alphabet)

with open("input.txt") as file:
    for rucksacks in file:
        priorities = [alphabet.index(x) + 1 for x in rucksacks if x in charset]

        comp1 = set(priorities[:len(priorities)//2])
        comp2 = set(priorities[len(priorities)//2:])

        match = comp1 & comp2

        for priority in match:
            psum += priority

    print(psum)
