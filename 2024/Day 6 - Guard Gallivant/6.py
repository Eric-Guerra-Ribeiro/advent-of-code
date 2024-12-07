
from __future__ import annotations
from pathlib import Path
from enum import Enum

import numpy as np


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    @staticmethod
    def get_next(direction:Direction) -> Direction:
        return Direction((direction.value + 1) % len(Direction)) 


class Localization:

    def __init__(self, map:list[str]) -> None:
        self.map = map
        self.num_rows = len(map)
        self.num_columns = len(map[0])
        self.direction = Direction.UP
        self.obstacle_pos = None

        self.isInLoop = False

        for i, row in enumerate(map):
            for j, char in enumerate(row):
                if char == "^":
                    self.i = i
                    self.j = j
                    self.visited_places = {(i, j) : {self.direction}}
                    return


    def turn(self):
        self.direction = Direction.get_next(self.direction)

    def get_next_pos(self) -> tuple[int, int]:
        if self.direction == Direction.UP:
            return (self.i - 1, self.j)
        elif self.direction == Direction.RIGHT:
            return (self.i, self.j + 1)
        elif self.direction == Direction.DOWN:
            return (self.i + 1, self.j)
        elif self.direction == Direction.LEFT:
            return (self.i, self.j - 1)

    def pos_is_valid(self, pos:tuple[int, int]):
        if (0 <= pos[0] < self.num_rows) and (0 <= pos[1] < self.num_columns):
            return True
        return False

    def pos_is_obstacle(self, pos:tuple[int, int]):
        if not self.pos_is_valid(pos):
            return False
        return self.map[pos[0]][pos[1]] == "#" or self.obstacle_pos == pos

    def go_to_next(self) -> bool:
        next_pos = self.get_next_pos()
        if not self.pos_is_valid(next_pos):
            return False
        if self.pos_is_obstacle(next_pos):
            self.turn()
            return self.go_to_next()
        self.i, self.j = next_pos
        if next_pos in self.visited_places:
            if self.direction in self.visited_places[next_pos]:
                self.isInLoop = True
            else:
                self.visited_places[next_pos].add(self.direction)
        else:
            self.visited_places[next_pos] = {self.direction}
        return True

    def obstruct(self, pos: tuple[int, int]) -> None:
        self.obstacle_pos = pos



def read_input(path: Path) -> list[str]:
    with open(path) as file:
        return file.read().splitlines()


def solve_part1(input: list[str]) -> int:
    guard_localization = Localization(input)
    while guard_localization.go_to_next():
        pass
    return len(guard_localization.visited_places)


def solve_part2(input: list[str]) -> int:
    sol = 0
    guard_localization = Localization(input)
    while guard_localization.go_to_next():
        possible_positions = guard_localization.visited_places.keys()
    for pos in possible_positions:
        if input[pos[0]][pos[1]] == ".":
            guard_localization = Localization(input)
            guard_localization.obstruct(pos)
            while guard_localization.go_to_next():
                if guard_localization.isInLoop:
                    sol += 1
                    break
    return sol


if __name__ == "__main__":
    folder_path = Path("./2024/Day 6 - Guard Gallivant")
    # Solving Example
    example_path = folder_path / "example.txt"
    example = read_input(example_path)
    assert solve_part1(example) == 41
    assert solve_part2(example) == 6
    # Solving
    input_path = folder_path / "input.txt"
    input = read_input(input_path)
    # Part 1
    sol1 = solve_part1(input)
    print(f"Solution Part 1: {sol1}")
    # Part 2
    sol2 = solve_part2(input)
    print(f"Solution Part 2: {sol2}")
