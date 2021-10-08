# importacao de bibliotecas
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# criacao de funcao
def coletar_votos():
  """
  Função para acessar cada URL de votação nominal.
  E coletar os votos, nome de deputado, partido e uf.
  """
  # import CSV scraped with def definir_link_nominal()
  urls_finais = pd.read_csv("data/urls_finais.csv")
  
  # criando listas vazias para o append
  link_all = []
  nome_all = []
  partido_all = []
  voto_all = []
  
  # loop para definir URL
  # e depois loop para e entrar no li
  # e pegar os spans definidos
  for url in range(0, len(urls_finais['link_final'].tolist())):
    #print(url)
    page = requests.get(urls_finais['link_final'].tolist()[0])
    soup = BeautifulSoup(page.text, 'html.parser')
    div = soup.find('div', {'class': 'titulares'})
    link = urls_finais['link_final'].tolist()[url]
    time.sleep(3)
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
