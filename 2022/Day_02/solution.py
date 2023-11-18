# Solution for Day 2

INPUT_PATH = "./2022/Day_02/input.txt"

vals = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

res_vals = {"X": 0, "Y": 3, "Z": 6}


def result_score(foe, me) -> int:
    foe_num = vals[foe]
    me_num = vals[me]

    if foe_num == me_num:
        return 3

    match (foe_num):
        case 1:
            return 6 if me_num - foe_num == 1 else 0
        case 2:
            return 6 if me_num - foe_num == 1 else 0
        case 3:
            return 6 if me_num - foe_num == -2 else 0
    raise ValueError(f"Invalid entry: {foe}, {me}")


# given an outcome and foe, pick what i need to play
def inst_score(foe, res) -> int:
    foe_num = vals[foe]

    match (res):
        # tie
        case "Y":
            return foe_num
        # loss
        case "X":
            if foe_num == 1:
                return 3
            elif foe_num == 2:
                return 1
            else:
                return 2
        # Win
        case "Z":
            if foe_num == 1:
                return 2
            elif foe_num == 2:
                return 3
            else:
                return 1

    raise ValueError(f"Invalid entry: {foe}, {res}")


with open(INPUT_PATH) as file:
    lines = file.read().split("\n")


turns = [i.split(" ") for i in lines]


# final = resultscore + vals[me]
scores = [result_score(turn[0], turn[1]) + vals[turn[1]] for turn in turns]

# new codex
new_scores = [inst_score(turn[0], turn[1]) + res_vals[turn[1]] for turn in turns]

# total
print(new_scores[0:5])
print(turns[0:5])
print(sum(scores))
print(sum(new_scores))
