import requests

def open_file(file):
    # Open txt file
    f = open(file)
    inp = [int(i) for i in f.read().splitlines()]
    return inp

def get_File(url, cookies, file):
    cookies = {'session' : cookies}
    r = requests.get(url, cookies=cookies)
    with open(file + '.txt', 'wb') as f:
        f.write(r.content)