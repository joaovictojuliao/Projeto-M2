import Classe2 as cl
pesquisa=0
cont=1
rodando=True
lista_nome=[]
lista_idade = []
lista_genero = []
pergunta1 = []
pergunta2 = []
pergunta3 = []
pergunta4 = []
dataEHora = []
dict = {
    'Nome ':lista_nome,
    'Idade ':lista_idade,
    'Genero ':lista_genero,
    'Pergunta-1 ':pergunta1,
    'Pergunta-2 ':pergunta2,
    'Pergunta-3 ':pergunta3,
    'Pergunta-4 ':pergunta4,
    'Data e hora ':dataEHora   
} 

pesquisa=cl.PesquisaSaude.inicio(cl.PesquisaSaude, pesquisa)
if cl.PesquisaSaude.inicio(cl.PesquisaSaude, pesquisa)==1:
    while rodando:
        nome=input(f'Digite o nome do {cont}º entrevistado: ') 
        idade = 1
        idade = cl.PesquisaSaude.idadeVerif(cl.PesquisaSaude, idade)
        if idade == 0:
            print('\n\n**************************PROGRAMA FINALIZADO**************************\n')
            cl.PesquisaSaude.arquivoCsv(cl.PesquisaSaude,dict)
            break
       
        genero=cl.PesquisaSaude.generos(cl.PesquisaSaude)    
        perguntas=cl.PesquisaSaude.quatroPerguntas(cl.PesquisaSaude, 0,0,0,0)
        dt=cl.PesquisaSaude.dataHora(cl.PesquisaSaude)

        lista_idade.append(idade)
        lista_nome.append(nome)
        lista_genero.append(genero)
        pergunta1.append(perguntas[0])
        pergunta2.append(perguntas[1])
        pergunta3.append(perguntas[2])
        pergunta4.append(perguntas[3])
        dataEHora.append(dt)
        cont+=1
else:
    print('\n\n**************************PROGRAMA FINALIZADO**************************\n')
    
