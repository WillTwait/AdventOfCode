# Solution for Day 2

INPUT_PATH = "./2023/Day_02/input.txt"

MAX_CONTENTS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

with open(INPUT_PATH) as file:
    lines = file.read().split("\n")

# P1 & P2
valid_games = []
game_powers = []

for game in lines:
    parsed_round = game.split(": ", 1)
    game_number = int(parsed_round[0].split(" ")[1])

    draws = parsed_round[1].split("; ")
    DRAW_VALIDITY = []

    MIN_COUNTS = {"red": 0, "green": 0, "blue": 0}

    for draw in draws:
        pulls = draw.split(", ")

        for pull in pulls:
            split_pull = pull.split(" ")
            pull_value = split_pull[0]
            pull_color = split_pull[1]

            # Check min
            if MIN_COUNTS[pull_color] < int(pull_value):
                MIN_COUNTS[pull_color] = int(pull_value)

            # Check validity
            if MAX_CONTENTS[pull_color] < int(pull_value):
                DRAW_VALIDITY.append(False)
            else:
                DRAW_VALIDITY.append(True)

        # if any pull is invalid, this game number is invalid
    if all(value for value in DRAW_VALIDITY):
        valid_games.append(game_number)

    POWER = 1
    for value in MIN_COUNTS.values():
        POWER = POWER * value

    game_powers.append(POWER)

print(f"p1: {sum(valid_games)}")
print(f"p2: {sum(game_powers)}")
