import requests
import json
import TV_montaURL

url = TV_montaURL.Pathtv.MontarURL(0)
# print(url)

# url = 'https://programacao.netcombo.com.br/gatekeeper/exibicao/select?q=id_revel:1_435&callback=callbackShows&json.wrf=callbackShows&wt=json&rows=100000&sort=id_canal%20asc,dh_inicio%20asc&fl=dh_fim%20dh_inicio%20st_titulo%20titulo%20id_programa%20id_canal&fq=dh_inicio:%5B2020-03-28T04:00:00Z%20TO%202020-03-28T05:59:00Z%5D&callback=callbackShows'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
proxies = {"http": "127.0.0.1:8080", "https": "127.0.0.1:8080"}

# com proxy
# resposta = requests.get(url, proxies=proxies, headers=headers, verify=False)

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


# print(itemf)

# lacos criados para buscar os canais
class MostraProgramas:
    #def __init__(self):
        #self.id = id
        #self.programa = programa
        #self.comeco = comeco
        #self.fim = fim

    def Programacao(self):
        for n in itemf:
            id = n['id_canal']
            programa = n['titulo']
            comeco = n['dh_inicio']
            comeco = comeco[:-1][11:]
            fim = n['dh_fim']
            fim = fim[:-1][11:]

            if id == "435":
                canal = "Globo"
                print("CANAL: {0} | {1} - Hora: {2} - {3}".format(canal, programa, comeco, fim))
                tvprogr = "CANAL: {0} | {1} - Hora: {2} - {3}".format(canal, programa, comeco, fim)
            elif id == "922":
                canal = "+Globosat"
                print("CANAL: {0} | {1} - Hora: {2} - {3}".format(canal, programa, comeco, fim))
            elif id == "432":
                canal = "Globonews"
                print("CANAL: {0} | {1} - Hora: {2} - {3}".format(canal, programa, comeco, fim))
            elif id == "450":
                canal = "Multishow"
                print("CANAL: {0} | {1} - Hora: {2} - {3}".format(canal, programa, comeco, fim))
            elif id == "438":
                canal = "Discovery Home & Health"
                print("CANAL: {0} | {1} - Hora: {2} - {3}".format(canal, programa, comeco, fim))
            elif id == "1512":
                canal = "TLC"
                print("CANAL: {0} | {1} - Hora: {2} - {3}".format(canal, programa, comeco, fim))
            elif id == "472":
                canal = "National Geographic"
                print("CANAL: {0} | {1} - Hora: {2} - {3}".format(canal, programa, comeco, fim))
            elif id == "421":
                canal = "Discovery Channel"
                print("CANAL: {0} | {1} - Hora: {2} - {3}".format(canal, programa, comeco, fim))
#            elif id == "407":
#                canal = "Animal Planet"
#                print("CANAL: {0} | {1} - Hora: {2} - {3}".format(canal, programa, comeco, fim))
#            elif id == "2257":
#                canal = "History Channel"
#                print("CANAL: {0} | {1} - Hora: {2} - {3}".format(canal, programa, comeco, fim))
#            elif id == "423":
#                canal = "Discovery SCI"
#                print("CANAL: {0} | {1} - Hora: {2} - {3}".format(canal, programa, comeco, fim))
#            elif id == "456":
#                canal = "MTV"
#                print("CANAL: {0} | {1} - Hora: {2} - {3}".format(canal, programa, comeco, fim))
#            elif id == "952":
#                canal = "FoodNetwork"
#                print("CANAL: {0} | {1} - Hora: {2} - {3}".format(canal, programa, comeco, fim))
        return tvprogr

#canais = MostraProgramas.Programacao(0)
#print(canais)