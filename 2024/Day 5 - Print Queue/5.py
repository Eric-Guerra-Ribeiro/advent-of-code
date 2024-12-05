from pathlib import Path

import numpy as np

def read_input(path: Path) -> tuple[dict[int : int],  list[np.ndarray]]:

    order_rules = dict()
    list_pages_to_produce = []

    reading_rules = True

    with open(path) as file:
        for line in file.readlines():
            if line == "\n":
                reading_rules = False
            elif reading_rules:
                split_line = line.split("|")
                num_before = int(split_line[0])
                num_after = int(split_line[1])
                if num_before in order_rules:
                    order_rules[num_before].add(num_after)
                else:
                    order_rules[num_before] = {num_after}
            else:
                list_pages_to_produce.append(np.array(line.split(","), dtype=int))
    return order_rules, list_pages_to_produce


def is_ordered(order_rules: dict[int : int], pages: np.ndarray) -> bool:
    for i in range(1, pages.size):
        for j in range(i):
            if pages[i] in order_rules and pages[j] in order_rules[pages[i]]:
                return False
    return True


def solve_part1(input_rules:dict[int : int], input_pages:list[np.ndarray]) -> int:
    sol = 0
    for pages in input_pages:
        if is_ordered(input_rules, pages):
            sol += pages[pages.size//2]
    return sol


def order_pages(order_rules: dict[int : int], pages: np.ndarray) -> np.ndarray:
    nums = {page for page in pages}
    specific_rules = {num : order_rules[num] & nums for num in nums if num in order_rules}
    depedencies_count = {num : 0 for num in nums}
    for _, vals in specific_rules.items():
        for val in vals:
            depedencies_count[val] += 1
    ordered_pages = np.zeros_like(pages)
    for i in range(ordered_pages.size):
        for num, count in depedencies_count.items():
            if count != 0:
                continue
            ordered_pages[i] = num
            if num in order_rules:
                for dependecy in order_rules[num]:
                    if dependecy in depedencies_count:
                        depedencies_count[dependecy] -= 1
            del depedencies_count[num]
            break

    return ordered_pages



def solve_part2(input_rules:dict[int : int], input_pages:list[np.ndarray]) -> int:
    sol = 0
    for pages in input_pages:
        if not is_ordered(input_rules, pages):
            ordered_pages = order_pages(input_rules, pages)
            sol += ordered_pages[len(ordered_pages)//2]
    return sol


if __name__ == "__main__":
    folder_path = Path("./2024/Day 5 - Print Queue")
    # Solving Example
    example_path = folder_path / "example.txt"
    example = read_input(example_path)
    assert solve_part1(*example) == 143
    assert solve_part2(*example) == 123
    # Solving
    input_path = folder_path / "input.txt"
    input = read_input(input_path)
    # Part 1
    sol1 = solve_part1(*input)
    print(f"Solution Part 1: {sol1}")
    # Part 2
    sol2 = solve_part2(*input)
    print(f"Solution Part 2: {sol2}")
