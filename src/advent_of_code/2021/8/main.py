from advent_of_code.util import open_file, get_File

def getFirst(file):


def getSecond(file):


if __name__ == "__main__":
    cookie = input('Enter your cookie: ')
    day = input('Enter the day: ')
    get_File('https://adventofcode.com/2021/day/' + day + '/input', cookie, '2')
    print(getFirst())
    print(getSecond())