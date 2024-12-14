from __future__ import annotations
from pathlib import Path

class Position:

    def __init__(self, i:int, j:int) -> None:
        self.i = i
        self.j = j

    def __add__(self, other_pos:Position) -> Position:
        return Position(self.i + other_pos.i, self.j + other_pos.j)

    def is_valid(self, num_rows:int, num_columns:int) -> bool:
        return 0 <= self.i < num_rows and 0 <= self.j < num_columns

    def get(self) -> tuple[int, int]:
        return self.i, self.j
    
    def access(self, matrix:list[list[int]]):
        return matrix[self.i][self.j]
    
    def __str__(self) -> str:
        return f"({self.i},{self.j})"

    def __repr__(self) -> str:
        return self.__str__()
    
    def __hash__(self) -> int:
        return str.__hash__(self.__str__())
    
    def __eq__(self, value) -> bool:
        return self.i == value.i and self.j == value.j


class HikeMap:

    def __init__(self, map: list[str]) -> None:
        self.hike_map = [[int(char) for char in row] for row in map]
        self.num_rows = len(map)
        self.num_columns = len(map[0])
    
    def get_zeros(self) -> list[Position]:
        return [Position(i, j) for i, row in enumerate(self.hike_map) for j, num in enumerate(row) if num == 0]

    def get_possible_neighbours(self, pos:Position) -> list[Position]:
        deltas = [Position(1, 0), Position(-1, 0), Position(0, 1), Position(0, -1)]
        return [
            new_pos
            for delta in deltas
            for new_pos in [pos + delta]
            if new_pos.is_valid(self.num_rows, self.num_columns)
               and new_pos.access(self.hike_map) - pos.access(self.hike_map) == 1
        ]
    
    def calc_trailhead_score(self, pos:Position, reached_nines:set[Position]) -> int:
        if pos.access(self.hike_map) == 9:
            if pos in reached_nines:
                return 0
            reached_nines.add(pos)
            return 1

        score = 0

        for children in self.get_possible_neighbours(pos):
            score += self.calc_trailhead_score(children, reached_nines)

        return score

    def calc_trailhead_rating(self, pos:Position) -> int:
        if pos.access(self.hike_map) == 9:
            return 1

        score = 0

        for children in self.get_possible_neighbours(pos):
            score += self.calc_trailhead_rating(children)

        return score



def read_input(path: Path) -> list[str]:
    with open(path) as file:
        return file.read().split()


def solve_part1(input: list[str]) -> int:
    hike_map = HikeMap(input)
    sol = 0
    for zero in hike_map.get_zeros():
        sol += hike_map.calc_trailhead_score(zero, set())
    return sol
    



def solve_part2(input: list[str]) -> int:
    hike_map = HikeMap(input)
    sol = 0
    for zero in hike_map.get_zeros():
        sol += hike_map.calc_trailhead_rating(zero)
    return sol


if __name__ == "__main__":
    folder_path = Path("./2024/Day 10 - Hoof It")
    # Solving Example
    example_path = folder_path / "example.txt"
    example = read_input(example_path)
    assert solve_part1(example) == 36
    assert solve_part2(example) == 81
    # Solving
    input_path = folder_path / "input.txt"
    input = read_input(input_path)
    # Part 1
    sol1 = solve_part1(input)
    print(f"Solution Part 1: {sol1}")
    # Part 2
    sol2 = solve_part2(input)
    print(f"Solution Part 2: {sol2}")
