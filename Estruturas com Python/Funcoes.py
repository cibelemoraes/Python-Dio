"""def exibir_mensagem():
    print("Ola Mundo!")
    
def exibir_mensagem_3(nome="Cibele"):
    print(f"Seja bem vinda {nome}!")
    
def exibir_mensagem_4(nome):
    print(f"Seja bem vinda {nome}!")
    
exibir_mensagem()
exibir_mensagem_3()
exibir_mensagem_4("Fernanda")"""

#funções de soma

"""def calcular_total(numeros):
    return sum(numeros)

def retornar_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return antecessor, sucessor

def func_3():
    print("Olá Mundo! ")
    
 
 
print(calcular_total([10, 20, 40]))   
print(retornar_antecessor_e_sucessor(10))
print(func_3())"""


"""#salvar carro no banco de dados....
def salvar_carro(marca, modelo, ano, placa):
    #salvar carro no banco de dados....
    print(f"carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")
    
salvar_carro("Palio", "Fiat", 1999, "ABC-1234")    
salvar_carro(marca= "Fiat", modelo= "Palio", ano="1999", placa="ABC-1234")"""

#funções para exibir lista e dicionarios

def exibir_poema(data_extenso, *args, **Kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in Kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)
    
    
exibir_poema("Segunda feira, 25 de março de 2023",
    "Minha alma tem o peso da luz",

"Tem o peso da música",

"Tem o peso da palavra nunca dita",

"Prestes quem sabe a ser dita",

"Tem o peso de uma lembrança",

"Tem o peso de uma saudade",

"Tem o peso de um olhar",

"Pesa como pesa uma ausência",

"E a lágrima que não chorou",

"Tem o imaterial peso de uma solidão",
autor= "Clarice Lispector",
ano= 1956,
)