def main():
    str_list = ['given', 'intern', 'InterviewBit', 'network', 'local', 'multiple', 'define', 'nodes', 'algorithm',
                'allows', 'community', 'phase', 'single']
    my_list = []

    for i in str_list:
        if len(i) % 2 != 0:
            my_list.append(i)

    print(my_list)


if __name__ == '__main__':
    main()