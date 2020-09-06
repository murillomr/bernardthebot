import telepot
import TV

arq = open('thebot', 'r')
tokenapi = arq.read()
# print(tokenapi)
arq.close()

bot = telepot.Bot(tokenapi)
resposta = bot.getUpdates()
#print(resposta)
# bot.sendMessage(21457221, 'opa')


class CanaisFav:
    @classmethod
    def Globo(cls):
        TV.MostraProgramas.CanalGlobo()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    @classmethod
    def Globosat(cls):
        TV.MostraProgramas.CanalGlobosat()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    @classmethod
    def Globonews(cls):
        TV.MostraProgramas.CanalGlobonews()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    @classmethod
    def Multishow(cls):
        TV.MostraProgramas.CanalMultishow()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    @classmethod
    def Mtv(cls):
        TV.MostraProgramas.CanalMTV()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    @classmethod
    def FoodNetwork(cls):
        TV.MostraProgramas.CanalFoodNetwork()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    @classmethod
    def AnimalPlanet(cls):
        TV.MostraProgramas.CanalAnimalPlanet()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    @classmethod
    def TLC(cls):
        TV.MostraProgramas.CanalTLC()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    @classmethod
    def DiscoveryHEM(cls):
        TV.MostraProgramas.CanalDiscoveryHEM()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    @classmethod
    def DiscoverySCI(cls):
        TV.MostraProgramas.CanalDiscoverySCI()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    @classmethod
    def NatGeo(cls):
        TV.MostraProgramas.CanalNatGeo()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    @classmethod
    def Discovery(cls):
        TV.MostraProgramas.CanalDiscovery()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    @classmethod
    def History(cls):
        TV.MostraProgramas.CanalHistory()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    @classmethod
    def DiscWorld(cls):
        TV.MostraProgramas.CanalDiscWorld()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

class CanaisSport():
    @classmethod
    def Sportv1(cls):
        TV.MostraProgramas.CanalSporTV()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    @classmethod
    def Sportv2(cls):
        TV.MostraProgramas.CanalSporTV2()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()


    @classmethod
    def Sportv3(cls):
        TV.MostraProgramas.CanalSporTV3()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()


    @classmethod
    def FoxSports(cls):
        TV.MostraProgramas.CanalFoxSports()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()


    @classmethod
    def FoxSports2(cls):
        TV.MostraProgramas.CanalFoxSports2()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()


    @classmethod
    def TNT(cls):
        TV.MostraProgramas.CanalTNT()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()


    @classmethod
    def EspnBR(cls):
        TV.MostraProgramas.CanalEspnBR()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()


    @classmethod
    def Espn(cls):
        TV.MostraProgramas.CanalEspn()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()


    @classmethod
    def Premiere1(cls):
        TV.MostraProgramas.CanalPremiere1()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()


    @classmethod
    def Premiere2(cls):
        TV.MostraProgramas.CanalPremiere2()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()


    @classmethod
    def Premiere3(cls):
        TV.MostraProgramas.CanalPremiere3()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()


    @classmethod
    def Premiere4(cls):
        TV.MostraProgramas.CanalPremiere4()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()


    @classmethod
    def Premiere5(cls):
        TV.MostraProgramas.CanalPremiere5()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()


    @classmethod
    def Premiere6(cls):
        TV.MostraProgramas.CanalPremiere6()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()


    @classmethod
    def Premiere7(cls):
        TV.MostraProgramas.CanalPremiere7()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()



# funcoes para executar todos comandos dos canais favoritos


# verifica o bot recebeu alguma mensagem
# caso nao, nada acontece.
# caso sim, verifica se a formatacao esta correta e as respostas sao enviadas para o usuario
# Um (1) eh acrescido ao identificador para o bot apagar a mensagem recebida anteriormente
# e depois eh chamada as funcoes que envia a requisicao para obter a grade de programacao
# e eh chamada as funcoes que obtem informacoes de cada canal

if resposta == []:
    pass
else:
    #print("teste else")
    #print(resposta)
    identificador = resposta[0]['update_id']
    #print(identificador)
    texto = resposta[0]['message']
    #print(texto)
    texto = texto['text']
    #print(texto)
    if type(identificador) == int:
        identificador = identificador + 1
        #print(identificador)
        bot.getUpdates(offset=identificador)
        TV.MostraProgramas.Requisicao()
        if not texto.isdigit():
            CanaisFav.Globo()
            CanaisFav.Globosat()
            CanaisFav.Globonews()
            CanaisFav.Multishow()
            CanaisFav.Mtv()
            CanaisFav.FoodNetwork()
            CanaisFav.AnimalPlanet()
            CanaisFav.TLC()
            CanaisFav.DiscoveryHEM()
            CanaisFav.DiscoverySCI()
            CanaisFav.NatGeo()
            CanaisFav.Discovery()
            CanaisFav.History()
            CanaisFav.DiscWorld()
        else:
            CanaisSport.Premiere1()
            CanaisSport.Premiere2()
            CanaisSport.Premiere3()
            CanaisSport.Premiere4()
            CanaisSport.Premiere5()
            CanaisSport.Premiere6()
            CanaisSport.Premiere7()
            CanaisFav.Globo()
            CanaisSport.Sportv1()
            CanaisSport.Sportv2()
            CanaisSport.Sportv3()
            CanaisSport.FoxSports()
            CanaisSport.FoxSports2()
            CanaisSport.TNT()
            CanaisSport.Espn()
            CanaisSport.EspnBR()
    else:
        pass
'''
# CanaisFav.Globo()
CanaisFav.Globosat()
CanaisFav.Globonews()
CanaisFav.Multishow()
CanaisFav.Mtv()
CanaisFav.FoodNetwork()
CanaisFav.AnimalPlanet()
CanaisFav.TLC()
CanaisFav.DiscoveryHEM()
CanaisFav.DiscoverySCI()
CanaisFav.NatGeo()
CanaisFav.Discovery()
CanaisFav.History()
'''
