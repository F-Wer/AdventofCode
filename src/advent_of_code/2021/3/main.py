import collections
from advent_of_code.util import open_file, get_File
def getFirst():
    i = 0
    a = ""
    gamma = ""
    content = open_file('3.txt', mode = "strings")
    length = len(content[0])
    for n in range(length):
        while i < len(content):
            a += content[i][n]
            i += 1
        i = 0
        gamma += collections.Counter(a).most_common(1)[0][0]
        a = ""
    temp = int(gamma, 2)
    inverse = temp ^ (2 ** (len(gamma) + 1) - 1)
    epsilon = bin(inverse)[3 : ]
    return int(gamma,2) * int(epsilon,2)


def getSecond():
    i = 0
    a = ""
    b = ""
    c = ""
    content = open_file('3.txt', mode="strings")
    oxygen = content
    length = len(oxygen[0])
    for n in range(length):
        while i < len(oxygen):
            a += oxygen[i][n]
            i += 1
        i = 0
        b = collections.Counter(a)
        value0 = b.get("0")
        value1 = b.get("1")
        if value1 == value0:
            c += '1'
        else:
            c += b.most_common()[:1][0][0]
        oxygen = [x for x in oxygen if x[n] == (c[n])]
        a = ""
    if len(oxygen) == 1:
            print(oxygen[0])
            print(int(oxygen[0], 2))
            pass
    i2 = 0
    a2 = ""
    b2 = ""
    c2 = []
    content = open_file('3.txt', mode="strings")
    co2 = content
    length2 = len(co2[0])
    for n2 in range(length2):
            while i2 < len(co2):
                a2 += co2[i2][n2]
                i2 += 1
            i2 = 0
            b2 = collections.Counter(a2)
            value0 = b2.get('0')
            value1 = b2.get('1')
            if value1 == value0:
                c2 += '0'
            else:
                c2 += b2.most_common()[:-1 - 1:-1][0][0]
            co2 = [x for x in co2 if x[n2] == (c2[n2])]
            a2 = ""
    if len(co2) == 1:
                print(co2[0])
                print(int(co2[0],2))
                pass
    return int(oxygen[0],2) * int(co2[0],2)

if __name__ == "__main__":
    cookie = input('Enter your cookie: ')
    day = input('Enter the day: ')
    get_File('https://adventofcode.com/2021/day/' + day + '/input', cookie, day)
    print(getFirst())
    print(getSecond())