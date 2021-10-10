#Elaborar um programa em Python que solicite os dados de estatura (em metros)
#e peso (em Kg) de uma pessoa e calcule/visualize seu IMC (Índice de Massa
#Corporal). Lembre que IMC = peso/estatura²

tura=float(input("Digite sua altura"))
pe=float(input("Digite seu peso"))
pap=tura*tura
imc=pe/pap
print("Seu imc é",imc)
