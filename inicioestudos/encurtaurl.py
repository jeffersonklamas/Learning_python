#Encurtador de url com python
#by @jeffersonklamas

#instale o pyshorteners com 

pip install pyshorteners

import pyshorteners

# URL original

url = "https://www.pmi.org/learning/library/pmo-agile-transformation-6063"

# Carregando a lib

sh = pyshorteners.Shorteners()

# Irá gerar a URL encurtada

shortUrl = sh.tinyurl.short(url)

# A nova url

print(f"URL Encurtada: {shortUrl}")