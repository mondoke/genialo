#! python3
#southpy - opens a random South Park Episode

import requests, sys, webbrowser, bs4, random
#Selects a server. If you want to watch from a different site, change the next line. The default is a page with latin american south park dub.
site = 'totalsouthpark.blogspot.com'
def capxtemp(temp):
    listcaps = [0,13,18,17,17,14,17,15,14,14,14,14,14,14,14,14,10,10,10,10,10,10] #Caps per season
    nro= random.randint(1,listcaps[temp])
    temp = str(temp)
    if len(temp) ==1:
        temp = '0'+temp
    
    nro = str(nro)
    if len(nro)==1:
        nro = '0'+nro
    
    return temp+'x'+nro


#If it has two numbers A and B, chooses cap AxB
if len(sys.argv) > 2:
    #Gets the adress from the command line
    temp = str(sys.argv[1])
    nro = str(sys.argv[2])
    if len(temp) ==1:
        temp = '0'+temp
    
    nro = str(nro)
    if len(nro)==1:
        nro = '0'+nro
    
    cap= temp+'x'+nro
    

#If given one number, that indicates season
elif len(sys.argv) == 2:
    temp = int(sys.argv[1])
    cap=capxtemp(temp)

else:
    #Random episode
    temp = random.randint(0,22)
    cap = capxtemp(temp)
    
print('Va')
res = requests.get('https://www.google.com/search?q=site%3A' + site + '+' + cap)
res.raise_for_status()

#Gets links from the results
soup = bs4.BeautifulSoup(res.text)

#opens a browser window with the result
linkElms = soup.select('.r a')

webbrowser.open('http://google.com' + linkElms[0].get('href'))
print('Al carajo, yo me voy')
