from pathlib import Path
from dataclasses import dataclass
import numpy as np
import re


@dataclass
class Command:
    action: str
    start_coordinate: tuple[int, int]
    end_coordinate: tuple[int, int]


def load_commands() -> list[Command]:
    def parse(line: str) -> Command:
        command = ("turn on" if "on" in line else "turn off") if "turn" in line else "toggle"
        first, second = re.findall(r"\d*,\d*", line)
        start_x, start_y = [int(element) for element in first.split(",")]
        end_x, end_y = [int(element) for element in second.split(",")]
        return Command(command, (start_x, start_y), (end_x, end_y))

    lines = Path('../data/day06.txt').read_text().split("\n")
    return [
        parse(line)
        for line in lines
    ]


def transform(commands: list[Command]) -> np.ndarray:
    matrix = np.zeros((1000, 1000), dtype=bool)
    for command in commands:
        x_slice = slice(command.start_coordinate[0], command.end_coordinate[0] + 1)
        y_slice = slice(command.start_coordinate[1], command.end_coordinate[1] + 1)
        match command.action:
            case "turn off":
                matrix[x_slice, y_slice] = False
            case "turn on":
                matrix[x_slice, y_slice] = True
            case "toggle":
                matrix[x_slice, y_slice] = ~matrix[x_slice, y_slice]
    return matrix


if __name__ == '__main__':
    print(np.sum(transform(load_commands())))
