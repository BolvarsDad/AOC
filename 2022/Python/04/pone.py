import re

with open("input.txt") as file:
    overlap = 0

    for data in file:
        # number1-number2, number3-number4
        # complete overlap can be found if number1 <= number3 and number2 >= number4
        lines = re.split(',|-', data.strip())
        ranges = [eval(i) for i in lines]

        if ranges[0] <= ranges[2] and ranges[1] >= ranges[3]:
            overlap += 1

        elif ranges[2] <= ranges[0] and ranges[3] >= ranges[1]:
            overlap += 1

    print(overlap)
