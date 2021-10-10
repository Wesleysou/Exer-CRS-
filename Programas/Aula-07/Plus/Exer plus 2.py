resp='s'

while(resp=='s' or resp=='S'):

     cod=input("Digite o código do exame(A,B,C ou D)")

     if(cod=='A' or cod=='a'):

         print("Angiografia = R$ 155,50")

     elif(cod=='B' or cod=='b'):

         print("Venografia = R$ 95,50")

     elif(cod=='C' or cod=='c'):

         print("Urografia = R$ 387,95")

     elif(cod=='D' or cod=='d'):

         print("Ultrasson = R$ 79,99")

     else:

         print("Não trabalhamos com esse exame")

     resp=input("Digite s para continuar")  
