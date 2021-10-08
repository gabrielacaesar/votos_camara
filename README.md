Repositório criado como projeto final das disciplinas "Pensamento computacional" e "Transparência, reprodutibilidade e uso ético dos dados", no master do Insper.
 
Este repositório tem como objetivo raspar dados de votações nominais do portal da Câmara dos Deputados.

### O que o código faz
- Recebe a data de início e fim da pesquisa e a paginação máxima   
- Gera URLs considerando esses dados
- Acessa os HTMLs dessa pesquisa por atividades no plenário ([Clique aqui](https://www.camara.leg.br/agenda?dataInicial__proxy=01%2F02%2F2020&dataInicial=01%2F02%2F2020&dataFinal__proxy=01%2F07%2F2020&dataFinal=01%2F07%2F2020&categorias=Plen%C3%A1rio) para ver o exemplo de URL)
- Coleta os links de cada atividade no plenário
- Filtra por sessões deliberativas (aquelas que têm votações)
- Acessa os HTMLs de todas as sessões deliberativas ([Clique aqui](https://www.camara.leg.br/presenca-comissoes/votacao-portal?reuniao=59571) para ver o exemplo de URL)
- Coleta o id das votações de cada sessão deliberativa
- Cria URLs específicas para cada votação
- Filtra por votações nominais (aquelas que mostram o voto de cada político)
- Acessa os HTMLs de todas as votações nominais ([Clique aqui](https://www.camara.leg.br/presenca-comissoes/votacao-portal?reuniao=59571&itemVotacao=28979) para ver o exemplo de URL)
- Coleta os dados das votações nominais
- Cria um CSV com os votos de todos os deputados nas votações

![](https://c.tenor.com/pqckQpWm9DIAAAAM/typing-code.gif)

### O que faz cada script
- [Script 1](https://github.com/gabrielacaesar/votos_camara/blob/main/scripts/cd_periodo.py): **cd_periodo.py // definir_data()**           
O código considera os parâmetros informados pelo usuário (data de início, data de fim e paginação máxima) para gerar as URLs a serem percorridas.

- [Script 2](https://github.com/gabrielacaesar/votos_camara/blob/main/scripts/cd_evento.py): **cd_evento.py // coletar_eventos()**        
O código acessa cada URL e coleta os seguintes dados: data, hora, local, nome do evento e link do evento. Ele coloca tais dados em um dicionário e o transforma em um dataframe para fazer o download em CSV. Output (arquivo gerado): urls_eventos_plenario.csv

- [Script 3](https://github.com/gabrielacaesar/votos_camara/blob/main/scripts/cd_filtro.py): **cd_filtro.py // filtrar_deliberativa()**    
O código padroniza a coluna 'atividade e filtra considerando as colunas 'atividade' e 'link'. O objetivo é manter apenas votações deliberativas da Câmara dos Deputados. Output esperado (arquivo gerado): url_votacao.csv

- [Script 4](https://github.com/gabrielacaesar/votos_camara/blob/main/scripts/cd_votacao): **cd_votacao.py // pegar_id_votacao()**    
O código acessa cada URL e coleta o id do menu dropdown de cada votação. Output esperado (arquivo gerado): id_votacoes.csv

- [Script 5](https://github.com/gabrielacaesar/votos_camara/blob/main/scripts/cd_links.py): **cd_links.py // definir_link_nominal()**    
O código gera as URLs únicas de cada votação e filtra por votações nominais. Output esperado (arquivo gerado): urls_finais.csv

- [Script 6](https://github.com/gabrielacaesar/votos_camara/blob/main/scripts/cd_votos.py): **cd_votos.py // coletar_votos()**    
O código acessa cada URL e coleta os dados de cada votação nominal: nome do deputado, partido do deputado, UF do deputado e voto. Casa não haja voto, o robô coloca "Ausente". Output esperado (arquivo gerado): dados_finais.csv

- [Script 7](https://github.com/gabrielacaesar/votos_camara/blob/main/scripts/script-final.py): **script-final.py**   
O código chama todas as funções acima mencionadas e informa os parâmetros da função definir_data() do script cd_periodo. 

### Por que usamos ``Selenium``
- A escolha por ``Selenium`` ocorreu porque eu acredito que esta é uma das vantagens em usar Python
- E, por isso, gostaria de ganhar mais fluência ao usar essa biblioteca
- Mas também usamos ``Beautiful Soup`` e ``requests`` 
- Ao desenvolver os scripts com ``rvest`` no R, a Câmara passou a atrapalhar o acesso da máquina com ``HTTP ERROR 431``
- Posteriormente, foi encontrada uma forma de driblar o problema
- Mas, ainda assim, havia um interesse em mexer com a automatização de browser, com ``Selenium``

### Por que raspamos o site da Câmara
- Hoje, a API da Câmara não informa os deputados ausentes nas votações nominais       
- Apenas para comparar: a API do Senado informa os ausentes           
- Tal demanda já foi apresentada como sugestão administrativa via Lei de Acesso à Informação para a Câmara           
- Também foi reforçada, com apoio de outro usuário, [via issue no GitHub](https://github.com/CamaraDosDeputados/dados-abertos/issues/312) e [já havia sido cobrada por outras pessoas antes](https://github.com/CamaraDosDeputados/dados-abertos/issues/302)
- Para ter o resultado nominal com todos os deputados em exercício, hoje é necessário raspar o HTML da Casa ([exemplo aqui](https://www.camara.leg.br/presenca-comissoes/votacao-portal?reuniao=63176&itemVotacao=10127)) ou baixar um arquivo DBF
- Os arquivos DBF, porém, pararam de ser atualizados em determinado momento da pandemia, com a adoção do modelo de votação virtual
- Sem essa funcionalidade na API, a obtenção desses dados se torna mais manual e custosa
- O objetivo desses scripts é automatizar o acesso aos dados completos (ou seja, com os ausentes) das votações nominais

### Como você pode rodar o código na sua máquina
- Verifique se você tem o Python na sua máquina     
- Verifique a versão do seu Chrome e baixe o [ChromeDriver](https://chromedriver.chromium.org/downloads)       
- Faça o download do repositório na sua máquina     
- Use o terminal para rodar os scripts    
- Rode o arquivo ``script-final.py``, que chama as funções      

### Instruções
Trabalho individual.

Objetivo: criar um programa que executa um processo de ETL - Extract, Transform, Load. Essas 3 etapas são a base para programas que lidam com dados e são encontradas em diversos tipos de programas, exemplos:

1)
- EXTRACT: acessa um determinado site, identifica e extrai do HTML apenas dados de interesse. 
- TRASNFORM: faz alguma limpeza nos dados extraídos. 
- LOAD: salva os dados extraídos em uma planilha.

2)
- EXTRACT: abre uma planilha disponibilizada pelo usuário. 
- TRANSFORMA: manipula a planilha, limpando dados e/ou fazendo análises. 
- LOAD: salva o resultado em um banco de dados.

Você não precisa se limitar aos exemplos acima, desde que existam essas etapas em seu programa.

O programa deve resolver um problema prático do dia-a-dia jornalístico, porém não é necessário que ele execute todo o processo de automação (exemplo: caso você queria coletar uma informação, limpá-la, gerar uma planilha e enviá-la por email, a parte de envio por email não precisa fazer parte do trabalho).

Bibliotecas que não foram vistas durante a disciplina podem ser utilizadas (porém você precisará explicar para que serve e por que a utilizou).

Dica: crie funções para separar as etapas de seu programa e, caso seja útil, crie uma classe com métodos que executam as etapas ETL.

#### Apresentação
- O código deverá ser enviado pelo Blackboard
- A apresentação do trabalho será feita na aula do dia 08/10/2021 e deverá durar de 3 a 5 minutos, consistindo de:
- Explicação do problema/objetivo do programa
- Mostrar principais partes do código e motivação pelas decisões tomadas (por que criou/não criou funções, por que usou as bibliotecs que usou etc.)
- A entrega final será até dia 11/10/2021, porém o envio até a aula do dia 08/10 é encorajado, pois conseguiremos ver a evolução do trabalho. Se o trabalho não for apresentado em aula, o aluno precisará gravar vídeo de 10 minutos com a explicação detalhada (mais detalhada do que seria em aula, explicando linha-a-linha do código).
