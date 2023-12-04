# Solution for Day 1

INPUT_PATH = "./2023/Day_01/input.txt"

text_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

with open(INPUT_PATH) as file:
    lines = file.read().split("\n")

combos = []
for line in lines:
    COMBO = ""
    # first digit
    for l in line:
        if l.isdigit():
            COMBO = COMBO + l
            break

    for l in line[::-1]:
        if l.isdigit():
            COMBO = COMBO + l
            break

    combos.append(int(COMBO))

print(sum(combos))

# P2
combos = []
for line in lines:
    COMBO = ""
    TEXT = ""
    FIRST_DIGIT_FOUND = False
    SECOND_DIGIT_FOUND = False

    # first digit
    for l in line:
        if l.isdigit():
            COMBO += l
            TEXT = ""
            FIRST_DIGIT_FOUND = True
            break
        else:
            TEXT += l
            for index in range(len(TEXT) - 1):
                found = text_map.get(TEXT[index:])

                if found is not None:
                    COMBO += found
                    TEXT = ""
                    FIRST_DIGIT_FOUND = True
                    break

        if FIRST_DIGIT_FOUND:
            break

    for l in line[::-1]:
        if l.isdigit():
            COMBO += l
            TEXT = ""
            SECOND_DIGIT_FOUND = True
            break
        else:
            # reverse check starting from beginning
            TEXT += l
            reversed_text = TEXT[::-1]
            for index in range(len(reversed_text)):
                found = text_map.get(reversed_text[0 : len(reversed_text) - index])

                if found is not None:
                    COMBO += found
                    SECOND_DIGIT_FOUND = True
                    break
        if SECOND_DIGIT_FOUND:
            break

    combos.append(int(COMBO))

# P2 answer
print(sum(combos))
