from advent_of_code.util import open_file, get_File

def getFirst():
    forward = 0
    horizontal = 0
    content = open_file('2.txt')
    for line in content:
        try:
            if 'forward' in line:
                splitf = line.split()
                forward += int(splitf[1])
                del splitf
            elif 'up' in line:
                splitu = line.split()
                horizontal -= int(splitu[1])
                del splitu
            else:
                splith = line.split()
                horizontal += int(splith[1])
                del splith
        except:
            print('ERROR')
    return forward * horizontal



def getSecond():
    aim = 0
    horizontal = 0
    depth = 0
    content = open_file('2.txt')
    for line in content:
        try:
            if 'forward' in line:
                splitf = line.split()
                horizontal += int(splitf[1])
                depth = ( int(splitf[1]) * aim ) + depth
                del splitf
            elif 'up' in line:
               splitu = line.split()
               aim -= int(splitu[1])
               del splitu
            elif 'down' in line:
                splith = line.split()
                aim += int(splith[1])
                del splith
        except:
            print('ERROR')
    return  horizontal , depth, aim


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
    result = getSecond()
    print(result)
    print(result[0] * result[1])



