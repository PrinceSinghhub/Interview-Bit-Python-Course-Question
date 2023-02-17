def main():
    num = int(input())

    if num >= 90:
        print("A")
    elif num < 90 and num >= 80:
        print("B")

    elif num < 80 and num >= 70:
        print("C")
    elif num < 70 and num >= 60:
        print("D")
    elif num < 60 and num >= 50:
        print("E")
    else:
        print("F")


if __name__ == '__main__':
    main()