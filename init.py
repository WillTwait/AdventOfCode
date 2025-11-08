import os


def create_advent_of_code_repo(year):
    repo_name = f"{year}"
    os.makedirs(repo_name, exist_ok=True)

    # Create daily challenge folders
    for day in range(1, 26):
        day_folder = os.path.join(repo_name, f"Day_{day:02}")
        os.makedirs(day_folder, exist_ok=True)

        # Add a README file for each day
        with open(os.path.join(day_folder, "README.md"), "w") as day_readme:
            day_readme.write(f"# Day {day}\n\n")

        # Add a solution file placeholder
        with open(os.path.join(day_folder, "solution.py"), "w") as solution:
            solution.write(f"# Solution for Day {day}\n")

        # Add a solution file placeholder
        with open(os.path.join(day_folder, "input.txt"), "w") as solution:
            pass

        # Add a test file placeholder
        with open(os.path.join(day_folder, "input.test.txt"), "w") as solution:
            pass

    # Create a utils folder if needed
    os.makedirs(os.path.join(repo_name, "utils"), exist_ok=True)

    print(f"Repository structure for Advent of Code {year} created successfully!")


create_advent_of_code_repo(2024)
