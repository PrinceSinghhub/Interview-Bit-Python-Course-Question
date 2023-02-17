def main():
    for i in range(int(input())):
        try:
            a,b = map(int, input().split())
            print (a//b)
        except ZeroDivisionError as e:
            print ('Error Code:',e)
        except ValueError as e:
            print ('Error Code:',e)
    return 0

if __name__ == '__main__':
    main()