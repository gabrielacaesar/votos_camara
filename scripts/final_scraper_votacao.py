#################################################
###    SCRAPER PARA OS DADOS DA VOTAÇÃO       ###
#################################################
# importacao de bibliotecas
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())

# import CSV scraped with dropdown_scraper_votacao.csv
urls_finais = pd.read_csv("data/urls_finais_1.csv")

# criando a URL especifica de cada item do dropdown
urls_finais['link_final'] = urls_finais.apply(lambda row: row.link + '&itemVotacao=' +  str(row.option), axis = 1)
urls_finais = urls_finais['link_final']
#print(urls_finais['link_final'])
#urls_finais.to_csv("data/urls_finais_2.csv", encoding='utf-8', index = False)

##### EM DESENVOLVIMENTO
# OBS: add 'tituloNomePauta' no scraper

link_votacao = []
li_itens = []
#nome_itens = []
#partido_uf_itens = []
#voto_itens = []

for link in range(0,len(urls_finais.tolist())):
  browser.get(urls_finais[link])
  ul_itens = browser.find_elements_by_xpath('//div[@class="titulares"]/ul')
  for li_item in range(0, len(ul_itens)):
    link_votacao.append(urls_finais[link])
    li_itens.append(ul_itens[li_item].text)

dados = {'link': link_votacao, 'option': li_itens}
# 'nome': nome_itens, 'partido_uf': partido_uf_itens, 'voto': voto_itens
print(dados)

dados_finais = pd.DataFrame(dados)
dados_finais.to_csv('data/dados_finais.csv', encoding='utf-8', index = False)

browser.quit()
