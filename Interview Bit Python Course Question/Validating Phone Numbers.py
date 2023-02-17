

import re
def main():
    for i in range(int(input())):
        if re.search(r"^[6789]\d{9}$",input()):
            print('YES')
        else:
            print('NO')
    return 0

if __name__ == '__main__':
    main()
