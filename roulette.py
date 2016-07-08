from random import Random

RED = 0
BLACK = 1


def main():
    v2()


def v1():  # Check total amount of reds and blacks
    randomColorGenerator = Random()
    reds = 0
    blacks = 0
    money = 0
    for _ in range(100000):
        choice = RED if reds < blacks else BLACK
        randomColor = randomColorGenerator.randint(0, 1)
        if randomColor == RED:
            reds += 1
        else:
            blacks += 1
        money += 1 if randomColor == choice else -1

    print("Total money: {0}".format(money))


def v2():  # Only bet if last 4 colors were the same
    lastRandomColors = [2, 3, 4, 5]
    randomColorGenerator = Random()
    randomColorIndex = 0
    randomColor = -1
    hasBet = False
    money = 0

    for _ in range(100000):
        if v2_LastColorsAreTheSame(lastRandomColors):
            choice = (lastRandomColors[0] + 1) % 2
            hasBet = True

        print("{}".format("RED" if randomColor == RED else "BLACK"))
        randomColor = randomColorGenerator.randint(0, 1)
        lastRandomColors[randomColorIndex] = randomColor
        randomColorIndex = (randomColorIndex + 1) % 4

        if hasBet:
            print("++++++ BET")
            money += 1 if randomColor == choice else -1
            hasBet = False

    print("Total money: {0}".format(money))


def v2_LastColorsAreTheSame(lastRandomColors):
    if len(lastRandomColors) != 4:
        return False

    targetColor = lastRandomColors[0]
    for color in lastRandomColors:
        if targetColor != color:
            return False
    return True


if __name__ == "__main__":
    main()
