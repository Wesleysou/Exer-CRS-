hm=float(input("Digite a quantidade de horas mensais trabalhadas: "))
he=float(input("Digite a quantidade de horas extras realizadas: "))
dias=int(input("Digite a quantidade de faltas: "))
ht=he+(hm-dias*8)

print("A quantidade de horas trabalhadas é de: ",ht)
