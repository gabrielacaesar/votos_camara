from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# import CSV scraped with evento_cd.py
df = pd.read_csv("df.csv")

# padronizacao da coluna, filtro por deliberativa e por link do portal da cd
df['evento'] = df['evento'].str.upper().str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

filtro_evento = df['evento'].str.contains("SESSAO DELIBERATIVA")
filtro_link = df['link'].str.contains("camara.leg.br")

df2 = df.loc[filtro_evento]
df2 = df2.loc[filtro_link]

#df2.to_csv('df2.csv', encoding='utf-8', index = False)
#sessao_deliberativa.to_csv('dados_n.csv', encoding='utf-8', index = False)

urls_deliberativa = df2['link'].tolist()

print(urls_deliberativa)
#url_deliberativa.to_csv('url_deliberativa.csv', encoding='utf-8', index = False)

browser = webdriver.Chrome(ChromeDriverManager().install())

href_votacoes = []

for url in range(0,len(urls_deliberativa)):
  browser.get(urls_deliberativa[url])
  a_votacao = browser.find_elements_by_xpath('//a[@class="links-adicionais__link-votacao"]')
  for href in range(0, len(a_votacao)):
   href_votacoes.append(url[href].get_attribute("href"))
    
urls = {'url': href_votacoes}
urls_votacoes = pd.DataFrame(href_votacoes)

urls_votacoes.to_csv('urls_votacoes.csv', encoding='utf-8', index = False)
