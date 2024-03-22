# Criando um dicionário com alguns dados sobre uma pessoa
pessoa = {
    'nome': 'João', 'idade': 30, 'cidade': 'São Paulo', 'profissão': 'Engenheiro'
}

"""# Acessando os valores do dicionário
print("Nome:", pessoa['nome'])
print("Idade:", pessoa['idade'])
print("Cidade:", pessoa['cidade'])
print("Profissão:", pessoa['profissão'])"""

"""# Adicionando um novo par chave-valor ao dicionário
pessoa['email'] = 'joao@example.com'
print("Email:", pessoa['email'])

# Alterando o valor de uma chave
pessoa['idade'] = 31
print("\nNova idade de", pessoa['nome'] + ":", pessoa['idade'])"""

"""del pessoa['cidade']
# Verificando se uma chave existe no dicionário
if 'cidade' in pessoa:
    print("\nCidade de", pessoa['nome'] +": pessoa['cidade]")
else:
    print('\nInformações sobre a cidade não encontrada')"""
    
# Verificando se uma determinada chave existe em um dicionario
#print(pessoa.get("nome",{}))

"""novo_dicionario = {"a":100, 1: "teste", "b": "python"}
print(novo_dicionario.keys())"""

#verificando se uma chave existe ,e adicionando outra ao mesmo tempo 

"""pessoa.setdefault("cep", 54110415)
print(pessoa)"""

#atualizando um dicionario com outras chaves

pessoa.update({"cidade": "recife"})
print(pessoa)

