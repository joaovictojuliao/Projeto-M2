
import datetime as date
import pandas as pd

class PesquisaSaude():      
    def inicio(self, pesquisa):
        while pesquisa>2 or pesquisa<1:
            pesquisa=int(input('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - '
              '\nOlá, bem-vindo a pesquisa sobre a "Conscientização da Saúde Mental"'
              '\n---------------- Deseja participar da pesquisa ? ----------------'
              '\n[ 1 ]- Sim'
              '\n[ 2 ]- Nao\n'))
        return pesquisa

    def idadeVerif(self, idade):
        while (idade<18 or idade>140) and idade != 0:
            idade=int(input(f'\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - '
            '\nDigite a idade do entrevistado, lembrando precisa ser maior de idade: '))
        return idade

    def generos(self):
        genero = int(input('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
                '\nDigite o número que corresponde ao gênero do entrevistado: '
                '\n[ 1 ]- Masculino\n[ 2 ]- Feminino\n[ 3 ]- Binário\n[ 4 ]- Outro\nDigite aqui: '))
        while genero<1 or genero>4:
            print('Valor inválido,tente novamente...')
            genero=int(input('Digite o número que corresponde ao seu gênero: '
                '\n[ 1 ]- Masculino\n[ 2 ]- Feminino\n[ 3 ]- Binário\n[ 4 ]- Outro\nDigite aqui: '))
        if genero==1:
            self.genero='Masculino '
            return self.genero
        elif genero==2:
            self.genero='Feminino '
            return self.genero
        elif genero==3:
            self.genero='Binario '
            return self.genero
        elif genero==4:
            self.genero='Outro '
            return self.genero
    
    def quatroPerguntas(self, pergunta1, pergunta2, pergunta3, pergunta4):
        while pergunta1<1 or pergunta1>3:
            print('\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
            pergunta1=int(input('1- Você acha importante cuidar da saúde mental?: '
            '\n[ 1 ]- Sim\n[ 2 ]- Nao\n[ 3 ]- Nao sei responder\n'))
            if pergunta1==1:
                self.resposta1='Sim '
            elif pergunta1==2:
                self.resposta1='Nao '
            elif pergunta1==3:
                self.resposta1='Nao sei responder '
            else:
                print('Resposta inválida')

        while pergunta2<1 or pergunta2>3:
            print('\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
            pergunta2=int(input('2- Você sabe qual a utilidade do acompanhamento psicológico?: '
            '\n[ 1 ]- Sim\n[ 2 ]- Nao\n[ 3 ]- Nao sei responder\n'))
            if pergunta2==1:
                self.resposta2='Sim '
            elif pergunta2==2:
                self.resposta2='Nao '
            elif pergunta2==3:
                self.resposta2='Nao sei responder '
            else:
                print('Resposta inválida')

        while pergunta3<1 or pergunta3>3:
            print('\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
            pergunta3=int(input('3- Você sente a necessidade de ter acompanhamento psicológico?: '
            '\n[ 1 ]- Sim\n[ 2 ]- Nao\n[ 3 ]- Nao sei responder\n'))
            if pergunta3==1:
                self.resposta3='Sim '
            elif pergunta3==2:
                self.resposta3='Nao '
            elif pergunta3==3:
                self.resposta3='Nao sei responder '
            else:
                print('Resposta invalida')

        while pergunta4<1 or pergunta4>3:
            print('\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
            pergunta4=int(input('4- Você possui acompanhamento psicológico?: '
            '\n[ 1 ]- Sim\n[ 2 ]- Nao\n[ 3 ]- Nao sei responder\n'))
            if pergunta4==1:
                self.resposta4='Sim '
            elif pergunta4==2:
                self.resposta4='Nao '
            elif pergunta4==3:
                self.resposta4='Nao sei responder '
            else:
                print('Resposta inválida')
        return self.resposta1, self.resposta2, self.resposta3, self.resposta4
    
     def dataHora(self):
        dataHoraCadastrada = date.datetime.now()
        dataHoraCadastrada = dataHoraCadastrada.strftime('%d/%m/%Y %H:%M:%S')
        return dataHoraCadastrada

    def arquivoCsv(self, dict):
        df = pd.DataFrame(dict)
        df.to_csv("perguntas.csv", index = False, sep =',')
        print('****Foi criado um arquivo (perguntas.csv) com as informações obtidas!****' 
        '\n- - - - - - - - Obrigado por participar da nossa pesquisa - - - - - - - -\n\n\n')
    
