'''n1=float(input("Digite o primeiro valor: "))
n2=float(input("Digite o segundo valor: "))
n3=float(input("Digite o terceiro valor: "))
if(n1>n2 and n1>n3):
    print("O primeiro valor é o maior")
elif(n2>n1 and n2>n3):
    print("O segundo valor é o maior")
else:
    print("O terceiro valor é o maior")'''


n1=float(input("Digite o primeiro valor: "))
n2=float(input("Digite o segundo valor: "))
n3=float(input("Digite o terceiro valor: "))
if(n1>n2 and n1>n3):
    print("O primeiro valor é o maior")
else:
    if (n2>n1 and n2>n3):
        print("O segundo valor é o maior")
    else:
        print("O terceiro valor é o maior")
