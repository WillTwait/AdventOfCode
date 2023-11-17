# Solution for Day 1

with open("./2022/Day_01/input.txt") as file:
    lines = file.read()

elf_list = lines.split("\n\n")

sums = []
for elf in elf_list:
    nums = [int(i) for i in elf.split("\n")]
    sums.append(sum(nums))

# max elf
print(max(sums))

# top 3 elves
sums.sort(reverse=True)
print(sum(sums[0:3]))
