from collections import Counter

INPUT_PATH = "./2024/Day_01/input.txt"

# Solution for Day 1

# S1
with open(INPUT_PATH) as file:
    diff_sum = 0
    lines = file.read().split("\n")

    list_a = [int(line.split()[0]) for line in lines]
    list_a.sort()
    list_b = [int(line.split()[1]) for line in lines]
    list_b.sort()

    for i, val in enumerate(list_a):
        diff = abs(val - list_b[i])
        diff_sum += diff

print(diff_sum)

# S2
with open(INPUT_PATH) as file:
    similarity_score = 0
    lines = file.read().split("\n")

    list_a = [int(line.split()[0]) for line in lines]
    counter_b = Counter([int(line.split()[1]) for line in lines])

    for i, val in enumerate(list_a):
        similarity = val * counter_b.get(val, 0)
        similarity_score += similarity

print(similarity_score)
