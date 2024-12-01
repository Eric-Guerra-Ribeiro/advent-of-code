from pathlib import Path

import numpy as np


def solve_part1(input: np.ndarray) -> int:
    lists = np.sort(input, axis=0)
    return np.sum(np.abs(lists[:, 0] - lists[:, 1]))


def solve_part2(input: np.ndarray) ->int:
    list1 = input[:, 0]
    list2 = input[:, 1]

    list2_frequency = dict()
    for element in list2:
        if element in list2_frequency:
            list2_frequency[element] += 1
        else:
            list2_frequency[element] = 1
    
    return sum(list2_frequency[element]*element for element in list1 if element in list2_frequency)


if __name__ == "__main__":
    folder_path = Path("./2024/Day 1 - Historian Hysteria")
    # Solving Example
    example_path = folder_path / "example.txt"
    example = np.loadtxt(example_path, dtype=int)
    assert solve_part1(example) == 11
    assert solve_part2(example) == 31
    # Solving
    input_path = folder_path / "input.txt"
    input = np.loadtxt(input_path, dtype=int)
    # Part 1
    sol1 = solve_part1(input)
    print(f"Solution Part 1: {sol1}")
    # Part 2
    sol2 = solve_part2(input)
    print(f"Solution Part 2: {sol2}")
