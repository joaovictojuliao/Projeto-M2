import pandas as pd

class PesquisaSaude():
    def __init__(self, nome, idade, datahora):
        self.nome=nome
        self.idade=idade
        self.datahora=datahora

    def idadeVerif(self, idade):        
        while idade<0 or idade>140:
            idade=int(input("Digite a idade correta do entrevistado, lembrando precisa ser maior de idade: "))
        return idade

    def generos(self):
        genero = int(input('Digite o número que corresponde ao seu gênero: '
                '\n1- Masculino\n2- Feminino\n3- Binário\n4- Outro\nDigite aqui: '))
        while genero<1 or genero>4:
            print('Valor inválido,tente novamente...')
            genero=int(input('Digite o número que corresponde ao seu gênero: '
                '\n1- Masculino\n2- Feminino\n3- Binário\n4- Outro\nDigite aqui: '))
        if genero==1:
            self.genero='Masculino'
            return self.genero
        elif genero==2:
            self.genero='Feminino'
            return self.genero
        elif genero==3:
            self.genero='Binário'
            return self.genero
        elif genero==4:
            self.genero='Outro'
            return self.genero
    
    def quatroPerguntas(self, pergunta1, pergunta2, pergunta3, pergunta4):

        while pergunta1<1 or pergunta1>3:
            pergunta1=int(input('1- Você acha importante cuidar da saúde mental?: '))
            if pergunta1==1:
                self.resposta1='Sim'
            elif pergunta1==2:
                self.resposta1='Não'
            elif pergunta1==3:
                self.resposta1='Não sei responder'
            else:
                print('Resposta inválida')

        while pergunta2<1 or pergunta2>3:
            pergunta2=int(input('2- Você sabe qual a utilidade do acompanhamento psicológico?: '))
            if pergunta2==1:
                self.resposta2='Sim'
            elif pergunta2==2:
                self.resposta2='Não'
            elif pergunta2==3:
                self.resposta2='Não sei responder'
            else:
                print('Resposta inválida')

        while pergunta3<1 or pergunta3>3:
            pergunta3=int(input('3- Você sente a necessidade de ter acompanhamento psicológico?: '))
            if pergunta3==1:
                self.resposta3='Sim'
            elif pergunta3==2:
                self.resposta3='Não'
            elif pergunta3==3:
                self.resposta3='Não sei responder'
            else:
                print('Resposta inválida')

        while pergunta4<1 or pergunta4>3:
            pergunta4=int(input('4- Você possui acompanhamento psicológico?: '))
            if pergunta4==1:
                self.resposta4='Sim'
            elif pergunta4==2:
                self.resposta4='Não'
            elif pergunta4==3:
                self.resposta4='Não sei responder'
            else:
                print('Resposta inválida')

        return self.resposta1, self.resposta2, self.resposta3, self.resposta4
