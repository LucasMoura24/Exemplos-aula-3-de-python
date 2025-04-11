with open('teste.txt', 'w') as f:
    f.write('texto 1\n')
    f.write('texto 2')

with open('teste.txt', 'r') as f:
    print(f.read())    