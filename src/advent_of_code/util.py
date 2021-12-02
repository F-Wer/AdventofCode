import os
import shutil
from shutil import copyfile
import requests

def open_file(file, **mode):
    # Open txt file
    f = open(file)
    if mode == 'numbers':
        inp = [int(i) for i in f.read().splitlines()]
    else:
        inp = [i for i in f.read().splitlines()]
    return inp

def get_File(url, cookies, file):
    cookies = {'session' : cookies}
    r = requests.get(url, cookies=cookies)
    with open(file + '.txt', 'wb') as f:
        f.write(r.content)

def create_folders(year):
    current_dir = os.path.dirname((__file__))
    for i in range(1, 25):
        try:
            os.mkdir(os.path.dirname((__file__)) + '\\' + year + '\\' + str(i))
            shutil.copy('main.py', os.path.dirname((__file__)) + '\\' + year + '\\' + str(i))
            print('Created folder: ' + str(i))
        except OSError as error:
                print(error)
        shutil.copy(current_dir + '\\' + 'main.py', os.path.dirname((__file__)) + '\\' + year + '\\' + str(i))

if __name__ == '__main__':
    create_folders('2022')