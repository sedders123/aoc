freq = 0
with open("input.txt") as f:
    for l in f:
        freq += int(l)
print(freq)
