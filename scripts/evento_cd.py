########################################################################
###          SCRAPER PARA OS EVENTOS DO PLENÁRIO DA CÂMARA           ###
########################################################################
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())

url_list = list(map('https://www.camara.leg.br/agenda/?dataInicial__proxy=01/02/2020&dataInicial=01/02/2020&dataFinal__proxy=04/10/2021&dataFinal=04/10/2021&categorias=Plen%C3%A1rio&pagina={}'.format, range(1, 26)))
print(url_list)

data_n = []
hora_n = []
local_n = []
evento_n = []
link_n = []
indice_n = []
dados_n = []
url_n = []

for n in range(0,len(url_list)):
  browser.get(url_list[n])
  
  eventos = browser.find_elements_by_xpath('//a[@class="g-agenda__nome"]')
  data = browser.find_elements_by_xpath('//span[@class="g-agenda__data"]')
  hora = browser.find_elements_by_xpath('//span[@class="g-agenda__hora"]')
  local = browser.find_elements_by_xpath('//span[@class="g-agenda__categoria"]')
  evento = browser.find_elements_by_xpath('//a[@class="g-agenda__nome"]')
  link = browser.find_elements_by_xpath('//a[@class="g-agenda__nome"]')
  
  for i in range(0, len(eventos)):
    data_n.append(data[i].text)
    print(data_n)
    hora_n.append(hora[i].text)
    local_n.append(local[i].text)
    evento_n.append(evento[i].text)
    link_n.append(link[i].get_attribute("href"))
    indice_n.append(i)
    #url_n.append(url_list[n])
    print(url_n)

dados = {'data' : data_n, 'hora' : hora_n, 'local' : local_n, 'evento' : evento_n, 'link' : link_n, 'url' : url_n}

urls_eventos_plenario = pd.DataFrame(dados)
browser.quit()

print(urls_eventos_plenario)
urls_eventos_plenario.to_csv('data/urls_eventos_plenario.csv', encoding='utf-8', index = False)
