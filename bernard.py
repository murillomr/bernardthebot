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
    def Globo():
        TV.MostraProgramas.CanalGlobo()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    def Globosat():
        TV.MostraProgramas.CanalGlobosat()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    def Globonews():
        TV.MostraProgramas.CanalGlobonews()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    def Multishow():
        TV.MostraProgramas.CanalMultishow()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    def Mtv():
        TV.MostraProgramas.CanalMTV()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    def FoodNetwork():
        TV.MostraProgramas.CanalFoodNetwork()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    def AnimalPlanet():
        TV.MostraProgramas.CanalAnimalPlanet()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    def TLC():
        TV.MostraProgramas.CanalTLC()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    def DiscoveryHEM():
        TV.MostraProgramas.CanalDiscoveryHEM()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    def DiscoverySCI():
        TV.MostraProgramas.CanalDiscoverySCI()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    def NatGeo():
        TV.MostraProgramas.CanalNatGeo()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    def Discovery():
        TV.MostraProgramas.CanalDiscovery()
        arquivo = open('temp.txt', 'r')
        mensagem = arquivo.read()
        bot.sendMessage(21457221, mensagem)
        arquivo.close()

    def History():
        TV.MostraProgramas.CanalHistory()
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
    identificador = resposta[0]['update_id']
    #print(identificador)
    if type(identificador) == int:
        identificador = identificador + 1
        #print(identificador)
        bot.getUpdates(offset=identificador)
        TV.MostraProgramas.Requisicao()
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
