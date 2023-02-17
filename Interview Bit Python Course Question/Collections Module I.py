from collections import Counter

def main():
    N = int(input())
    d = Counter(map(int, input().split()))
    M = int(input())
    ans = 0
    for i in range(M):
        xi, typ = map(int, input().split())
        if typ in d and d[typ] > 0:
            ans += xi
            d[typ] -= 1
    print(ans)
    return 0

if __name__ == '__main__':
    main()