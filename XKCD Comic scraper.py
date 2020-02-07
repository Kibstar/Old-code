import requests, bs4, re, os


folderPath = r'C:\Users\jackk\Documents\Python Things\XKCD Comics\\'

def comicLinkGetter(num):
    if os.path.isfile(folderPath + str(num) + '.jpg')== False:
        print(folderPath + str(num) + '.jpg')

        res = requests.get('http://xkcd.com/' + str(num))
        try:
            res.raise_for_status()
        except Exception:
            print(f'Comic {num} is not available')
            return
        soup = bs4.BeautifulSoup(res.text,'html.parser')
        elem = soup.find(id = 'comic') ## Search by ID has a lot more continuity across multiple web pages
        linkFinder = re.compile(r'((imgs)\S*(.png|jpg))') ## Looks for links ending are JPEG or PNG
        imageLinkSearch = linkFinder.search(str(elem)) ## Needs to be converted to a string
        if imageLinkSearch == None:
            print('Couldnt find a link')
            return
        link = imageLinkSearch.group()
        return 'https://' + link


def comicDownloader(link,i):
    if link == None:
        return
    res = requests.get(link)
    try:
        res.raise_for_status()
    except Exception:
        print(f'Could not connect to webpage {i}')
    if os.path.isdir(folderPath) == False:
        os.mkdir(folderPath)
    imageFile = open(folderPath + str(i)+'.jpg','wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)

for i in range(1,3000):
    comicDownloader(comicLinkGetter(i),i)
