f = open ('arquivo_teste.txt', 'r')
for linha in f:
    print(linha.split())
f.close()