import requests


def getFile(url, cookies):
    cookies = {'session' : cookies}
    r = requests.get(url, cookies=cookies)
    with open('1.txt', 'wb') as f:
        f.write(r.content)

def open_file(file):
    # Open txt file
    f = open('1.txt')
    inp = [int(i) for i in f.read().splitlines()]
    return inp

def iterateFile():
    i = 0
    content = open_file('1.txt')
    for line in content:
        try:
            if line > val and line:
                    i = i + 1
                    print('Value', line, 'is greater than', val)
            else:
                    print('Value', line, 'is less than', val)
        except:
            print('First',line)
        val = line
    return i


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # cookie = input('Enter your cookie: ')
    # getFile('https://adventofcode.com/2021/day/1/input', cookie)
    print(iterateFile())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
