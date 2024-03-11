"""maior_idade=18
idade_especial=12

idade = int(input("informe sua idade: "))

if idade >= maior_idade:
    print("maior de idade, pode tirar a CNH")


if idade < maior_idade:
    print("ainda não pode tirar a cnh")

if idade >= maior_idade:
    print("maior de idade, pode tirar a CNH")
else:
    print("ainda não pode tirar a CNH.")


if idade >= maior_idade:
    print("maior de idade, pode tirar a CNH")
elif idade == idade_especial:
    print("pode fazer as aulas teoricas , mais não pode fazer as aulas praticas")
else:
    print("ainda não pode tirar a CNH.")"""

#ESTRUTURAS CONDICIONAIS ANINHADAS

conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("saque realizado com sucesso com uso do cheque especial")
    else:
        print("não foi possivel realizar o saque, saldo infuficiente!")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("saldo insuficiente!")
else:
    print("o sistema não reconheceu esse tipo de conta , entre em contato com seu gerente")