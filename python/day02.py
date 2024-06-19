from pathlib import Path


def load_data():
    content = Path('../data/day02.txt').read_text()
    lines = content.split('\n')
    return [
        [int(value) for value in line.split('x')]
        for line in lines
    ]


def amount_of_paper(length: int, width: int, height: int) -> int:
    sides = [
        length * width,
        width * height,
        height * length,
    ]
    return 2 * sum(sides) + min(sides)


def amount_of_ribbon(length: int, width: int, height: int) -> int:
    sides = [
        length + width,
        width + height,
        height + length,
    ]
    return 2 * min(sides) + length * width * height


def main():
    measures = load_data()
    print(sum(amount_of_paper(*measure) for measure in measures))
    print(sum(amount_of_ribbon(*measure) for measure in measures))


if __name__ == '__main__':
    main()
