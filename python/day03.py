from pathlib import Path


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


def main():
    coordinates = visited_homes(read_moves())
    print(len(coordinates))


if __name__ == '__main__':
    main()
