# importacao de funcoes criadas apartadas
from cd_periodo import definir_data
from cd_evento import coletar_eventos
from cd_filtro import filtrar_deliberativa
from cd_votacao import pegar_id_votacao
from cd_links import definir_link_nominal
from cd_votos import coletar_votos

####### DEFINICAO DO PERIODO/TEMPO
# parâmetros:
# - data inicio
# - data fim
# - paginacao maxima
definir_data("01/02/2020", "01/07/2020", 7)

####### COLETA DAS ATIVIDADES NO PLENARIO
coletar_eventos()

###### FILTRO POR SESSAO DELIBERATIVA
filtrar_deliberativa()

###### COLETA DO ID DE CADA VOTACAO
pegar_id_votacao()

###### CRIACAO DE URL DE VOTACAO NOMINAL
definir_link_nominal()

###### COLETA DOS DADOS DE VOTACOES
coletar_votos()
