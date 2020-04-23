import requests
import json
import TV_montaURL

# lacos criados para buscar os canais
class MostraProgramas:

#    def __init__(self, itemf):
#        self.itemf = itemf

    def Requisicao():
        global itemf
        url = TV_montaURL.Pathtv.MontarURL(0)
        # print(url)

        # url = 'https://programacao.netcombo.com.br/gatekeeper/exibicao/select?q=id_revel:1_435&callback=callbackShows&json.wrf=callbackShows&wt=json&rows=100000&sort=id_canal%20asc,dh_inicio%20asc&fl=dh_fim%20dh_inicio%20st_titulo%20titulo%20id_programa%20id_canal&fq=dh_inicio:%5B2020-03-28T04:00:00Z%20TO%202020-03-28T05:59:00Z%5D&callback=callbackShows'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
        proxies = {"http": "127.0.0.1:8080", "https": "127.0.0.1:8080"}

        # com proxy
        #resposta = requests.get(url, proxies=proxies, headers=headers, verify=False)

        # sem proxy
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
        #print(itemf)

    def CanalGlobo():
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
                #print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    def CanalGlobosat():
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
                #print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    def CanalGlobonews():
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
                #print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    def CanalMultishow():
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
                #print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    def CanalMTV():
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
                #print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    def CanalFoodNetwork():
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
                #print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    def CanalAnimalPlanet():
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
                #print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    def CanalTLC():
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
                #print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    def CanalDiscoveryHEM():
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
                #print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    def CanalDiscoverySCI():
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
                #print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    def CanalNatGeo():
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
                #print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    def CanalDiscovery():
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
                #print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()

    def CanalHistory():
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
                #print("{0}: {1} - {2}".format(programa, comeco, fim))
                canalprog = "{0}: {1} - {2}".format(programa, comeco, fim)
                novo = open('temp.txt', 'a')
                novo.write(canalprog + "\n")
                novo.close()
