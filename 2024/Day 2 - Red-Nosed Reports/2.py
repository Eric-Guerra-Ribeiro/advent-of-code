from pathlib import Path

import numpy as np

def read_input(path: Path) -> list[np.ndarray]:
    with open(path) as file:
        lines = file.readlines()
        return [np.array(line.split(), dtype=int) for line in lines]


def is_safe(level: np.ndarray) -> bool:
    if len(level) <=1 :
        return True
    diff = level[1:] - level[:-1]
    abs_diff = np.abs(diff)
    # Safe level must differ by at most 3
    if np.max(abs_diff) > 3:
        return False
    # Safe level must differ by at least 1
    if np.min(abs_diff) < 1:
        return False
    # Safe level must be increasing or decreasing
    num_increasing = np.sum(diff > 0)
    if num_increasing == 0 or num_increasing == len(diff):
        return True
    return False


def solve_part1(input: list[np.ndarray]) -> int:
    safe = sum(is_safe(level) for level in input)
    return safe


def is_dampened_safe(level: np.ndarray) -> bool:
    for i in range(len(level)):
        if is_safe(np.delete(level, i)):
            return True
    return False


def solve_part2(input: list[int]) ->int:
    safe = sum(is_dampened_safe(level) for level in input)
    return safe


if __name__ == "__main__":
    folder_path = Path("./2024/Day 2 - Red-Nosed Reports")
    # Solving Example
    example_path = folder_path / "example.txt"
    example = read_input(example_path)
    assert solve_part1(example) == 2
    assert solve_part2(example) == 4
    # Solving
    input_path = folder_path / "input.txt"
    input = read_input(input_path)
    # Part 1
    sol1 = solve_part1(input)
    print(f"Solution Part 1: {sol1}")
    # Part 2
    sol2 = solve_part2(input)
    print(f"Solution Part 2: {sol2}")
