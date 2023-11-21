# Solution for Day 3

INPUT_PATH = "./2022/Day_03/input.txt"
TEST_PATH = "./2022/Day_03/test_input.txt"


with open(INPUT_PATH) as file:
    lines = file.read().split("\n")

priorities = []
# Part 1
# Split each line in half (0 is c1, 1 is c2)
for line in lines:
    mid = len(line) // 2
    c1 = line[:mid]
    c2 = line[mid:]

    # loop through first half, see if it exists in second
    for letter in c1:
        try:
            match = c2.index(letter)
            letter = c2[match]
            priorities.append(ord(letter) - (96 if letter.islower() else 38))
            break

        except ValueError:
            continue

# print(priorities)
print(sum(priorities))

# PART 2
for line in lines:
    mid = len(line) // 2
    c1 = line[:mid]
    c2 = line[mid:]

    # loop through first half, see if it exists in second
    for letter in c1:
        try:
            match = c2.index(letter)
            letter = c2[match]
            priorities.append(ord(letter) - (96 if letter.islower() else 38))
            break

        except ValueError:
            continue

# print(priorities)
print(sum(priorities))
