'''
A nomenclatura simplificada "Classificação Internacional de Doenças" refere-se ao
instrumentos de base epidemiológica que organiza informações sobre doenças, sinais,
sintomas, achados anormais, queixas, circunstâncias sociais e causas externas.
A CID-10, décima versão do documento, foi aprovada em 1994.
Dois anos mais tarde, começou a ser utilizada no Brasil.
Fonte: https://amplimed.com.br/cid-10?utm_source=cid-10&utm_medium=organic&utm_campaign=cid-10
consulta realizada em maio de 2021
Como o CID-10 possui 14210 infelismente não poderemos utilizar todo s ítens desta relação.
Mesmo assim "vamos supor que temos a nossa lista completa"
O RH de sua empresa acaba recebendo diversos atestados médicos e em todos vem com o CID-10.
Alguns casos são fáceis de identificar pela grande quantidade de casos corriqueiros por exemplo:
código U07.1 da doença "COVID-19 vírus identificado"
código B30  da doença "Conjuntivite viral"
código B30.9 da doença "Conjuntivite viral não especificada"

Baseando-se nas listas já populadas efetue os seguintes relatórios:
1 - Quantidade de doenças "lista descrição" cadastradas com mais de 300 casos
2 - Exibir o CID das doenças e a descrição de cada uma
3 - Quantidade de casos de uma doença com funcionários da empresa (este código a ser pesquisado o usuário deverá digitar)
4 - Localizar e exibir uma doença dado o código digitado pelo usuário
5 - Relatório contendo a descrição o CID e a quantidade de casos já contabilizado pela empresa
6 - Relatório de doenças com o mesmo número
7 - Relatório de quantas doenças possuem a letra digitada pelo usuário caso não tenha a letra digitada exibir (doença não cadastrada)
8 - Relatório com a média de casos de doenças cadastradas
9 - Relatório com as doenças com casos acima da média
10 - Relatório com as doenças com casos abaixo da média
11 - Exibir as doenças na ordem inversa a que mostra na lista
12 - Listagem das doenças com números pares
13 - Listagem das doenças com números ímpares
14 - O somatório de casos de doenças que teve com os funcionários da empresa
Como a empresa sabe que não dará tempo de enviar todos os relatórios ela sugere a seguinte proposta:

Escolha 5 relatórios citados acima para enviar ao professor Douglas para ele conferir e assim atribuir a nota de sua avaliação!

Cada relatório vale 1,0 ponto

Em seu programa você deverá inserir o comentários quais foram os relatórios escolhidos.

Caso tenha mais de cinco relatórios, serão considerados somente os 5 primeiros relatórios inseridos em seu arquivo.
'''
ordem=[2,6,12,18,25,36,44,55,62,70,81,91,96,106,112,120,128,135,142,148,152,157,161,167,176,181,190,197,203,212,219,228,235,240,246,253,260,270,278,286,289,300,309,313,317,322,333,339,343,350,354,358,364,372,377,384,390,394,404,409,415,421,428,436,442,446,452,461,471,477,487,495,500,509,512,517,522,528,531,542,550,555,561,567,574,579,586,592,600,610,617,628,637,645,653,658,664,670,677,685,694,698]
letra=['A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B']
numero=[0,1,2,3,4,5,6,7,8,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,36,37,39,40,41,42,43,44,48,49,50,51,52,53,54,56,59,60,63,66,67,68,69,71,74,75,77,79,80,81,82,83,84,85,87,88,92,93,95,96,98,0,1,2,5,6,8,15,16,17,18,19,20,21,22,23,25,26,27,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48]
letraNumero=['A.00','A.01','A.02','A.03','A.04','A.05','A.06','A.07','A.08','A.15','A.16','A.17','A.18','A.19','A.20','A.21','A.22','A.23','A.24','A.25','A.26','A.27','A.28','A.30','A.31','A.32','A.36','A.37','A.39','A.40','A.41','A.42','A.43','A.44','A.48','A.49','A.50','A.51','A.52','A.53','A.54','A.56','A.59','A.60','A.63','A.66','A.67','A.68','A.69','A.71','A.74','A.75','A.77','A.79','A.80','A.81','A.82','A.83','A.84','A.85','A.87','A.88','A.92','A.93','A.95','A.96','A.98','B.00','B.01','B.02','B.05','B.06','B.08','B.15','B.16','B.17','B.18','B.19','B.20','B.21','B.22','B.23','B.25','B.26','B.27','B.30','B.33','B.34','B.35','B.36','B.37','B.38','B.39','B.40','B.41','B.42','B.43','B.44','B.45','B.46','B.47','B.48']
cod=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
CID=['A00.0','A01.0','A02.0','A03.0','A04.0','A05.0','A06.0','A07.0','A08.0','A15.0','A16.0','A17.0','A18.0','A19.0','A20.0','A21.0','A22.0','A23.0','A24.0','A25.0','A26.0','A27.0','A28.0','A30.0','A31.0','A32.0','A36.0','A37.0','A39.0','A40.0','A41.0','A42.0','A43.0','A44.0','A48.0','A49.0','A50.0','A51.0','A52.0','A53.0','A54.0','A56.0','A59.0','A60.0','A63.0','A66.0','A67.0','A68.0','A69.0','A71.0','A74.0','A75.0','A77.0','A79.0','A80.0','A81.0','A82.0','A83.0','A84.0','A85.0','A87.0','A88.0','A92.0','A93.0','A95.0','A96.0','A98.0','B00.0','B01.0','B02.0','B05.0','B06.0','B08.0','B15.0','B16.0','B17.0','B18.0','B19.0','B20.0','B21.0','B22.0','B23.0','B25.0','B26.0','B27.0','B30.0','B33.0','B34.0','B35.0','B36.0','B37.0','B38.0','B39.0','B40.0','B41.0','B42.0','B43.0','B44.0','B45.0','B46.0','B47.0','B48.0']
descricao=['Cólera devida a Vibrião cholerae 01 biótipo cholerae','Febre tifoide','Enterite por salmonela','Shiguelose devida a Shigella dysenteriae','Infecção por Escherichia coli enteropatogênica','Intoxicação alimentar estafilocócica','Disenteria amebiana aguda','Balantidíase','Enterite por rotavírus','Tuberculose pulmonar com confirmação por exame microscópio da expectoração com ou sem cultura','Tuberculose pulmonar com exames bacteriológico e histológico negativos','Meningite tuberculosa','Tuberculose óssea e das articulações','Tuberculose miliar aguda de localização única e especificada','Peste bubônica','Tularemia ulceroglandular','Carbúnculo cutâneo','Brucelose por Brucella melitensis','Mormo','Espirilose','Erisipelóide cutâneo','Leptopirose icterohemorrágica','Pasteurelose','Hanseníase [lepra] indeterminada','Infecção pulmonar micobacteriana','Listeriose cutânea','Difteria faríngea','Coqueluche por Bordetella pertussis','Meningite meningocócica','Septicemia por Streptococcus do grupo A','Septicemia por Staphylococcus aureus','Actinomicose pulmonar','Nocardiose pulmonar','Bartonelose sistêmica','Gangrena gasosa','Infecção estafilocócica não especificada','Sífilis congênita precoce sintomática','Sífilis genital primária','Sífilis cardiovascular','Sífilis latente  não especificada se recente ou tardia','Infecção gonocócica do trato geniturinário inferior sem abscesso periuretral ou das glândulas acessórias','infecções por clamídias do trato geniturinário inferior','Tricomoníase urogenital','Infecção dos órgãos genitais e do trato geniturinário pelo vírus do herpes','Verrugas anogenitais (venéreas)','Lesões iniciais da bouba','Lesões primárias da pinta','Febre recorrente transmitida por piolhos','Estomatite ulcerativa necrotizante','Fase inicial do tracoma','Conjuntivite causada por clamídias','Tifo epidêmico transmitido por piolhos devido a Rickettsia prowazekii','Febre maculosa por Rickettsia richettsii','Febre das trincheiras','Poliomielite paralítica aguda associada ao vírus vacinal','Doença de Creutzfeldt-Jakob','Raiva silvestre','Encefalite japonesa','Encefalite da taiga [encefalite vernoestival russa]','Encefalite por enterovírus','Meningite por enterovírus','Febre exantemática por enterovírus [exantema de Boston]','Febre de Chikungunya','Febre de Oropouche','Febre amarela silvestre','Febre hemorrágica de Junin','Febre hemorrágica da Criméia (do Congo)','Eczema herpético','Meningite por varicela','Encefalite pelo vírus do herpes zoster','Sarampo complicado por encefalite','Rubéola com complicações neurológicas','Outras infecções por ortopoxvírus','Hepatite A com coma hepático','Hepatite aguda B com agente Delta (co-Infecção) com coma hepático','(Super)Infecção Delta aguda de portador de hepatite B','Hepatite viral crônica B com agente Delta','Hepatite viral não especificada sem coma','Doença pelo HIV resultando em infecções micobacterianas','Doença pelo HIV resultando em sarcoma de Kaposi','Doença pelo HIV resultando em encefalopatia','Síndrome de Infecção aguda pelo HIV','Pneumonite por citomegalovírus','Orquite por caxumba [parotidite epidêmica]','Mononucleose pelo vírus herpes gama','Ceratoconjuntivite devida a adenovírus','Mialgia epidêmica','Infecção por adenovírus não especificada','Tinha da barba e do couro cabeludo','Pitiríase versicolor','Estomatite por Candida','Coccidioidomicose pulmonar aguda','Histoplasmose pulmonar aguda por Histoplasma capsulatum','Blastomicose pulmonar aguda','Paracoccidioidomicose pulmonar','Esporotricose pulmonar','Cromomicose cutânea','Aspergilose pulmonar invasiva','Criptococose pulmonar','Mucormicose pulmonar','Eumicetoma','Lobomicose']
casos=[340,412,480,427,43,222,46,294,490,100,274,428,457,71,198,414,432,127,347,23,132,271,282,194,189,369,299,25,442,90,422,272,278,79,357,280,29,2,225,260,279,393,126,286,9,391,443,370,401,438,203,93,215,320,179,398,89,266,253,217,226,95,232,142,240,228,489,131,199,138,182,442,391,495,229,245,291,141,316,43,304,69,186,442,322,84,333,181,91,119,420,276,413,52,244,198,409,43,37,378,175,74]
show =[]

