# importacao de bibliotecas
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# import CSV scraped with evento_cd.py
df = pd.read_csv("data/df.csv")

# padronizacao da coluna, filtro por deliberativa e por link do portal da cd
df['evento'] = df['evento'].str.upper().str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
filtro_evento = df['evento'].str.contains("SESSAO DELIBERATIVA")
filtro_link = df['link'].str.contains("camara.leg.br")

# aplicacao dos filtros criados acima
url_votacao = df.loc[filtro_evento]
url_votacao = url_votacao.loc[filtro_link]

# criacao de nova coluna 'final_url' usando numero final da coluna 'link'
url_votacao['id'] = url_votacao['link'].apply(lambda x : x.split('/')[-1])
url_votacao['final_url'] = url_votacao.apply(lambda x : 'https://www.camara.leg.br/presenca-comissoes/votacao-portal?reuniao=' + x['id'], axis = 1)

# download de dataframe
url_votacao.to_csv('urls_votacao_cd.csv', encoding='utf-8', index = False)
