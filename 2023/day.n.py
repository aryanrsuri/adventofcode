def day1(input: str) -> int:
    with open(input, "r") as f:
        for line in f.read().splitlines():
            print(line)
    return 0


def day2(input: str) -> int:
    with open(input, "r") as f:
        for line in f.read().splitlines():
            print(line)
    return 0


def main():
    day1("./input/day.1.input")
    day2("./input/day.1.input")


if __name__ == "__main__":
    main()
