import re

stacks = {
    1: ['N', 'C', 'R', 'T', 'M', 'Z', 'P'],
    2: ['D', 'N', 'T', 'S', 'B', 'Z'],
    3: ['M', 'H', 'Q', 'R', 'F', 'C', 'T', 'G'],
    4: ['G', 'R', 'Z'],
    5: ['Z', 'N', 'R', 'H'],
    6: ['F', 'S', 'H', 'W', 'P', 'Z', 'L', 'D'],
    7: ['W', 'D', 'Z', 'R', 'C', 'G', 'M'],
    8: ['S', 'J', 'F', 'L', 'H', 'W', 'Z', 'Q'],
    9: ['S', 'Q', 'P', 'W', 'N']
}

with open("input.txt") as file:
    moves = []

    for line in file:
        instruction_vals = re.findall(r'\d{1,2}', line)
        if instruction_vals:
            instruction_vals = list(map(int, [val for val in instruction_vals]))
            moves.append(instruction_vals)

    for move in moves:
        crate_stack = []

        for i in range(move[0]):
            crate = stacks[move[1]].pop()
            crate_stack.append(crate)

        crate_stack.reverse()
        for crates in crate_stack:
            stacks[move[2]].append(crates)

    ans = ''.join([val[-1] for val in stacks.values()])

    print(ans)
