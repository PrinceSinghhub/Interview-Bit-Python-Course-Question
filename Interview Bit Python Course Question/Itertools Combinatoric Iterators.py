from itertools import permutations

def main():
    S,K = input().split(" ")

    for i in permutations(sorted(S),int(K)):
        print("".join(i))
    return 0

if __name__ == '__main__':
    main()