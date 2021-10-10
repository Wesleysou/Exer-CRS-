compra=float(input("Digite o valor de sua compra"))



if compra>200.00:

   desconto = compra * 2/100

   print("Sua compra teve um desconto de 20%", " \n preço final = %.2f" %(compra-desconto))

else:

   print("Sua compra não teve desconto \n preço final = %.2f" %compra)
