Repositório criado como projeto final das disciplinas "Pensamento computacional" e "Transparência, reprodutibilidade e uso ético dos dados", no master do Insper

### Por que usamos ``Selenium``
- a escolha por ``selenium`` ocorreu porque eu acredito que esta é uma das vantagens em usar Python
- e, por isso, gostaria de ganhar mais fluência ao usar essa biblioteca
- ao desenvolver os scripts com ``rvest`` no R, a Câmara passou a atrapalhar o acesso da máquina com ``HTTP ERROR 431``

### O que os scripts fazem
- Acessa os HTMLs de atividades no plenário
- Coleta os links de atividades no plenário
- Filtra por sessões deliberativas (aquelas que têm votações)
- Acessa os HTMLs de todas as sessões deliberativas
- Coleta o número das votações nominais de cada sessão deliberativa
- Cria URLs específicas para cada votação nominal
- Acessa os HTMLs de todas as votações nominais
- Coleta os dados das votações nominais
- Cria um CSV com os votos de todos os deputados nas votações

### Por que raspamos o site da Câmara
- hoje, a API da Câmara não informa os deputados ausentes nas votações nominais
- tal demanda já foi apresentada como sugestão administrativa via Lei de Acesso à Informação
- também foi reforçada, com apoio de outro usuário, [via issue no GitHub](https://github.com/CamaraDosDeputados/dados-abertos/issues/312) e [já havia sido cobrada por outras pessoas antes](https://github.com/CamaraDosDeputados/dados-abertos/issues/302)
- para ter o resultado nominal com todos os deputados em exercício, hoje é necessário raspar o HTML da Casa ([exemplo aqui](https://www.camara.leg.br/presenca-comissoes/votacao-portal?reuniao=63176&itemVotacao=10127)) ou baixar um arquivo DBF
- os arquivos DBF, porém, pararam de ser atualizados em determinado momento da pandemia, com a adoção do modelo de votação virtual
- sem essa funcionalidade na API, a obtenção desses dados se torna mais manual e custosa
- o objetivo desses scripts é automatizar o acesso aos dados completos (ou seja, com os ausentes) das votações nominais

### O que faz cada script
- [Script 1](https://github.com/gabrielacaesar/ausencia_congresso/blob/main/scripts/evento_cd.py):evento_cd.py
O código entra na URL citada, que faz uma busca por eventos no plenário da Câmara desde 01/02/2020 (início da atual legislatura) até hoje (04/10/2021). Em cada URL, ele coleta os seguintes dados: data, hora, local, nome do evento e link do evento. Ele coloca tais dados em um dicionário e o transforma em um dataframe para fazer o download em CSV.

- [Script 2](https://github.com/gabrielacaesar/ausencia_congresso/blob/main/scripts/dropdown_scraper_votacao.py)
O código lê o arquivo CSV gerado pelo script anterior e considera a coluna com as urls para gerar o loop. Na iteração, o robô coleta os dados do menu dropdown, como nome da votação e id da votação. Depois, ele cria um dicionário e o transforma em dataframe para, enfim, baixá-lo como CSV.

- [Script 3](https://github.com/gabrielacaesar/ausencia_congresso/blob/main/scripts/final_scraper_bs.py)
O código lê o arquivo CSV gerado pelo script anterior (id_votacoes.csv). Ele considera a coluna 'id_option' e 'link' para criar uma coluna nova chamada 'link_final'. Depois, ele coloca a coluna 'nome_option' em caixa alta e sem acento para aplicar um filtro caso detecte a palavra 'NOMINAL'. Por fim, ele considera a coluna 'link_final' para fazer um loop e coletar os dados de cada votação nominais: nome do deputado, partido do deputado, UF do deputado e voto. Casa não haja voto, o robô coloca "Ausente". Por fim, ele cria um dicionário e o transforma em dataframe para, enfim, baixá-lo como CSV.

### Como você pode rodar o código na sua máquina
xxxx

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
