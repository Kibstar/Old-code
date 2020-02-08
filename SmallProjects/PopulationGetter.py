import os, requests, bs4, re, sys
countryList = ('Kenya').split()

folderPath = r'C:\Users\jackk\Documents\Python Things\Country population finder'
if os.path.isdir(folderPath) == False:
    os.mkdir(folderPath)

def linkMaker(country):
    populationURL = 'https://www.worldometers.info/world-population/'
    return populationURL + country + '-population/'

def populationFinder(url):
    res = requests.get(url)
    res.raise_for_status()
    popSoup = bs4.BeautifulSoup(res.text,'html.parser')
    popFinder = re.compile(r'((2020).*(v:)\s*(\d{5,10}))')
    popMatchedObject = popFinder.search(popSoup.text)
    population = f'{int(popMatchedObject.group(4)):,}'
    return str(population)
if len(sys.argv) > 1:
    argvList = list(sys.argv[1:])
    for i in argvList:
        print(f'The Population of {i.capitalize()} is: ' + populationFinder(linkMaker(i.lower())))
else:
    if len(countryList) == 0:
        print('The country list is empty')
    for i in countryList:
        print(f'The Population of {i.capitalize()} is: ' + populationFinder(linkMaker(i.lower())))

