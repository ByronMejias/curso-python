def arg(num):
    return type(num)

print(arg('234.22'))


def arg(*num):
    return type(num)

print(arg(10, 20, 30))