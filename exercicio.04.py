def calcular_media(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    quantidade = len(numeros)
    if quantidade == 0:
        media = 0
    else:
        media = soma / quantidade
    return media

numeros_aleatorios = [10, 20, 30, 40, 50]
print(calcular_media(numeros_aleatorios))