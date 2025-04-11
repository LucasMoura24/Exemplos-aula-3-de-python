f = open ('arquivo_teste.txt', 'w+')

texto = ["palavra 1", "palavra 2", "palavra 3"]

for linha in texto:
    f.write(linha)
    f.write("/n")
f.close()