from pathlib import Path
import re

import numpy as np

match_int = re.compile(r"\d+")

def read_input(path: Path) -> list[dict[str:tuple[int,int]]]:
    machines = []
    with open(path) as file:
        button_a_str = file.readline()
        button_b_str = file.readline()
        prize_str = file.readline()

        machine = {}
        machine["A"] = tuple(int(num.group(0)) for num in match_int.finditer(button_a_str))
        machine["B"] = tuple(int(num.group(0)) for num in match_int.finditer(button_b_str))
        machine["Prize"] = tuple(int(num.group(0)) for num in match_int.finditer(prize_str))

        machines.append(machine)
        while file.readline():
            button_a_str = file.readline()
            button_b_str = file.readline()
            prize_str = file.readline()

            machine = {}
            machine["A"] = tuple(int(num.group(0)) for num in match_int.finditer(button_a_str))
            machine["B"] = tuple(int(num.group(0)) for num in match_int.finditer(button_b_str))
            machine["Prize"] = tuple(int(num.group(0)) for num in match_int.finditer(prize_str))

            machines.append(machine)
    return machines

def cost_tokens(move_a:tuple[int,int], move_b:tuple[int,int], prize_position:tuple[int,int]) -> int:
    # Return -1 : Impossible
    x_a, y_a = move_a
    x_b, y_b = move_b
    x_prize, y_prize = prize_position
    # Consistent and Determinate System
    if x_a*y_b - x_b*y_a != 0:
        tickets_b = (x_a*y_prize - y_a*x_prize)//(x_a*y_b - x_b*y_a)
        tickets_a = (x_prize - x_b*tickets_b)//x_a
        # Solution is not positive
        if tickets_a < 0 or tickets_b < 0:
            return -1
        # Solution is not an integer
        if (x_a*tickets_a + x_b*tickets_b != x_prize
           or y_a*tickets_a + y_b*tickets_b != y_prize):
            return -1
    # Consitent and Indeterminate System
    elif x_a*y_prize - y_a*x_prize == 0:
        raise NotImplementedError()
    # Inconsistent System
    else:
        return -1
    return 3*tickets_a + tickets_b

def solve_part1(input: list[dict[str:tuple[int,int]]]) -> int:
    sol = 0
    for machine in input:
        cost = cost_tokens(machine["A"], machine["B"], machine["Prize"])
        sol += cost if cost > 0 else 0
    return sol


def solve_part2(input: list[dict[str:tuple[int,int]]]) -> int:
    sol = 0
    offset = 10000000000000
    for machine in input:
        machine["Prize"] = tuple(val + offset for val in machine["Prize"])
        cost = cost_tokens(machine["A"], machine["B"], machine["Prize"])
        sol += cost if cost > 0 else 0
    return sol


if __name__ == "__main__":
    folder_path = Path("./2024/Day 13 - Claw Contraption")
    # Solving Example
    example_path = folder_path / "example.txt"
    example = read_input(example_path)
    assert solve_part1(example) == 480
    # Solving
    input_path = folder_path / "input.txt"
    input = read_input(input_path)
    # Part 1
    sol1 = solve_part1(input)
    print(f"Solution Part 1: {sol1}")
    # Part 2
    sol2 = solve_part2(input)
    print(f"Solution Part 2: {sol2}")
