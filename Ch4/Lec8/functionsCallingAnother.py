def main():
    firstPart()
    print(str(4)+': from main')


def firstPart():
    print(str(1)+': from firstPart')
    secondPart()


def secondPart():
    print(str(2)+': from secondPart')
    thirdPart()


def thirdPart():
    print(str(3)+': from thirdPart')


main()
