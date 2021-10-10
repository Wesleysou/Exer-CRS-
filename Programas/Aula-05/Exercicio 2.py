#luz=float(input("Digite o valor da conta de luz:"))
#agua=float(input("Digite o valor da conta de água:"))
#salario=float(input("Digite o seu salário:"))
#plus = (luz+agua+telefone)
#menos= salari-plus
#if(plus > salario):
#   print("Seu salario não é suficiente")
#else:
 #  print("Seu salario foi sulficiente oque restou foi",menos)
agua=float(input("Digite o valor da sua Água: "))

imposto=float(input("Digite o valor do seu Imposto: "))

telefone=float(input("Digite o valor do telefone: "))

salario=float(input("Digite seu salário: "))

contas = agua+imposto+telefone



if (agua+imposto+telefone)<=salario:

  sobra = salario-contas

  print("Ebaa! Seu salario é suficiente para pagar as três contas")

  print("Sobraram", sobra, "do seu salário")

else:

  print("Seu salário não é suficiente para pagar suas contas")
