x = float(input("Insira um valor para X: "))
y = float(input("Insira um valor para Y: "))

if x < 0:
    if y < 0:
        print("Q3")
    elif y > 0:
        print("Q1")
    else:
        print("O Valor esta no Eixo X.")
elif x > 0:
    if y > 0:
        print("Q2")
    elif y < 0:
        print("Q4")
    else:
        print("O Valor está  X.")
else:
    if y != 0:
        print("O Valor está Y.")
    else:
        print("O Valor está na Origem.")
