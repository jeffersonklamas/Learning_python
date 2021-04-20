#Encurtador de url com python
#by @jeffersonklamas

#instale o pyshorteners com pip install pyshorteners

#Pensar em inserir formulário onde se cola a url e automaticamente gera uma nova url.

import pyshorteners

#url = Input("Cole ou digite a URL que quer encurtar: ")

# URL original

url = "https://www.pmi.org/learning/library/pmo-agile-transformation-6063"

# Carregando a lib

encurta = pyshorteners.Shortener()

# Irá gerar a URL encurtada

shortUrl = encurta.tinyurl.short(url)

# A nova url

print(f"URL Encurtada: {shortUrl}")