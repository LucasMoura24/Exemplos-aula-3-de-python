f = open ('teste.txt' , 'w')
f.write('textp 1')
f.close()

f = open ('teste.txt', 'r')
print(f.read())
f.close()