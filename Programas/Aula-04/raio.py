import math
raiomaior=float(input("Digite o valor do raio maior: \n"))
raiomenor=float(input("Digite o valor do raio menor: \n"))
alt=float(input("Digite a altura do cone: \n"))
volume=(math.pi*alt)/3*(math.pow(raiomaior,2)+raiomaior*raiomenor+math.pow(raiomenor,2))
print("O volume do tronco do cone é: \n%.2f"%volume)
