arquivo = open(r'C:\Users\cibel\Downloads\video visagio.txt')  # Usando uma string raw para evitar problemas com caracteres de escape

#print(arquivo.read())

#print(arquivo.readline())

print(arquivo.readlines())
arquivo.close()
