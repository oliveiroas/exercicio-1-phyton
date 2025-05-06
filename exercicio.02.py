def somar_numeros(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

numeros_aleatorios = [1, 2, 3, 4, 5]  
resultado = somar_numeros(numeros_aleatorios)
print(resultado)