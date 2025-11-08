# Solution for Day 2
INPUT_PATH = "./2024/Day_02/input.txt"

# safe: all inc or all dec
#   - i guess this means safe = true if report == report.sort() || report == report.sort()[::-1]

# AND
# safe: adj levels diff: 1 <= n <= 3


# S1
def solution_1(sol_lines: list[str]) -> int:
    safe_reports = 0

    def check_inc(line: list[int]) -> bool:
        sorted_line = sorted(line)

        return bool(line == sorted_line or line == sorted_line[::-1])

    def check_adj(current: int, next_val: int) -> bool:
        return bool(1 <= abs(current - next_val) <= 3)

    # turn each string of report row int array of levels
    # for each str input, convert it to num array, then run tests
    # sum the score for each string
    for line in sol_lines:
        report = [int(level) for level in line.split()]
        is_adj = True

        is_sloped = check_inc(report)

        for i in range(len(report) - 1):
            is_adj = check_adj(report[i], report[i + 1])
            if not is_adj:
                break

        is_safe = is_adj and is_sloped

        if is_safe:
            safe_reports += 1

    return safe_reports


# S2
def solution_2(sol_lines: list[str]) -> int:
    safe_reports = 0

    def check_inc(line: list[int]) -> bool:
        sorted_line = sorted(line)

        return bool(line == sorted_line or line == sorted_line[::-1])

    def check_adj(current: int, next_val: int) -> bool:
        return bool(1 <= abs(current - next_val) <= 3)

    # turn each string of report row int array of levels
    # for each str input, convert it to num array, then run tests
    # sum the score for each string
    for line in sol_lines:
        report = [int(level) for level in line.split()]
        is_adj = True

        is_sloped = check_inc(report)

        for i in range(len(report) - 1):
            is_adj = check_adj(report[i], report[i + 1])
            if not is_adj:
                break

        is_safe = is_adj and is_sloped

        if not is_safe:
            # try looping through removing one
            for i, _ in enumerate(report):
                new_report = report[:]
                del new_report[i]

                is_adj = True

                is_sloped = check_inc(new_report)

                for i in range(len(new_report) - 1):
                    is_adj = check_adj(new_report[i], new_report[i + 1])
                    if not is_adj:
                        break

                is_safe = is_adj and is_sloped

                if is_safe:
                    break

        if is_safe:
            safe_reports += 1

    return safe_reports


with open(INPUT_PATH) as file:
    lines = file.read().split("\n")

    print(f"p1: {solution_1(lines)}")
    print(f"p2: {solution_2(lines)}")
