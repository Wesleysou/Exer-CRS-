qtdeDiárias=int(input("Digite a quantidade de diárias: "))
tipo=input("Digite o tipo de hospedagem: ")
if tipo=='S':
    print("Valor a pagar: ",(qtdeDiárias*255.5))
else:
    if tipo =='D':
        print("Valor a pagar: ",(qtdeDiárias*305.5))
    else:
        if tipo =='T':
            print("Valor a pagar: ",(qtdeDiárias*360.5))
        else:
            print("Tipo de hospegadem inválida")
