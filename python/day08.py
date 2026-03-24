from pathlib import Path


def load_lines():
    return Path("data/day08.txt").read_text().splitlines()


def compute(lines: list[str]) -> int:
    out = 0
    for line in lines:
        len_code = len(line)
        len_content = len(eval(line))
        out += len_code - len_content
    return out


if __name__ == '__main__':
    text = load_lines()
    print(compute(text))
