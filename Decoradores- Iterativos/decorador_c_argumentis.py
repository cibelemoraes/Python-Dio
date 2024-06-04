def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        resultado = funcao(*args, **kwargs)
        print("faz algo depois de executar")
        return resultado
    return envelope


@meu_decorador
def ola_mundo(nome):
    print("Ola Mundo!", nome)

ola_mundo("João")