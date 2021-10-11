# importacao de bibliotecas
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# criacao de funcao
def coletar_eventos():
  """
  Função para coletar os eventos realizados no plenário da Câmara dos Deputados.
  Exemplos de eventos: sessão deliberativa, sessão não deliberativa, sessão solene, sessão conjunta etc
  """
  url_list = pd.read_csv("data/url_list.csv")
  url_list = url_list['url'].tolist()

  data_all = []
  hora_all = []
  local_all = []
  atividade_all = []
  link_all = []
  indice_all = []
  url_original = []
  
  browser = webdriver.Chrome(ChromeDriverManager().install())
  
  for url in range(0,len(url_list)):
    browser.get(url_list[url])
    eventos = browser.find_elements_by_xpath('//a[@class="g-agenda__nome"]')
    data = browser.find_elements_by_xpath('//span[@class="g-agenda__data"]')
    hora = browser.find_elements_by_xpath('//span[@class="g-agenda__hora"]')
    local = browser.find_elements_by_xpath('//span[@class="g-agenda__categoria"]')
    atividade = browser.find_elements_by_xpath('//a[@class="g-agenda__nome"]')
    link = browser.find_elements_by_xpath('//a[@class="g-agenda__nome"]')
    time.sleep(3)
    for evento in range(0, len(eventos)):
      data_all.append(data[evento].text)
      print(data_all)
      hora_all.append(hora[evento].text)
      local_all.append(local[evento].text)
      atividade_all.append(atividade[evento].text)
      link_all.append(link[evento].get_attribute("href"))
      indice_all.append(evento)
      url_original.append(url_list[url])
      #print(url_list[url])

  dados_eventos = {'data': data_all, 'hora': hora_all, 'local': local_all, 'atividade': atividade_all, 'link': link_all, 'url_original': url_original}

  urls_eventos_plenario = pd.DataFrame(dados_eventos)
  browser.quit()

  #print(urls_eventos_plenario)
  urls_eventos_plenario.to_csv('data/urls_eventos_plenario.csv', encoding='utf-8', index = False)
