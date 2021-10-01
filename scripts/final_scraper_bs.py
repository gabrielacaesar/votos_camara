######### BEAUTIFUL SOUP ######### 
# importacao de bibliotecas
import requests
from bs4 import BeautifulSoup
import pandas as pd

# link para raspar
page = requests.get('https://www.camara.leg.br/presenca-comissoes/votacao-portal?reuniao=63360&itemVotacao=10160')

# parseando o html
soup = BeautifulSoup(page.text, 'html.parser')

# criando lista vazia para o append
span_all = []

# loop para coleta dos spans
for li in soup.find_all(class_='titulares'):
    for span in li.find_all('span'):
        #print(span.string) 
        span_all.append(span.string)
        #print(span_all)

dados = {'conteudo': span_all}
print(dados)

dados_finais = pd.DataFrame(dados)
dados_finais.to_csv('data/dados_finais_SOAP.csv', encoding='utf-8', index = False)

