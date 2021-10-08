# importacao de biblioteca
# importacao de bibliotecas
import pandas as pd

# criacao de funcao
def definir_link_nominal():
  """
  Função para criar o link de cada votação nominal.
  """
  # import CSV scraped with def pegar_id_votacao()
  id_votacoes = pd.read_csv("data/id_votacoes.csv")
  #print(id_votacoes)
  
  # criando a URL especifica de cada item do dropdown
  id_votacoes['link_final'] = id_votacoes.apply(lambda row: row.link + '&itemVotacao=' +  str(row.id_option), axis = 1)
  
  # criando coluna com 'nome_option' em caixa alta
  id_votacoes['nome_option'] = id_votacoes['nome_option'].str.upper().str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
  
  # criando filtro para 'nominal'
  filtro_nominal = id_votacoes['nome_option'].str.contains("NOMINAL")
  urls_finais = id_votacoes.loc[filtro_nominal]
  print(urls_finais)
  
  # criando df com urls para raspagem
  urls_finais['link_final'].to_csv("data/urls_finais.csv", encoding='utf-8', index = False)
  