#2 - Exibir o CID das doenças e a descrição de cada uma
print("2 - Exibir o CID das doenças e a descrição de cada uma")
for i in range (len(CID)):
    print(CID[i] +" \ "+ descricao[i])
    

print('IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')
print('IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')

#12 - Listagem das doenças com números pares
print("12 - Listagem das doenças com números pares")
show=[]
for item in range (len(numero)):
    if(numero[item]%2 == 0):
        show.append( '%d'%numero[item] + " \ " + descricao[item])
print("Doenças com numero par")
for i in range (len(show)):
    print("%s\n"%show[i])

print('IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')
print('IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')

#13 - Listagem das doenças com números ímpares
print("13 - Listagem das doenças com números ímpares")
for item in range (len(numero)):
    if(numero[item]%2 == 1):
        show.append( "%d"%numero[item] + " \ " + descricao[item])
print("Doenças com numero impar")
for i in range (len(show)):
    print("%s\n"%show[i])

print('IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')
print('IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')

#14 - O somatório de casos de doenças que teve com os funcionários da empresa
print("14 - O somatório de casos de doenças que teve com os funcionários da empresa")
soma=sum(casos)
print("O valor total é de ",soma)

print('IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')
print('IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')

#11 - Exibir as doenças na ordem inversa a que mostra na lista
print("11 - Exibir as doenças na ordem inversa a que mostra na lista")
descricao.reverse()
print(descricao) 


    



    
