from pathlib import Path

import numpy as np

def read_input(path: Path) -> list[np.ndarray]:
    pass



def solve_part1(input: list[np.ndarray]) -> int:
    pass


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
