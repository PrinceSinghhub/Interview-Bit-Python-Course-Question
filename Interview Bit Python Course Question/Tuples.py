def main():
    tuple1 = tuple(("one", "two", "three"))
    tuple2 = tuple(("1", "2", "3"))

    # change value at index 0 of both tuple to string "number"
    tuple1 = list(tuple1)
    tuple2 = list(tuple2)
    tuple1[0] = "number"

    tuple2[0] = "number"





    # Your code goes here

    print(tuple(tuple1))
    print(tuple(tuple2))

    return 0


if __name__ == '__main__':
    main()