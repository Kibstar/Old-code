import os, string, random

URL = 'https://fake.py/'
folderLoc = r'c:\Users\jackk\PycharmProjects\SmallProjects\URL Shortener\\'
if os.path.isfile('site data.txt') == False:
    open('site data.txt', 'w+')


with open('site data.txt', 'r') as f:
    data = f.readlines()
    f.close()

def shortLink():
    path = ''
    pool = string.ascii_letters + '1234567890'
    for i in range(6):
        path += random.choice(pool)
    return path

def extractData(data):
    shortlist = []
    longlist = []
    for i in data:
        for j in range(len(i.split())):
            items = i.split()
            if j == 0:
                shortlist.append(items[0])
            elif j == 2:
                longlist.append(items[2])
    return shortlist, longlist


def checkAvailableLong(long, dict):
    for i in dict.keys():
        if i == long:
            return False
    return True

def checkAvailableShort(short, dict):
    for i in dict.values():
        if i == short:
            return False
    return True

def storingData(short,long):
    with open('site data.txt', 'a') as f:
        f.write(f'{short} | {long}\n')

shortlist, longlist = extractData(data)
dictionary = dict(zip(longlist, shortlist))

while True:
    userLink = input('Input the link you need shortening')
    if checkAvailableLong(userLink,dictionary):
        generatedLink = shortLink()
        while checkAvailableShort(generatedLink,dictionary) == False:
            print('generated new link')
            generatedLink = shortLink()

        storingData(generatedLink,userLink)
        print(f'Thank you, here is your shortened link: {URL+generatedLink}')
    else:
        storedLink = dictionary[userLink]
        print(f'This link has already been shortened. Here is the link: {URL+storedLink}')

