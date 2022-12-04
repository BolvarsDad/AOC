import re

def overlap_fn(start1, end1, start2, end2):
    return (
        start1 <= start2 <= end1 or
        start1 <= end2 <= end1 or
        start2 <= start1 <= end2 or
        start2 <= end1 <= end2
    )

with open("input.txt") as file:
    overlap = 0

    for data in file:
        lines = re.split(',|-', data.strip())
        ranges = [eval(i) for i in lines]

        overlap += overlap_fn(ranges[0], ranges[1], ranges[2], ranges[3])

    print(overlap)

