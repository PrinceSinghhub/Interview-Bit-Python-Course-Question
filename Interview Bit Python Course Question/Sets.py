def main():
    my_set = set([1, 3, 2, 4, 1, 3, 3, 0])

    # add 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 to my_set

    add_data = [10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,23]
    for i in add_data:
        my_set.add(i)
    # delete 2 and 3 from my_set

    my_set.remove(2)
    my_set.remove(3)

    li = list(my_set)
    li.sort()

    print(li)


if __name__ == '__main__':
    main()