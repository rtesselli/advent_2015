from pathlib import Path
from more_itertools import chunked


def read_moves():
    return Path('../data/day03.txt').read_text()


def displacement(move: str) -> tuple[int, int]:
    match move:
        case '^':
            return 0, 1
        case 'v':
            return 0, -1
        case '>':
            return 1, 0
        case '<':
            return -1, 0


def add(pair1: tuple[int, int], pair2: tuple[int, int]) -> tuple[int, int]:
    x1, y1 = pair1
    x2, y2 = pair2
    return x1 + x2, y1 + y2


def visited_homes(moves: str) -> set[tuple[int, int]]:
    x, y = 0, 0
    visited = {(x, y)}
    for move in moves:
        x, y = add((x, y), displacement(move))
        visited.add((x, y))
    return visited


def visited_homes2(moves: str) -> set[tuple[int, int]]:
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    visited = {(x1, y1)}
    for first, second in chunked(moves, 2):
        (x1, y1) = add((x1, y1), displacement(first))
        visited.add((x1, y1))
        (x2, y2) = add((x2, y2), displacement(second))
        visited.add((x2, y2))
    return visited


def main():
    moves = read_moves()
    print(len(visited_homes(moves)))
    print(len(visited_homes2(moves)))


if __name__ == '__main__':
    main()
