url ="bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

print (url)

indice_fatiamento = url.find('?')
url_base = url[0:indice_fatiamento]
print(url_base)

indice = url.find('&')
url_parametros = url [indice_fatiamento+1:indice]
print(url_parametros)
 