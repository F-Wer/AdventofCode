from advent_of_code.util import open_file, get_File

def getFirst():
    forward = 0
    horizontal = 0
    content = open_file('2.txt')
    for line in content:
        value = int(line.split()[1])
        try:
            if 'forward' in line:
                forward += value
            elif 'up' in line:
                horizontal -= value
            else:
                horizontal += value
        except:
            print('ERROR')
    return forward * horizontal



def getSecond():
    aim = 0
    horizontal = 0
    depth = 0
    content = open_file('2.txt')
    for line in content:
        value = int(line.split()[1])
        try:
            if 'forward' in line:
                horizontal += value
                depth = ( value * aim ) + depth
            elif 'up' in line:
               aim -= value
            elif 'down' in line:
                aim += value
        except:
            print('ERROR')
    return  horizontal * depth


def getRedditSolution():
#  nice solution with structural pattern matching
#  source: https://old.reddit.com/r/adventofcode/comments/r6zd93/2021_day_2_solutions/hmwbtbe/
    h = d = a = 0
    for x in open('2.txt'):
        match x.split():
            case 'forward', n:
                h += int(n)
                d += int(n) * a
            case 'up', n:
                a -= int(n)
            case 'down', n:
                a += int(n)

    print(h * a, h * d)


if __name__ == '__main__':
    cookie = input('Enter your cookie: ')
    get_File('https://adventofcode.com/2021/day/2/input', cookie, '2')
    print(getFirst())
    print(getSecond())



