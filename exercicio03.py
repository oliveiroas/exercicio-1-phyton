def verificar_idade(nome, idade):
    if idade >= 18:
        return f"{nome}, você é maior de idade."
    else:
        return f"{nome}, você é menor de idade."

nome = "Vinicius"
idade = 16
resultado = verificar_idade(nome, idade)
print(resultado)
