import telepot
import TV

arq = open('thebot', 'r')
tokenapi = arq.read()
# print(tokenapi)
arq.close()

bot = telepot.Bot(tokenapi)
resposta = bot.getUpdates()
print(resposta)

#identificador = resposta[0]['update_id']
#print(identificador)

#Pega Offset atual
arqoff = open('offset.txt', 'r')
offsetvalor = arqoff.read()
print(offsetvalor)

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

#CanaisFav.Globo()
'''
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