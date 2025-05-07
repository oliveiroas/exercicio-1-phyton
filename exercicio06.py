def cadastrar_filme(nome, descricao, classificaçao, categoria01, categoria02, categoria03):
    dados_filme = []
    filme = {
        "nome":nome,
        "descricao": descricao,
        "classificaçao": classificaçao,
        "categoria": [categoria01, categoria02, categoria03]
    }    
    dados_filme.append(filme)
    return dados_filme

print(cadastrar_filme("Velozes E Furiosos", "Filme De Ação Sobre Carros", "14 anos", "Açao", "Suspense", "Aventura"))