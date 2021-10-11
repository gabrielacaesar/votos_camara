# importacao de bibliotecas
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
  
# criacao de funcao
def pegar_id_votacao():
  """
  Função para coletar o id de cada votação no dropdown menu de cada URL.
  """
  # import CSV scraped with def filtrar_deliberativa()
  url_votacao = pd.read_csv("data/url_votacao.csv")
  
  # coluna com urls para webscraping
  url_scraper = url_votacao['url']
  
  # lista vazia para receber dados
  link_votacao = []
  option_value = []
  option_name = []
  
  # run webdriver
  browser = webdriver.Chrome(ChromeDriverManager().install())
  
  # loop para acessar URL e pegar o 'value' do option
  for link in range(0,len(url_scraper.tolist())):
    browser.get(url_scraper[link])
    dropdown_options = browser.find_elements_by_xpath('//select[@id="dropDownReunioes"]/option')
    time.sleep(3)
    for element in range(0, len(dropdown_options)):
      link_votacao.append(url_scraper[link])
      print(url_scraper.tolist()[link])
      option_value.append(dropdown_options[element].get_attribute("value"))
      option_name.append(dropdown_options[element].text)
    
  browser.quit()
  # inserindo dados em um dicionario
  dados = {'link': link_votacao, 'id_option': option_value, 'nome_option': option_name}
  print(dados)
  
  # transformando em dataframe
  id_votacoes = pd.DataFrame(dados)
  #print(id_votacoes)
  
  # download do dataframe
  id_votacoes.to_csv('data/id_votacoes.csv', encoding='utf-8', index = False)
