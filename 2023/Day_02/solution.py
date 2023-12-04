# Solution for Day 2

INPUT_PATH = "./2023/Day_02/input.txt"

MAX_CONTENTS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

with open(INPUT_PATH) as file:
    lines = file.read().split("\n")

valid_games = []
for game in lines:
    parsed_round = game.split(": ", 1)
    game_number = int(parsed_round[0].split(" ")[1])

    draws = parsed_round[1].split("; ")
    DRAW_VALIDITY = []

    for draw in draws:
        if any(not value for value in DRAW_VALIDITY):
            break

        pulls = draw.split(", ")

        for pull in pulls:
            split_pull = pull.split(" ")
            pull_value = split_pull[0]
            pull_color = split_pull[1]

            if MAX_CONTENTS[pull_color] < int(pull_value):
                DRAW_VALIDITY.append(False)
                break

            DRAW_VALIDITY.append(True)

        # if any pull is invalid, this game number is invalid
    if all(value for value in DRAW_VALIDITY):
        valid_games.append(game_number)
print(sum(valid_games))
