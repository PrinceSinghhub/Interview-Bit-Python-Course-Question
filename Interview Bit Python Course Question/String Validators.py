def main():
    S = input()
    check = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    ans = 1
    for i in S:
        if i in check:
            ans = 0
            print(True)
            break


    if ans == 1:
        print(False)



    ans1 = 1
    for i in S:
        if i.isalpha():
            print(True)
            ans1 = 0
            break
    if ans1 == 1:
        print(False)

    ans3 = 1
    for i in S:
        if i.isdigit():
            print(True)
            ans3 = 0
            break
    if ans3 == 1:
        print(False)

    ans4 = 1
    for i in S:
        if i.islower():
            print(True)
            ans4 = 0
            break
    if ans4 == 1:
        print(False)

    ans5 = 1
    for i in S:
        if i.isupper():
            print(True)
            ans5 = 0
            break
    if ans5 == 1:
        print(False)

if __name__ == '__main__':
    main()