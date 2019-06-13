# projeto-em-python
num=int(input("digite um número: "))
contador=1
while contador <= num:
    if num%2==1:
        contador=contador+1
        print("É primo")
        break
    else:
        print("não é primo")
        break
