from pathlib import Path
import re

import numpy as np


mul_re = re.compile(r"mul\(\d+,\d+\)")

mul_or_do_dont_re = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")


def multiply(mul: str) -> int:
    stripped_mul = mul.strip("mul()")
    list_nums = stripped_mul.split(",")
    return int(list_nums[0])*int(list_nums[1])


def read_input(path: Path) -> list[str]:
    with open(path) as file:
        return file.readlines()


def solve_part1(input: list[str]) -> int:
    sol = 0
    for string in input:
        list_mul = mul_re.findall(string)
        for mul in list_mul:
            sol += multiply(mul)
    return sol


def solve_part2(input: list[str]) -> int:
    sol = 0
    isActive = True
    for string in input:
        list_command = mul_or_do_dont_re.findall(string)
        for command in list_command:
            if command == "do()":
                isActive = True
            elif command == "don't()":
                isActive = False
            elif isActive:
                sol += multiply(command)
    return sol


if __name__ == "__main__":
    folder_path = Path("./2024/Day 3 - Mull it Over")
    # Solving Example
    example1_path = folder_path / "example1.txt"
    example1 = read_input(example1_path)
    assert solve_part1(example1) == 161
    example2_path = folder_path / "example2.txt"
    example2 = read_input(example2_path)
    assert solve_part2(example2) == 48
    # Solving
    input_path = folder_path / "input.txt"
    input = read_input(input_path)
    # Part 1
    sol1 = solve_part1(input)
    print(f"Solution Part 1: {sol1}")
    # Part 2
    sol2 = solve_part2(input)
    print(f"Solution Part 2: {sol2}")
