from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://resultados.as.com/resultados/futbol/champions/clasificacion/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
eq = soup.find_all('span', class_='nombre-equipo')
equipo = list()

count = 0
for i in eq:
   if count < 4:
       equipo.append(i.text)
   else:
       break
   count += 1

pnts = soup.find_all('td', class_='destacado')

puntos = list()
count = 0
for i in pnts:
   if count < 4:
       puntos.append(i.text)
   else:
       break
   count += 1

dframe = pd.DataFrame(
    {'Nombre': equipo, 'Puntaje': puntos}, 
    index=list(range(1,5)))
print(dframe)