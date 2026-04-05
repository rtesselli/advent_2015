from itertools import groupby


def iterate(n: int) -> int:
    n = str(n)
    for _ in range(40):
        new_n = []
        for k, group in groupby(n):
            counts = len(list(group))
            new_n.append(str(counts))
            new_n.append(k)
        n = "".join(new_n)
    return len(n)


if __name__ == '__main__':
    print(iterate(1321131112))
