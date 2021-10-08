# importacao de biblioteca
import pandas as pd

# criacao de funcao
def filtrar_deliberativa():
  """
  Função para manter apenas votações deliberativas da Câmara dos Deputados.
  Para isso, filtramos pelas colunas 'atividade' e 'link'.
  """
  # import CSV scraped with def coletar_eventos()
  url_eventos = pd.read_csv("data/urls_eventos_plenario.csv")
  
  # padronizacao da coluna, filtro por deliberativa e por link do portal da cd
  url_eventos['atividade'] = url_eventos['atividade'].str.upper().str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
  filtro_evento = url_eventos['atividade'].str.contains("SESSAO DELIBERATIVA")
  filtro_link = url_eventos['link'].str.contains("camara.leg.br")
  
  # aplicacao dos filtros criados acima
  url_votacao = url_eventos.loc[filtro_evento]
  url_votacao = url_votacao.loc[filtro_link]
  
  # criacao de nova coluna 'final_url' usando numero final da coluna 'link'
  url_votacao['id'] = url_votacao['link'].apply(lambda x : x.split('/')[-1])
  url_votacao['url'] = url_votacao.apply(lambda x : 'https://www.camara.leg.br/presenca-comissoes/votacao-portal?reuniao=' + x['id'], axis = 1)
  print(url_votacao)
  
  # coluna com urls para webscraping
  url_votacao['url'].to_csv("data/url_votacao.csv", encoding='utf-8', index = False)

