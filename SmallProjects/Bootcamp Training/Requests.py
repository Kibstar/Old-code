import requests, os

res = requests.get('http://automatetheboringstuff.com/files/rj.txt')
first500 = res.text[:500]

res.raise_for_status()

badRes = requests.get('http://google.com/gogoglwsf')
try:
    badRes.raise_for_status()
except:
    print('Bad link')

folderPath = r'C:\Users\jackk\Documents\Python Things\Requests\\'

if os.path.isdir(folderPath) == False:
    os.mkdir(folderPath)

romeo = open(folderPath + 'Romeo and Juliet.txt','wb')
for chunk in res.iter_content(10000):
    romeo.write(chunk)
romeo.close()