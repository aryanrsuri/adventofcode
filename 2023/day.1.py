import re
from typing import Any


def day1(input: str = "./input/day.1.input") -> int:
    ans: int = 0
    with open(input, "r") as f:
        for line in f.read().splitlines():
            digs = [c for c in line if c.isdigit()]
            ans += (int(digs[0] + digs[-1]))
    return ans


def day2(input: str = "./input/day.1.input") -> int:
    ans: int = 0
    digits: str = r"(?=(one|two|three|four|five|six|seven|eight|\d|nine))"
    map: dict[str, str] = {"one": "1", "two": "2", "three": "3", "four": "4",
                           "five": "5", "six": "6", "seven": "7", "eight": "8",
                           "nine": "9"}
    with open(input, "r") as f:
        for line in f.read().splitlines():
            digs: list[Any] = re.findall(digits, line)
            digs = [digs[0], digs[-1]]
            for i, d in enumerate(digs):
                if d in map:
                    digs[i] = map[d]
            ans += (int(digs[0] + digs[-1]))
    return ans


print(day1())
print(day2())
