from pathlib import Path
from collections import Counter


def count_parentheses(content: str) -> int:
    counts = Counter(content)
    return counts['('] - counts[')']


def main():
    content = Path('../data/day01.txt').read_text()
    print(count_parentheses(content))


if __name__ == '__main__':
    main()
