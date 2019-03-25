#! python3
#southpy - abre un capítulo de South Park al azar o elegido.

import requests, sys, webbrowser, bs4, random
def capxtemp(temp):
    listcaps = [0,13,18,17,17,14,17,15,14,14,14,14,14,14,14,14,10,10,10,10,10,10] #Caps por temporada
    nro= random.randint(1,listcaps[temp])#Capítulo en la temporada
    temp = str(temp)
    if len(temp) ==1:
        temp = '0'+temp
    
    nro = str(nro)
    if len(nro)==1:
        nro = '0'+nro
    
    return temp+'x'+nro


#Si tiene dos números, elegir ese capítulo
if len(sys.argv) > 2:
    #Sacar la dirección de la línea de comandos.
    temp = str(sys.argv[1])
    nro = str(sys.argv[2])
    if len(temp) ==1:
        temp = '0'+temp
    
    nro = str(nro)
    if len(nro)==1:
        nro = '0'+nro
    
    cap= temp+'x'+nro
    

#Si tiene uno solo, elegir esa temporada
elif len(sys.argv) == 2:
    temp = int(sys.argv[1])
    cap=capxtemp(temp)

else:
    #Capítulo al azar
    temp = random.randint(1,22)
    cap = capxtemp(temp)
    
print('Va')
res = requests.get('https://www.google.com/search?q=site%3Atotalsouthpark.blogspot.com+' + cap)
res.raise_for_status()

# Obtener los links de los primeros resultados
soup = bs4.BeautifulSoup(res.text)

# Abrir una pestaña del navegador para cada resultado.
linkElms = soup.select('.r a')

webbrowser.open('http://google.com' + linkElms[0].get('href'))
print('Al carajo, yo me voy')




