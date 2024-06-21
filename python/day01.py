from pathlib import Path
from collections import Counter


def count_parentheses(content: str) -> int:
    counts = Counter(content)
    return counts['('] - counts[')']


def find_basement(content: str) -> int | None:
    floor = 0
    for index, parentheses in enumerate(content):
        if floor < 0:
            return index
        floor += 1 if parentheses == '(' else -1
    return None


def main():
    content = Path('../data/day01.txt').read_text()
    print(count_parentheses(content))
    print(find_basement(content))


if __name__ == '__main__':
    main()
