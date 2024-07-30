from pathlib import Path
from more_itertools import chunked

def read_moves():
    return Path('../data/day03.txt').read_text()


def visited_homes(moves: str) -> set[tuple[int, int]]:
    x, y = 0, 0
    visited = {(x, y)}
    for move in moves:
        match move:
            case '^':
                y += 1
            case 'v':
                y -= 1
            case '>':
                x += 1
            case '<':
                x -= 1
        visited.add((x, y))
    return visited


def visited_homes2(moves: str) -> set[tuple[int, int]]:
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    visited = {(x1, y1)}
    for first, second in chunked(moves, 2):
        match first:
            case '^':
                y1 += 1
            case 'v':
                y1 -= 1
            case '>':
                x1 += 1
            case '<':
                x1 -= 1
        visited.add((x1, y1))
        match second:
            case '^':
                y2 += 1
            case 'v':
                y2 -= 1
            case '>':
                x2 += 1
            case '<':
                x2 -= 1
        visited.add((x2, y2))
    return visited


def main():
    moves = read_moves()
    coordinates = visited_homes(moves)
    print(len(coordinates))
    print(len(visited_homes2(moves)))


if __name__ == '__main__':
    main()
