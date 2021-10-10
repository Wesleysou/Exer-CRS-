nomes=[]
nota=[]
resp='S'

while(resp=='s'or resp=='S'):
    n=input('Digite o nome dos alunos')
    parcial=float(input('Digite a nota da parcial'))
    nome.append(n)
    nota.append(parcial)
    

    resp=(input('Digite s para continuar'))

acum=0
for i in range(len(nota)):
    acum=acum+nota[i]
    
media=acum/len(nota)

print(media)

for i in range(len(nota)):
    if(nota[i]>=media):
        print('O aluno',nomes[i],'está acima da média')
        print('nota',nota[i])
