# importacao de biblioteca
import pandas as pd

# criacao de funcao
def definir_data(data_inicio, data_fim, paginacao_maxima):
  """
  Função para definir datas de começo e fim da coleta.
  Também exige que a paginação máxima seja informada.
  
  Parâmetros obrigatórios:
    1) Data de início (string)
    2) Data do início (string)
    3) Paginação máxima (int)
  """
  url_list = []
  link = f'https://www.camara.leg.br/agenda/?dataInicial__proxy={data_inicio}&dataInicial={data_inicio}&dataFinal__proxy={data_fim}&dataFinal={data_fim}&categorias=Plen%C3%A1rio&pagina='
  for indice in range(1, paginacao_maxima + 1):
    url = link + str(indice)
    #print(url)
    url_list.append(url)
    print(url)
  url_list = {'url': url_list}
  url_list = pd.DataFrame(url_list)
  url_list.to_csv("data/url_list.csv", encoding='utf-8', index = False)
