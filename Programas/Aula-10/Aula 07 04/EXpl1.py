#         0         1     2       3        4          5 
nomes=['Wesley','Maria','João','Carlos','Ronald','Marcos']
for i in range(5):
    n=input("Digite seu nome")
    nomes.insert(i,n)
#a variavel i indica o índice
#em n o valor a ser atribuido
print(nomes)    

#nomnomes.remove(4)
x=nomes.pop()
print(nomes)

nomes.sort()
print(nomes)

