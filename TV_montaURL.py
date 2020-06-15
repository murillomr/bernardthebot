import TV_date
import TV_hora

#Obtem dia/hora atual e utc (+3)
dia = TV_date.Dia.Obterdia(0)
mes = TV_date.Mes.Obtermes(0)
hora = TV_hora.Hora.Obterhora(0)
minuto = TV_hora.Minuto.Obterminuto(0)
diautc = TV_date.Diautc.Obterdia(0)
mesutc = TV_date.Mesutc.Obtermesutc(0)
horautc = TV_hora.Horautc.Obterhorautc(0)
minutoutc = TV_hora.Minutoutc.Obterminuto(0)

class Pathtv:
    def __init__(self):
        self.pathtv = pathtv
# monta a URL de acordo com a programacao atual ate 3h a frente
    def MontarURL(self):
        pathtv = 'https://programacao.netcombo.com.br/gatekeeper/exibicao/select?q=id_revel:1_1015+id_revel:1_435+id_revel:1_922+id_revel:1_432+id_revel:1_450+id_revel:1_438+id_revel:1_1512+id_revel:1_472+id_revel:1_421+id_revel:1_407+id_revel:1_2257+id_revel:1_423+id_revel:1_456+id_revel:1_952+id_revel:1_1144+&callback=callbackShows&json.wrf=callbackShows&wt=json&rows=100000&sort=id_canal%20asc,dh_inicio%20asc&fl=dh_fim%20dh_inicio%20st_titulo%20titulo%20id_programa%20id_canal&fq=dh_inicio:%5B2020-{0}-{1}T{2}:{3}:00Z%20TO%202020-{4}-{5}T{6}:{7}:00Z%5D&callback=callbackShows'.format(mes, dia, hora, minuto, mesutc, diautc, horautc, minutoutc)
        #print(pathtv)
        return pathtv


#Pathtv.MontarURL(0)