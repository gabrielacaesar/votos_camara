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

# pegando os dados da URL final
# url = 'https://www.camara.leg.br/presenca-comissoes/votacao-portal?reuniao=59536&itemVotacao=28492'
# browser.get(url)
# dado = browser.find_elements_by_xpath('//div[@class="titulares"]/ul/li')
# print(votos)

teste_urls_finais = ['https://www.camara.leg.br/presenca-comissoes/votacao-portal?reuniao=59536&itemVotacao=28492',
'https://www.camara.leg.br/presenca-comissoes/votacao-portal?reuniao=59536&itemVotacao=28492',
'https://www.camara.leg.br/presenca-comissoes/votacao-portal?reuniao=59542&itemVotacao=28598',
'https://www.camara.leg.br/presenca-comissoes/votacao-portal?reuniao=59542&itemVotacao=28607']

link_votacao = []
span_itens = []
#nome_itens = []
#partido_uf_itens = []
#voto_itens = []

for link in range(0,len(teste_urls_finais)):
  browser.get(teste_urls_finais[link])
  li_itens = browser.find_elements_by_xpath('//div[@class="titulares"]/ul/li')
  #nome = browser.find_elements_by_xpath('//span[@class="nome"]')
  #partido_uf = browser.find_elements_by_xpath('//span[@class="nomePartido"]')
  #voto = browser.find_elements_by_xpath('//span[@class="votou"]')
  for span in range(0, len(li_itens)):
    link_votacao.append(teste_urls_finais[link])
    #nome_itens.append(nome[span].text)
    #partido_uf_itens.append(partido_uf[span].text)
    #voto_itens.append(voto[span].text)
    span_itens.append(li_itens[span].text)

dados = {'link': link_votacao, 'option': span_itens}
# 'nome': nome_itens, 'partido_uf': partido_uf_itens, 'voto': voto_itens
print(dados)

dados_finais = pd.DataFrame(dados)
dados_finais.to_csv('data/dados_finais.csv', encoding='utf-8', index = False)

browser.quit()
