from bs4 import BeautifulSoup
import requests

#página com inofrmações do tempo
html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/4295/pinhais-pr").content

#parser na pagina html
soup = BeautifulSoup(html,'html.parser')

#captura dados
resume = soup.find(class_='-gray -line-height-24 _center')
tempMin = soup.find(id='min-temp-1')
tempMax = soup.find(id='max-temp-1')

#Resultados
print("\n Resumo: " + resume.txt)
print('Temp. Minima: ' + tempMin.string)
print('Temp. Máxima: ' + tempMax.string)
