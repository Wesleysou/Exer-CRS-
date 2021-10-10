valor=int(input('Digite o valor:'))
notascem=0
notascinquenta=0
notasvinte=0
notasdez=0
notascinco=0
notasdois=0
notasum=0

while(valor !=0):
    if(valor>= 100):
         valor = valor - 100
         notascem = notascem +1
    elif(valor>= 50):
          valor = valor - 50
          notascinquenta = notascinquenta + 1
    elif(valor>= 20):
          valor = valor - 20
          notasvinte = notasvinte + 1
    elif(valor>= 10):
          valor = valor - 10
          notasdez = notasdez + 1
    elif(valor>= 5):
          valor = valor - 5
          notascinco = notascinco + 1
    elif(valor>= 2):
          valor = valor - 2
          notasdois = notasdois + 1
    elif(valor>= 1):
          valor = valor - 1
          notasum = notasum + 1

print( notascem,'Nota(s) de R$ 100,00')
print( notascinquenta,'Nota(s) de R$ 50,00')
print( notasvinte,'Nota(s) de R$ 20,00')
print( notasdez,'Nota(s) de R$ 10,00')
print( notascinco,'Nota(s) de R$ 5,00')
print( notasdois,'Nota(s) de R$ 2,00')
print( notasum,'Nota(s) de R$ 1,00')
