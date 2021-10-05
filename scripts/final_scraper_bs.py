###########################################################
###      SCRIPT PARA ACESSAR URL DE VOTAÇÃO NOMINAL     ###
###      E TAMBÉM COLETAR DADOS DE CADA DEPUTADO        ###  
###########################################################
# importacao de bibliotecas
import requests
from bs4 import BeautifulSoup
import pandas as pd

# import CSV scraped with dropdown_scraper_votacao.py
id_votacoes = pd.read_csv("data/id_votacoes.csv")
#print(id_votacoes)

# criando a URL especifica de cada item do dropdown
id_votacoes['link_final'] = id_votacoes.apply(lambda row: row.link + '&itemVotacao=' +  str(row.id_option), axis = 1)

# criando coluna com 'nome_option' em caixa alta
id_votacoes['nome_option'] = id_votacoes['nome_option'].str.upper().str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

# criando filtro para 'nominal'
filtro_nominal = id_votacoes['nome_option'].str.contains("NOMINAL")
urls_finais = id_votacoes.loc[filtro_nominal]
#print(urls_finais)

# criando df com urls para raspagem
urls_finais = urls_finais['link_final']
#print(len(urls_finais.tolist()))

# criando listas vazias para o append
link_all = []
nome_all = []
partido_all = []
voto_all = []

# loop para definir URL
# e depois loop para e entrar no li
# e pegar os spans definidos
for url in range(0, len(urls_finais.tolist())):
  #print(url)
  page = requests.get(urls_finais.tolist()[0])
  soup = BeautifulSoup(page.text, 'html.parser')
  div = soup.find('div', {'class': 'titulares'})
  link = urls_finais.tolist()[url]
  for li in div.find_all('li'):
    link_all.append(link)
    print(link)
    nome = li.find("span", {"class": "nome"}).contents[0]
    nome_all.append(nome)
    #print(nome_all)
    partido = li.find("span", {"class": "nomePartido"}).contents[0]
    partido_all.append(partido)
    #print(partido_all)
    try:
      voto = li.find("span", {"class": ["voto", "sim"]}).contents[0]
      voto_all.append(voto)
    except AttributeError:
        try:
          voto = li.find("span", {"class": ["voto", "nao"]}).contents[0]
          voto_all.append(voto)
        except AttributeError:
          voto = 'Ausente'
          voto_all.append(voto)
    #print(f'{nome_all} - {partido_all} - {voto_all} - {link_all}')
        
dados = {'nome': nome_all, 'partido': partido_all, 'voto': voto_all, 'link': link_all}
print(dados)

dados_finais = pd.DataFrame(dados)
dados_finais.to_csv('data/dados_finais.csv', encoding='utf-8', index = False)
