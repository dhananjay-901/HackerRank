#ou are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
def swap_case(a):
    b = a.swapcase()
    return b

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)