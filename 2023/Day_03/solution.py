# Solution for Day 3

INPUT_PATH = "./2023/Day_03/input.txt"

with open(INPUT_PATH) as file:
    lines = file.read().split("\n")

mapped_lines = []
buffer = []
for line in lines:
    # add l/r buffers
    line = "." + line + "."
    print(f"lr: {line}")
    buffer = ["." for _ in range(len(line))]

    row = []
    for char in line:
        row.append(char)
    mapped_lines.append(row)

# add top/bottom buffers
mapped_lines.insert(0, buffer)
mapped_lines.append(buffer)


print(mapped_lines)

part_numbers = []
no_ops = []
# iterate through non-buffered region
for row_number, row in enumerate(mapped_lines[1:-1]):
    # account for offset
    row_number += 1
    is_valid = False
    current_number = ""
    # ignore l/r buffers
    print(f"current: {row}")
    for char_number, char in enumerate(row[1:-1]):
        char_number += 1
        if char.isdigit():
            current_number += char
            print(f"appended: {current_number} with {is_valid}")

            # check if valid above
            if not is_valid:
                row_above = mapped_lines[row_number - 1]
                for char in row_above[char_number - 1 : char_number + 2]:
                    if not char.isdigit() and char != ".":
                        is_valid = True

            # check if valid below
            if not is_valid:
                row_below = mapped_lines[row_number + 1]
                print(f"row below: {row_below}")
                for char in row_below[char_number - 1 : char_number + 2]:
                    print(f"loc: {char_number}")
                    print(f"analizing: {row_below[char_number - 1 : char_number + 2]}")
                    print(f"char: {char}")
                    if not char.isdigit() and char != ".":
                        print(f"below true with: {char}")
                        is_valid = True

            # check if valid current
            if not is_valid:
                row_current = mapped_lines[row_number]
                left_right = [
                    row_current[char_number - 1],
                    row_current[char_number + 1],
                ]
                print(f"l/r: {left_right}")
                # check left
                for char in left_right:
                    if not char.isdigit() and char != ".":
                        is_valid = True
        else:
            print(f"no longer num with whole num: {current_number}")
            if len(current_number) > 0:
                if not is_valid:
                    no_ops.append(current_number)
                if is_valid:
                    print(f"valid appending: {current_number}")
                    part_numbers.append(int(current_number))
            current_number = ""
            is_valid = False

    # add on any end of rows
    if len(current_number) > 0 and is_valid:
        part_numbers.append(int(current_number))

print(part_numbers)
print(sum(part_numbers))
print(f"no_ops: {no_ops}")
