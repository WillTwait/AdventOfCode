# Solution for Day 3

INPUT_PATH = "./2023/Day_03/input.txt"

with open(INPUT_PATH) as file:
    lines = file.read().split("\n")

mapped_lines = []
buffer = []
for line in lines:
    # add l/r buffers
    line = "." + line + "."
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
gear_ratios = []
touched_gears = {}
gear_ratio_sum = 0
# iterate through non-buffered region
for row_number, row in enumerate(mapped_lines[1:-1]):
    # account for offset
    row_number += 1
    is_valid = False
    current_number = ""
    touched_gears_for_number = set()

    # ignore l/r buffers
    for char_number, char in enumerate(row[1:-1]):
        char_number += 1
        if char.isdigit():
            current_number += char

            # check if valid above
            row_above = mapped_lines[row_number - 1]
            for col, char in enumerate(row_above[char_number - 1 : char_number + 2]):
                absolute_row = row_number - 2
                absolute_col = col + char_number - 1
                coord = (absolute_row, absolute_col)
                if not char.isdigit() and char != ".":
                    if char == "*":
                        print(
                            f"char at: {(absolute_row, absolute_col)} for {current_number}, appending in above"
                        )
                        touched_gears_for_number.add(coord)
                    is_valid = True

            # check if valid below
            row_below = mapped_lines[row_number + 1]
            for col, char in enumerate(row_below[char_number - 1 : char_number + 2]):
                absolute_row = row_number
                absolute_col = col + char_number - 1
                coord = (absolute_row, absolute_col)
                if not char.isdigit() and char != ".":
                    if char == "*":
                        print(
                            f"char at: {(absolute_row, absolute_col)} for {current_number}, appending in below"
                        )
                        # append if not there
                        touched_gears_for_number.add(coord)

                    is_valid = True

            # check if valid current
            row_current = mapped_lines[row_number]
            left_right = [
                row_current[char_number - 1],
                row_current[char_number + 1],
            ]

            # TODO: split left and right?
            # check left
            for col, char in enumerate(left_right):
                # TODO: this is wrong
                absolute_row = row_number - 1
                absolute_col = col + char_number + col
                coord = (absolute_row, absolute_col)
                if not char.isdigit() and char != ".":
                    if char == "*":
                        print(
                            f"char at: {(absolute_row, absolute_col)} for {current_number}, appending in same"
                        )
                        touched_gears_for_number.add(coord)
                    is_valid = True
        else:
            if len(current_number) > 0:
                if is_valid:
                    print(f"touched: {touched_gears_for_number} for {current_number}")
                    part_numbers.append(int(current_number))
                    for coord in touched_gears_for_number:
                        # if exists, add the gear
                        if coord in touched_gears:
                            touched_gears[coord].append(int(current_number))
                        # if not exist, create row
                        else:
                            touched_gears[coord] = [int(current_number)]
            current_number = ""
            touched_gears_for_number = set()
            is_valid = False

    # add on any end of rows
    if len(current_number) > 0 and is_valid:
        part_numbers.append(int(current_number))

        print(f"touched: {touched_gears_for_number} for {current_number}")

        for coord in touched_gears_for_number:
            # if exists, add the gear
            if coord in touched_gears:
                touched_gears[coord].append(int(current_number))
            # if not exist, create row
            else:
                touched_gears[coord] = [int(current_number)]

for key, value in touched_gears.items():
    if len(value) == 2:
        print(f"legit gear: {key}: {value}")
        gear_ratio_sum += value[0] * value[1]

print(sum(part_numbers))
print(touched_gears)
print(gear_ratio_sum)
