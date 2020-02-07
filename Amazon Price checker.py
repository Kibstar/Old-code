import bs4, requests, time, smtplib, os
URL = 'https://www.amazon.co.uk/Canon-Compact-System-RF24-105mm-Adapter/dp/B07NJ5DBF9/'
myEmail = os.environ.get('GMAIL')
myPass = os.environ.get('PYTHON_GMAIL_PASS')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

def checkPrice(url):
    res = requests.get(URL, headers = headers)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    price = int(soup.find(id='price_inside_buybox').get_text().strip()[1:6].replace(',',''))
    if price < 2100:
        sendMail()
    print(f'£{price:,}')

def sendMail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(myEmail, myPass)
    subject = 'The price has dropped!'
    mainBody = f'The price has dropped below $2100! Here is the link: {URL}'
    server.sendmail(myEmail, myEmail, f'Subject: {subject}\n\n{mainBody}\n\nPython')
    print('Email sent!')
    server.close()

checkPrice(URL)
print('Hello World')
