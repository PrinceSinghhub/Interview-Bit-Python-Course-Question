import re
def main():
    N = int(input())
    for _ in range(N):
        if(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",input())):
            print('YES')
        else:
            print('NO')
            
    return 0

if __name__ == '__main__':
    main()