#3) Escreva um programa em Python para calcular o valor de uma prestação em
#atraso (prestacao). Para isso, obtenha o valor da prestação (valorPrestacao),
#a porcentagem de multa pelo atraso (multa) e a quantidade de dias de atraso
#(qtdeDias). Calcular e mostrar o valor da prestação atualizado, sabendo que: 
#prestacao=valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)
valorPrestacao=int(input("Digite o valor de sua prestação:"))
qtdeDias=int(input("Quantos dias a prestação está atrasada:"))
multa=float(input("Qual é a multa por atraso:"))
prestacao=valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)
print("O valor da prestação é",prestacao)

