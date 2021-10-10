percentual=float(input("Digite o percentual de frequência: "))
nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
media=(nota1+nota2)/2
if media>=5.75 and media<5.99:
    media=6
if percentual<75:
    print("Reprovado por frequência")
else:
    if media>=6:
        print("Aprovado")
    else:
        print("Reprovado por nota")
