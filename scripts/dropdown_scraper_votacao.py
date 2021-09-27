#################################################
###       SCRAPER PARA O DROPDOWN MENU        ###
#################################################
# importacao de bibliotecas
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())

# import CSV scraped with sessao_deliberativa_cd_2.csv
url_votacao = pd.read_csv("data/urls_votacao_cd.csv")

# coluna com urls para webscraping
url_scraper = url_votacao['final_url']

# lista vazia para receber dados
option_value = []
link_votacao = []

# loop para acessar URL e pegar o 'value' do option
for link in range(0,len(url_scraper.tolist())):
  browser.get(url_scraper[link])
  dropdown_options = browser.find_elements_by_xpath('//select[@id="dropDownReunioes"]/option')
  for element in range(0, len(dropdown_options)):
    link_votacao.append(url_scraper[link])
    option_value.append(dropdown_options[element].get_attribute("value"))
  
browser.quit()
# inserindo dados em um dicionario
dados = {'link': link_votacao, 'option': option_value}

# transformando em dataframe
urls_finais = pd.DataFrame(dados)
#print(urls_finais)

# download do dataframe
urls_finais.to_csv('data/df.csv', encoding='utf-8', index = False)
