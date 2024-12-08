from pathlib import Path
from typing import Callable

import numpy as np

class Map:

    def __init__(self, map:list[str], part:int) -> None:
        self.map = map
        self.antenna_dict = dict()

        self.num_rows = len(map)
        self.num_columns = len(map[0])

        for i, row in enumerate(map):
            for j, char in enumerate(row):
                if char == "." or char == "#":
                    continue
                if char in self.antenna_dict:
                    self.antenna_dict[char].append((i, j))
                else:
                    self.antenna_dict[char] = [(i, j)]

        if part == 1:
            self.antinodes = self.calc_antinodes(self.antinode_positions1)
        elif part == 2:
            self.antinodes = self.calc_antinodes(self.antinode_positions2)

    def calc_antinodes(self, antinode_generator:Callable) -> set[tuple[int, int]]:
        antinodes = {
            pos
            for positions in self.antenna_dict.values()
            for i in range(len(positions) - 1)
            for j in range(i + 1, len(positions))
            for pos in antinode_generator(positions[i], positions[j])
        }
        return antinodes

    def antinode_positions1(self, pos1:tuple[int, int], pos2:tuple[int, int]) -> set[tuple[int, int]]:
        return {
            pos
            for pos in [(2*pos1[0] - pos2[0], 2*pos1[1] - pos2[1]), (2*pos2[0] - pos1[0], 2*pos2[1] - pos1[1])]
            if self.pos_is_valid(pos)
        }

    def antinode_positions2(self, pos1:tuple[int, int], pos2:tuple[int, int]) -> set[tuple[int, int]]:
        delta_row = pos1[0] - pos2[0]
        delta_column = pos1[1] - pos2[1]
        positions = set()

        k = 1
        while (0 <= pos1[0] + k*delta_row < self.num_rows) and (0 <= pos1[1] + k*delta_column < self.num_columns):
            positions.add((pos1[0] + k*delta_row, pos1[1] + k*delta_column))
            k += 1
        
        k = 0
        while (0 <= pos1[0] + k*delta_row < self.num_rows) and (0 <= pos1[1] + k*delta_column < self.num_columns):
            positions.add((pos1[0] + k*delta_row, pos1[1] + k*delta_column))
            k -= 1
        
        return positions


    def pos_is_valid(self, pos:tuple[int, int]) -> bool:
        if (0 <= pos[0] < self.num_rows) and (0 <= pos[1] < self.num_columns):
            return True
        return False

    def get_num_antinodes(self) -> int:
        return len(self.antinodes)


def read_input(path: Path) -> list[str]:
    with open(path) as file:
        return file.read().splitlines()


def solve_part1(input: list[str]) -> int:
    city_map = Map(input, 1)
    return city_map.get_num_antinodes()



def solve_part2(input: list[str]) -> int:
    city_map = Map(input, 2)
    return city_map.get_num_antinodes()


if __name__ == "__main__":
    folder_path = Path("./2024/Day 8 - Resonant Collinearity")
    # Solving Example
    example_path = folder_path / "example.txt"
    example = read_input(example_path)
    assert solve_part1(example) == 14
    assert solve_part2(example) == 34
    # Solving
    input_path = folder_path / "input.txt"
    input = read_input(input_path)
    # Part 1
    sol1 = solve_part1(input)
    print(f"Solution Part 1: {sol1}")
    # Part 2
    sol2 = solve_part2(input)
    print(f"Solution Part 2: {sol2}")
