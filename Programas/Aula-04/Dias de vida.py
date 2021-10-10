#2) Crie um programa em Python que solicite ao usuário a sua idade expressa em
#anos, meses e dias (variáveis separadas). Calcule e mostre a idade expressa
#apenas em dias. Para isso considere 1 ano = 365 dias, 1 mês = 30 dias
idade=int(input("Digite sua idade:"))
messes=int(input("Quantos messes a menos para o seu próximo aniversario:"))
dias=int(input("Quantos dias para completar um próximo mes:"))
tic=idade*365
plac=messes*30
drip=tic+plac
bololo=dias+drip
print("Você tem",bololo,"dias de vida.")

