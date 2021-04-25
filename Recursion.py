n = int(input())
elem_was_used = list()


def choice():
    global n, elem_was_used
    if len(elem_was_used) != n:
        for i in range(1, n + 1):
            if not i in elem_was_used:
                elem_was_used.append(i)
                choice()
    else:
        for number in elem_was_used:
            print(number, end=' ')
        print()
    if elem_was_used != []:
        del elem_was_used[-1]


choice()
