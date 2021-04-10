def reverse(x: int) -> int:
    if x == 0:
        return 0
    x = [int(i) if i != '-' else i for i in str(x)]
    if x[0] == '-':
        negative_integer = True
        x.remove('-')
    else:
        negative_integer = False

    new_x = ''.join([str(item) for item in x[::-1]])
    new_x = new_x.lstrip('0')
    if negative_integer:
        new_x = -abs(int(new_x))
    else:
        new_x = abs(int(new_x))
    if not abs(new_x) <= 0x7FFFFFFF:
        return 0
    return new_x

reversed_integer = reverse(1563847412)

print(reversed_integer)