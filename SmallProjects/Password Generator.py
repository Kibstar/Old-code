import random, string

def askCriteria():
    capitals = False
    length = 7
    symbols = False

    caps = input('Does your password need uppercase characters in it?')
    if caps[0].lower() == 'y':
        capitals = True

    while length <= 7:
        leng = input('How long does your password need to be?')
        if leng.isdigit() == False:
            continue
        length = int(leng)

    symbs = input('Does your password need to contain any symbols?')
    if symbs[0].lower() == 'y':
        symbols = True

    return capitals, length, symbols

def passwordGen():

    symbols = list('''~`! @#$%^&*()_-+={[}]|\:;"'<,>.?/''')
    nums = list('1234567890')
    alpha = list(string.ascii_lowercase)
    alphaUpper = list(string.ascii_uppercase)
    pool = [nums,alpha]
    password = ''
    caps, leng, symbs = askCriteria()

    if caps == True:
        pool.append(alphaUpper)
    if symbs == True:
        pool.append(symbols)

    for i in range(leng):
        randCrit = pool[random.randint(0,len(pool)-1)]
        randObj = randCrit[random.randint(0,len(randCrit)-1)]
        password += randObj

    print(password)

passwordGen()