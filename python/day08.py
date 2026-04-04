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


def compute2(lines: list[str]) -> int:
    out = 0
    for line in lines:
        len_line = len(line)
        len_code = 0
        for c in line:
            match c:
                case '"':
                    len_code += 2
                case '\\':
                    len_code += 2
                case _:
                    len_code += 1
        len_code += 2
        out += len_code - len_line
    return out


if __name__ == '__main__':
    text = load_lines()
    print(compute(text))
    print(compute2(text))
