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

teste_url = ['https://www.camara.leg.br/presenca-comissoes/votacao-portal?reuniao=59536&itemVotacao=28492']

link_votacao = []
nome_votacao = []
nome_deputado = []
partido_deputado = []
voto_deputado = []
# urls_finais.tolist()

for link in range(0, len(teste_url)):
  browser.get(teste_url[link])
  h4_titulo = browser.find_elements_by_xpath('//h4[@class="tituloNomePauta"]')
for li_item in range(0, len(teste_url)):
  li_itens = browser.find_elements_by_xpath('//div[@class="titulares"]/ul/li')
  nome = browser.find_elements_by_xpath('//span[@class="nome"]')
  partido_uf = browser.find_elements_by_xpath('//span[@class="nomePartido"]')
  voto = browser.find_elements_by_xpath('//span[@class="votou"]')
  for span_item in range(0, len(li_itens)):
    nome_votacao.append(h4_titulo[link].text)
    link_votacao.append(teste_url[link])
    nome_deputado.append(nome[span_item].text)
    partido_deputado.append(partido_uf[span_item].text)
    #print(f'{nome[span_item].text} - {partido_uf[span_item].text}')
    if len(li_itens) > 3:
      voto_deputado.append(voto[span_item].text)
      #print(voto[span_item].text)
    else:
      voto_deputado.append("Ausente")
      #print(voto_deputado)
      print(f'{nome_deputado} - {partido_deputado} - {voto_deputado}')
      
dados = {'link_votacao': link_votacao, 
'nome_votacao': nome_votacao,
'nome_deputado': nome_deputado, 
'partido_deputado' : partido_deputado,
'voto_deputado': voto_deputado}
#

print(dados)

dados_finais = pd.DataFrame(dados)
dados_finais.to_csv('data/dados_finais_TESTE.csv', encoding='utf-8', index = False)

browser.quit()
