valor= int(input('Digite um número: '))
zipo=1
if (valor>0):    
  for n in range(2,(valor+1)):
    zipo =zipo+(1/n)
    print('Controle de valores\n acum=',zipo,'\no valor de N é',n)
    input()
  print('O resultado é: ', zipo)
else:
  print ('Valor inserido errado.')
