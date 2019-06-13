# projeto-em-python
print('Digite um número para verificar se ele é perfeito ')
n = int(input('digite o número : '))
cont = 1
soma = 0

while(cont<n):
 if (n%cont) == 0:
     soma = soma + cont
     cont = cont + 1
 else:
     cont = cont + 1

if (soma==n):
    print("O número " + str(n) + " é um número perfeito")
else:
    print("o número " + str(n) + " não é um número perfeito")
