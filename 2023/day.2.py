import re
import math
from typing import NamedTuple, Optional


def day1(input: str) -> int:
    ans: int = 0
    allowed: dict[str, int] = {"red": 12, "blue": 14, "green": 13}
    with open(input, "r") as f:
        for line in f.read().splitlines():
            id, game = line.split(":")
            for n, color in re.findall(r"(\d+) (red|blue|green)", game):
                if int(n) > allowed[color]:
                    break
            else:
                ans += int(id.split()[1])
    return ans


def day2(input: str) -> int:
    ans: int = 0
    with open(input, "r") as f:
        for line in f.read().splitlines():
            allowed: dict[str, int] = {"red": 0, "blue": 0, "green": 0}
            _, game = line.split(":")
            for n, color in re.findall(r"(\d+) (red|blue|green)", game):
                allowed[color] = max(int(n), allowed[color])
            ans += math.prod(allowed.values())
    return ans


def main():
    print(day1("./input/day.2.input"))
    print(day2("./input/day.2.input"))


if __name__ == "__main__":
    main()
