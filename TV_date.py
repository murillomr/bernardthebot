from datetime import datetime

class Mes:
    def __init__(self, agoram=None, mes=None, verificacaom=None, mesv=None):
        self.agoram = agoram
        self.mes = mes
        self.verificacaom = verificacaom
        self.mesv = mesv

    def Obtermes(self):
        agoram = datetime.now()
        # pega somente mes
        mes = agoram.month
        #  transforma a variavel "hora" de int (inteiro) para str (string) para utilizar o len() - verificacao de tamanho da string
        verificacaom = len(str(mes))
        if verificacaom == 1:
            mesv = "0" + str(mes)
            #print(mesv)
            #return para possibilitar o armazenamento da saida em uma variavel de outro arquivo
            return mesv
        else:
            mesv = str(mes)
            return mesv

class Mesutc:
    def __init__(self, agorautcm=None, mesutc=None, verificautcm=None, mesutcv=None):
        self.agorautcm = agorautcm
        self.mesutc = mesutc
        self.verificautcm = verificautcm
        self.mesutcv = mesutcv
    def Obtermesutc(self):
        # obter hora e data utc - tres horas a frente
        #print(datetime.utcnow())
        agorautcm = datetime.utcnow()
        # pega somente mes
        mesutc = agorautcm.month
        verificautcm = len(str(mesutc))
        if verificautcm == 1:
            mesutcv = "0" + str(mesutc)
            #print(mesutcv)
            # return para possibilitar o armazenamento da saida em uma variavel de outro arquivo
            return mesutcv
        else:
            mesutcv = str(mesutc)
            #print(mesutcv)
            # return para possibilitar o armazenamento da saida em uma variavel de outro arquivo
            return mesutcv

class Dia:
    def __init__(self, agoram=None, dia=None, verificacaom=None, diav=None):
        self.agoram = agoram
        self.dia = dia
        self.verificacaom = verificacaom
        self.diav = diav

    def Obterdia(self):
        # obter hora e data
        #print(datetime.now())
        agoram = datetime.now()
        # pega somente mes
        dia = agoram.day
        #  transforma a variavel "hora" de int (inteiro) para str (string) para utilizar o len() - verificacao de tamanho da string
        verificacaom = len(str(dia))
        if verificacaom == 1:
            diav = "0" + str(dia)
            #print(diav)
            #return para possibilitar o armazenamento da saida em uma variavel de outro arquivo
            return diav
        else:
            diav = str(dia)
            #print(diav)
            # return para possibilitar o armazenamento da saida em uma variavel de outro arquivo
            return diav

class Diautc:
    def __init__(self, agoram=None, dia=None, verificacaom=None, diav=None):
        self.agoram = agoram
        self.dia = dia
        self.verificacaom = verificacaom
        self.diav = diav

    def Obterdia(self):
        agoram = datetime.utcnow()
        # pega somente mes
        dia = agoram.day
        #  transforma a variavel "hora" de int (inteiro) para str (string) para utilizar o len() - verificacao de tamanho da string
        verificacaom = len(str(dia))
        if verificacaom == 1:
            diav = "0" + str(dia)
            #print(diav)
            #return para possibilitar o armazenamento da saida em uma variavel de outro arquivo
            return diav
        else:
            diav = str(dia)
            #print(diav)
            # return para possibilitar o armazenamento da saida em uma variavel de outro arquivo
            return diav

#executar classes e funcoes:
#Mes.Obtermes(0)
#Mesutc.Obtermesutc(0)
