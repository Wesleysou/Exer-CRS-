n1=float(input("Digite o primeiro valor: "))
n2=float(input("Digite o segundo valor: "))

op=input("Digito o tipo de cálculo: ")

if op =='+':
    print("A soma de ",n1,"com ",n2,"é igual a: ",(n1+n2))
elif op=='-':
    print("A subtração de ",n1,"com ",n2,"é igual a: ",(n1-n2))
elif op=='*':
    print("A multiplicação de ",n1,"com ",n2,"é igual a: ",(n1*n2))
elif op=='/':
    if(n2==0):
       print("Não podemos fazer divisão por zero")
    else:
        print("A divisão de ",n1,"com ",n2,"é igual a: ",(n1/n2))
