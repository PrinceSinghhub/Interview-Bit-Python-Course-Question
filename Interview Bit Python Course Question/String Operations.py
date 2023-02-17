def main():
    S = input()

    # Print length of the string S
    print(len(S))

    # Print the first occurence of the letter 'a' in S
    for i in S:
        if i == 'a':
            print(S.index(i))
            break
    # Note it is guaranteed that letter a is present in the string S

    # Print all the characters with even index in S
    ans = ""
    for i in range(len(S)):
        if i % 2 == 0:
            ans += S[i]
    print(ans)


if __name__ == '__main__':
    main()

