import Classe2 as cl
import datetime as date

lista_nome=[]
rodando=True
lista_idade = []
lista_genero = []
pergunta1 = []
pergunta2 = []
pergunta3 = []
pergunta4 = []
dict = {
    'nomes':lista_nome,
    'idades':lista_idade,
    'generos':lista_genero,
    'pergunta1':pergunta1,
    'pergunta2':pergunta2,
    'pergunta3':pergunta3,
    'pergunta4':pergunta4    
} 

while rodando:       
    idade = 1
    idade = cl.PesquisaSaude.idadeVerif(cl.PesquisaSaude, idade)
    if idade == 0:
        print('Programa finalizado')
        print(dict)
        break
    nome=input('Digite o nome do entrevistado: ')
    lista_idade.append(idade)
    genero=cl.PesquisaSaude.generos(cl.PesquisaSaude)
    lista_genero.append(genero)
    perguntas=cl.PesquisaSaude.quatroPerguntas(cl.PesquisaSaude, 0,0,0,0)
    lista_nome.append(nome)
    pergunta1.append(perguntas[0])
    pergunta2.append(perguntas[1])
    pergunta3.append(perguntas[2])
    pergunta4.append(perguntas[3])
