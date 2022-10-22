import requests, json

request = requests.get("https://api.hgbrasil.com/finance?format=json/quotations?key=665616e3")
data = json.loads(request.content)

dolar = data['results']['currencies']['USD']['buy']
euro = data['results']['currencies']['EUR']['buy']

real = float(input('Digite o valor em reais: \n'))

conversao_dolar = real*dolar
conversao_euro = real*euro
print("O valor de", real, "reais convertido é:\n")
print(conversao_dolar, "dólares")
print(conversao_euro, "euros")
