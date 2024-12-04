from pathlib import Path
import re

import numpy as np

xmas_re = re.compile(r"(?=(XMAS|SAMX))")
mas_re = re.compile(r"(?=(MAS|SAM))")

def read_input(path:Path) -> np.ndarray[str]:
    return np.loadtxt(path, dtype=str)


def vertical_words(horizontal_list:np.ndarray[str]) -> np.ndarray[str]:
    return [ "".join([horizontal_list[i][j] for i in range(horizontal_list.size)]) for j in range(len(horizontal_list[0]))]


def main_diag_words(horizontal_list:np.ndarray[str]) -> np.ndarray[str]:
    num_rows = horizontal_list.size
    num_columns = len(horizontal_list[0])
    return [ "".join([horizontal_list[n + dif][dif] for dif in range(max(0, -n), min(num_rows - n, num_columns))]) for n in range(1 - num_columns, num_rows)]


def anti_diag_words(horizontal_list:np.ndarray[str]) -> np.ndarray[str]:
    num_rows = horizontal_list.size
    num_columns = len(horizontal_list[0])
    return [ "".join([horizontal_list[i][n - i] for i in range(max(0, n - num_columns + 1), min(n + 1, num_rows))]) for n in range(num_rows + num_columns - 1)]


def solve_part1(input:np.ndarray[str]) -> int:
    sol = 0
    possible_lines_set = [input, vertical_words(input), anti_diag_words(input), main_diag_words(input)]
    for line_set in possible_lines_set:
        sol += sum(len(xmas_re.findall(line)) for line in line_set)
    return sol


def position_from_diag(index_in_diag_list:int, index:int, num_columns:int, isMain: bool) -> tuple[int, int]:
    if isMain:
        i = max(0, index_in_diag_list - num_columns + 1) + index
        j = i + num_columns - index_in_diag_list - 1
    else:
        i = max(0, index_in_diag_list - num_columns + 1) + index
        j = index_in_diag_list - i
    return (i, j)


def solve_part2(input:np.ndarray[str]) -> int:
    sol = 0
    num_colums = len(input[0])
    match_A_pos = set()
    for index, diag in enumerate(main_diag_words(input)):
        for match in mas_re.finditer(diag):
            match_A_pos.add(position_from_diag(index, match.start() + 1, num_colums, True))
    for index, diag in enumerate(anti_diag_words(input)):
        for match in mas_re.finditer(diag):
            if position_from_diag(index, match.start() + 1, num_colums, False) in match_A_pos:
                sol += 1
    return sol


if __name__ == "__main__":
    folder_path = Path("./2024/Day 4 - Ceres Search")
    # Solving Example
    example_path = folder_path / "example.txt"
    example = read_input(example_path)
    assert solve_part1(example) == 18
    assert solve_part2(example) == 9
    # Solving
    input_path = folder_path / "input.txt"
    input = read_input(input_path)
    # Part 1
    sol1 = solve_part1(input)
    print(f"Solution Part 1: {sol1}")
    # Part 2
    sol2 = solve_part2(input)
    print(f"Solution Part 2: {sol2}")
