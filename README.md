# ausencia_congresso
repositório criado como projeto final das disciplinas "pensamento computacional" e "transparência, reprodutibilidade e uso ético dos dados", no master do insper

- a escolha por ``selenium`` ocorreu porque eu acredito que esta é uma das vantagens em usar Python
- e, por isso, gostaria de ganhar mais fluência ao usar essa biblioteca
- ao desenvolver os scripts, a Câmara passou a atrapalhar o acesso da máquina com ``HTTP ERROR 431``

#### câmara dos deputados
- hoje, a API da Câmara não informa os deputados ausentes nas votações nominais
- tal demanda já foi apresentada como sugestão administrativa via Lei de Acesso à Informação
- também foi reforçada, com apoio de outro usuário, [via issue no GitHub](https://github.com/CamaraDosDeputados/dados-abertos/issues/312) e [já havia sido cobrada por outras pessoas antes](https://github.com/CamaraDosDeputados/dados-abertos/issues/302)
- para ter o resultado nominal com todos os deputados em exercício, hoje é necessário raspar o HTML da Casa ([exemplo aqui](https://www.camara.leg.br/presenca-comissoes/votacao-portal?reuniao=63176&itemVotacao=10127)) ou baixar um arquivo DBF
- sem essa funcionalidade API, a obtenção desses dados se torna mais manual
- o objetivo desses scripts e automatizar o acesso aos dados completos (ou seja, com os ausentes) das votações nominais

#### senado federal
- hoje, a API do Senado informa os deputados ausentes nas votações nominais
- por isso, neste caso, não faremos uma raspagem, e sim usaremos a API
- o objetivo dos scripts é facilitar o acesso aos ausentes das votações

