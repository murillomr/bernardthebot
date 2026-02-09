import requests
import json
import TV_montaURL


# lacos criados para buscar os canais
class MostraProgramas:

    #    def __init__(self, itemf):
    #        self.itemf = itemf
    @classmethod
    def Requisicao(cls):
        global itemf
        url = TV_montaURL.Pathtv.MontarURL()
        # print(url)

        # url = 'https://programacao.netcombo.com.br/gatekeeper/exibicao/select?q=id_revel:1_435&callback=callbackShows&json.wrf=callbackShows&wt=json&rows=100000&sort=id_canal%20asc,dh_inicio%20asc&fl=dh_fim%20dh_inicio%20st_titulo%20titulo%20id_programa%20id_canal&fq=dh_inicio:%5B2020-03-28T04:00:00Z%20TO%202020-03-28T05:59:00Z%5D&callback=callbackShows'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
        proxies = {"http": "127.0.0.1:8080", "https": "127.0.0.1:8080"}

        resposta = requests.get(url, headers=headers)

        # print(resposta.content)

        # Remove o início da resposta (callbackShows() e o último caractere da resposta ) - na ideia de formatar um json
        r = resposta.content[:-1][14:]
        # bytes para string JSON
        final = r.decode('utf-8')
        # print(final)

        # transformando JSON em DICIONARIO
        dicio = json.loads(final)
        # print(dicio)

        # entra dentro do dicionario "response"
        itemd = dicio.values()
        # print(itemd)
        # remove a string dict_values( e transforma a saida numa lista
        iteme = list(dicio.values())
        # print(iteme)
        # entra dentro da lista DOCS
        itemf = iteme[0]['docs']
        # print(itemf)

    @classmethod
    def CanalGlobo(cls):
        print("####GLOBO###")
        novo = open('temp.txt', 'w')
        novo.write("### GLOBO ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "435":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalGlobosat(cls):
        print("#### +GLOBOSAT ###")
        novo = open('temp.txt', 'w')
        novo.write("### +GLOBOSAT ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "922":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalGlobonews(cls):
        print("#### GLOBONEWS ###")
        novo = open('temp.txt', 'w')
        novo.write("### GLOBONEWS ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "432":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalMultishow(cls):
        print("####MULTISHOW###")
        novo = open('temp.txt', 'w')
        novo.write("### MULTISHOW ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "450":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalMTV(cls):
        print("####MTV###")
        novo = open('temp.txt', 'w')
        novo.write("### MTV ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "456":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalFoodNetwork(cls):
        print("#### Food Network ###")
        novo = open('temp.txt', 'w')
        novo.write("### Food Network ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "952":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalAnimalPlanet(cls):
        print("#### Animal Planet ###")
        novo = open('temp.txt', 'w')
        novo.write("### Animal Planet ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "407":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalTLC(cls):
        print("#### TLC ###")
        novo = open('temp.txt', 'w')
        novo.write("### TLC ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "1512":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalDiscoveryHEM(cls):
        print("#### Discovery Home & Health ###")
        novo = open('temp.txt', 'w')
        novo.write("### Discovery Home & Health ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "438":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalDiscoverySCI(cls):
        print("#### Discovery Science ###")
        novo = open('temp.txt', 'w')
        novo.write("### Discovery Science ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "423":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalNatGeo(cls):
        print("#### National Geographic ###")
        novo = open('temp.txt', 'w')
        novo.write("### National Geographic ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "472":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalDiscovery(cls):
        print("#### Discovery Channel ###")
        novo = open('temp.txt', 'w')
        novo.write("### Discovery Channel ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "421":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalHistory(cls):
        print("#### History Channel ###")
        novo = open('temp.txt', 'w')
        novo.write("### History Channel ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "2257":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalDiscWorld(cls):
        print("#### Discovery World ###")
        novo = open('temp.txt', 'w')
        novo.write("### Discovery World ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "1144":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalSporTV(cls):
        print("#### SportTV ###")
        novo = open('temp.txt', 'w')
        novo.write("### SporTV ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "1063":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalSporTV2(cls):
        print("#### SportTV2 ###")
        novo = open('temp.txt', 'w')
        novo.write("### SporTV2 ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "1047":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalSporTV3(cls):
        print("#### SportTV3 ###")
        novo = open('temp.txt', 'w')
        novo.write("### SporTV3 ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "1137":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalFoxSports(cls):
        print("#### FoxSports ###")
        novo = open('temp.txt', 'w')
        novo.write("### FoxSports ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "1034":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalFoxSports2(cls):
        print("#### FoxSports2 ###")
        novo = open('temp.txt', 'w')
        novo.write("### FoxSports2 ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "1090":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalTNT(cls):
        print("#### TNT ###")
        novo = open('temp.txt', 'w')
        novo.write("### TNT ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "478":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalEspnBR(cls):
        print("#### ESPN Brasil ###")
        novo = open('temp.txt', 'w')
        novo.write("### ESPN Brasil ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "426":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalEspn(cls):
        print("#### ESPN ###")
        novo = open('temp.txt', 'w')
        novo.write("### ESPN ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "427":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalPremiere1(cls):
        print("#### Premiere1 ###")
        novo = open('temp.txt', 'w')
        novo.write("### Premiere 1 ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "1365":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalPremiere2(cls):
        print("#### Premiere2 ###")
        novo = open('temp.txt', 'w')
        novo.write("### Premiere 2 ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "1360":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalPremiere3(cls):
        print("#### Premiere3 ###")
        novo = open('temp.txt', 'w')
        novo.write("### Premiere 3 ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "1361":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalPremiere4(cls):
        print("#### Premiere4 ###")
        novo = open('temp.txt', 'w')
        novo.write("### Premiere 4 ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "1362":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()


    @classmethod
    def CanalPremiere5(cls):
        print("#### Premiere5 ###")
        novo = open('temp.txt', 'w')
        novo.write("### Premiere 5 ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "1363":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalPremiere6(cls):
        print("#### Premiere6 ###")
        novo = open('temp.txt', 'w')
        novo.write("### Premiere 6 ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "1364":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    @classmethod
    def CanalPremiere7(cls):
        print("#### Premiere7 ###")
        novo = open('temp.txt', 'w')
        novo.write("### Premiere 7 ###" + "\n")
        novo.close()
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]
            if id == "693":
                # print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()


