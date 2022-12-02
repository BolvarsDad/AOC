with open("input.txt", 'r') as handle:
    elves = [[int(line) for line in kcal.split("\n")] for kcal in handle.read()[:-1].split("\n\n")]
    
    print(max(sum(kcals) for kcals in elves))
    print(sum(sorted([sum(kcals) for kcals in elves])[-3:]))
