import std/tables
import std/strutils

proc day1_part1(): int =
  let content = readFile("../data/day01.txt").strip
  let frequencies = toCountTable(content)
  return frequencies['('] - frequencies[')']

proc day1_part2(): int =
  let content = readFile("../data/day01.txt").strip
  var floor = 0
  for i, elem in content:
    floor += (if elem == '(': 1 else: -1)
    if floor < 0:
      return i + 1


when isMainModule:
  echo(day1_part1())
  echo(day1_part2())
