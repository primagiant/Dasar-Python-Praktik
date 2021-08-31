def swap_case(s):
    hasil = ''
    for i in s:
        if i.islower():
            i = i.upper()
            hasil += i
        else:
            i = i.lower()
            hasil += i
    return hasil

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)