import std/strutils
import std/sugar
import math

proc loadData(): seq[array[0..2, int]] =
  let rows = readFile("../data/day02.txt").strip.splitLines
  let sizes = collect(newSeq):
    for row in rows:
      let splitted = row.split("x")
      [parseInt(splitted[0]), parseInt(splitted[1]), parseInt(splitted[2])]
  return sizes

proc amountOfPaper(l: int, w: int, h: int): int =
  return 10


proc day02_part1(): int =
  let sizes = loadData()
  let amounts = collect(newSeq):
    for dimensions in sizes:
      amountOfPaper(dimensions[0], dimensions[1], dimensions[2])
  return sum(amounts)


when isMainModule:
  echo(day02_part1())