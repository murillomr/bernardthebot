from datetime import datetime

class Hora:
    def __init__(self, agora=None, hora=None, verificacao=None, horav=None):
        self.agora = agora
        self.hora = hora
        self.verificacao = verificacao
        self.horav = horav

    def Obterhora(self):
        agora = datetime.now()
        hora = agora.hour
        hora = hora - 1
        verificacao = len(str(hora))
        if verificacao == 1:
            horav = "0" + str(hora)
            return horav
        else:
            horav = str(hora)
            return horav

class Horautc:
    def __init__(self, agorautc=None, horautc=None, verificautc=None, horautcv=None):
        self.agorautc = agorautc
        self.horautc = horautc
        self.verificautc = verificautc
        self.horautcv = horautcv
    def Obterhorautc(self):
        agorautc = datetime.utcnow()
        # pega somente hora
        horautc = agorautc.hour
        verificautc = len(str(horautc))
        if verificautc == 1:
            horautcv = "0" + str(horautc)
            #print(horautcv)
            # return para possibilitar o armazenamento da saida em uma variavel de outro arquivo
            return horautcv
        else:
            horautcv = str(horautc)
            #print(horautcv)
            # return para possibilitar o armazenamento da saida em uma variavel de outro arquivo
            return horautcv

class Minuto:
    def __init__(self, agora=None, minuto=None, verificacao=None, minutov=None):
        self.agora = agora
        self.minuto = minuto
        self.verificacao = verificacao
        self.minutov = minutov

    def Obterminuto(self):
        # obter hora e data
        #print(datetime.now())
        agora = datetime.now()
        # pega somente hora
        minuto = agora.minute
        #  transforma a variavel "hora" de int (inteiro) para str (string) para utilizar o len() - verificacao de tamanho da string
        verificacao = len(str(minuto))
        if verificacao == 1:
            minutov = "0" + str(minuto)
            #print(minutov)
            # return para possibilitar o armazenamento da saida em uma variavel de outro arquivo
            return minutov
        else:
            minutov = str(minuto)
            #print(minutov)
            # return para possibilitar o armazenamento da saida em uma variavel de outro arquivo
            return minutov

class Minutoutc:
    def __init__(self):
        self.agora = agora
        self.minuto = minuto
        self.verificacao = verificacao
        self.minutov = minutov

    def Obterminuto(self):
        # obter hora e data
        #print(datetime.now())
        agora = datetime.utcnow()
        # pega somente hora
        minuto = agora.minute
        #  transforma a variavel "hora" de int (inteiro) para str (string) para utilizar o len() - verificacao de tamanho da string
        verificacao = len(str(minuto))
        if verificacao == 1:
            minutov = "0" + str(minuto)
            #print(minutov)
            # return para possibilitar o armazenamento da saida em uma variavel de outro arquivo
            return minutov
        else:
            minutov = str(minuto)
            #print(minutov)
            # return para possibilitar o armazenamento da saida em uma variavel de outro arquivo
            return minutov

