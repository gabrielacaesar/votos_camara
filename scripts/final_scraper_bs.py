######### BEAUTIFUL SOUP ######### 
# importacao de bibliotecas
import requests
from bs4 import BeautifulSoup
import pandas as pd

# import CSV scraped with dropdown_scraper_votacao.py
urls_finais = pd.read_csv("data/urls_finais_1.csv")

### OBS: ACRESCENTAR O QUERY CONTAINS PARA NOMINAL
print(urls_finais)
# criando a URL especifica de cada item do dropdown
urls_finais['link_final'] = urls_finais.apply(lambda row: row.link + '&itemVotacao=' +  str(row.option), axis = 1)
urls_finais = urls_finais['link_final']

# criando listas vazias para o append
url_all = []
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
  for li in div.find_all('li'):
    url_all.append(url)
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
    print(f'{nome_all} - {partido_all} - {voto_all} - {url_all}')
        
dados = {'nome': nome_all, 'partido': partido_all, 'voto': voto_all, 'url': url_all}
print(dados)

dados_finais = pd.DataFrame(dados)
dados_finais.to_csv('data/dados_finais_SOAP.csv', encoding='utf-8', index = False)

