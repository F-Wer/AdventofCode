from advent_of_code.util import open_file, get_File

def getFirst():
    content = open_file('3.txt', mode = "strings")
    return content
#
# def getSecond():


if __name__ == "__main__":
    # cookie = input('Enter your cookie: ')
    # day = input('Enter the day: ')
    # get_File('https://adventofcode.com/2021/day/' + day + '/input', cookie, day)
    print(__file__)
    print(getFirst())
    # print(__file__)
    # print(getSecond())