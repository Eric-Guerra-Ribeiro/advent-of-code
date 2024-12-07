from pathlib import Path
from typing import Callable

import numpy as np

def read_input(path: Path) -> list[tuple[int,np.ndarray]]:
    with open(path) as file:
        return [
            (int(split_line[0]), np.fromiter((num for num in split_line[1].split()), dtype=int)) for line in file.readlines()
            for split_line in [line.split(":")]
        ]


def add_nums(a:int, b:int) -> int:
    return a + b


def mul_nums(a:int, b:int) -> int:
    return a * b


def there_are_operations(target:int, nums: np.ndarray, operations:list[Callable]) -> bool:
    partial_results = {nums[0]}
    for num in nums[1:]:
        partial_results = {operation(partial_result, num)  for partial_result in partial_results for operation in operations}
    return target in partial_results


def concatenate_nums(a:int, b:int) -> int:
    return a*10**(1 + int(np.log10(b))) + b


def solve_part1(input: list[np.ndarray]) -> int:
    sol = 0
    for target, nums in input:
        if there_are_operations(target, nums, [add_nums, mul_nums]):
            sol += target
    return sol


def solve_part2(input: list[int]) -> int:
    sol = 0
    for target, nums in input:
        if there_are_operations(target, nums, [add_nums, mul_nums, concatenate_nums]):
            sol += target
    return sol


if __name__ == "__main__":
    folder_path = Path("./2024/Day 7 - Bridge Repair")
    # Solving Example
    example_path = folder_path / "example.txt"
    example = read_input(example_path)
    assert solve_part1(example) == 3749
    assert solve_part2(example) == 11387
    # Solving
    input_path = folder_path / "input.txt"
    input = read_input(input_path)
    # Part 1
    sol1 = solve_part1(input)
    print(f"Solution Part 1: {sol1}")
    # Part 2
    sol2 = solve_part2(input)
    print(f"Solution Part 2: {sol2}")
