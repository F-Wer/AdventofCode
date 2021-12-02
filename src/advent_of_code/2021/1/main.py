from advent_of_code.util import open_file, get_File

def getFirst():
    i = 0
    content = map(int,open_file('1.txt'))
    for line in content:
        try:
            if int(line) > int(val) and line:
                    i = i + 1
                    print('Value', line, 'is greater than', val)
            else:
                    print('Value', line, 'is less than', val)
        except:
            print('First',line)
        val = line
    return i

def getSecond():
    i = 0
    content = list(map(int,open_file('1.txt')))
    for line in range(3, len(content)):
        if(content[line] > content[line-3]):
            i += 1
    return i


if __name__ == '__main__':
    # cookie = input('Enter your cookie: ')
    # get_File('https://adventofcode.com/2021/day/1/input', cookie, '1')
    print(getFirst())
    print(getSecond())


