import Classe2 as cl
import datetime as date

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
    'Nome':lista_nome,
    'Idade':lista_idade,
    'Gênero':lista_genero,
    'pergunta-1':pergunta1,
    'pergunta-2':pergunta2,
    'pergunta-3':pergunta3,
    'pergunta-4':pergunta4,
    'Data e hora':dataEHora   
} 

while rodando:       
    idade = 1
    idade = cl.PesquisaSaude.idadeVerif(cl.PesquisaSaude, idade)
    if idade == 0:
        print('Programa finalizado')
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
    dataHoraCadastrada = date.datetime.now()
    dataHoraCadastrada = dataHoraCadastrada.strftime('%d/%m/%Y %H:%M:%S')
    dataEHora.append(dataHoraCadastrada) 
