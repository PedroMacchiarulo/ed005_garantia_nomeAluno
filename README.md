O sistema de Garantia de Notas Fiscais foi estruturado com base em um modelo relacional que reflete o funcionamento real de uma rede de lojas, usuários e produtos com garantias associadas. A seguir, estão descritas as principais relações entre as entidades e a lógica que as fundamenta:

Loja → Equipamentos (1:N):
Cada loja é responsável pela venda ou cadastro de diversos equipamentos. No entanto, cada equipamento pertence exclusivamente a uma única loja, o que estabelece uma relação de um para muitos.

Usuários → Equipamentos (1:N):
Um mesmo usuário (como cliente, técnico ou funcionário) pode estar vinculado a vários equipamentos cadastrados em seu nome. Cada equipamento, porém, pertence a apenas um usuário, mantendo a integridade da relação.

Equipamentos → Garantia (1:1):
Cada equipamento possui uma única garantia ativa associada ao momento da compra. Essa relação de um para um garante que cada item tenha seu próprio registro de garantia, evitando duplicidades ou inconsistências.
(Caso o sistema evolua para permitir renovações de garantia, essa relação poderá ser alterada para 1:N.)

Loja → Garantia (1:N):
Uma loja pode emitir diversas garantias para os produtos que comercializa, mas cada garantia é vinculada a uma única loja emissora, mantendo o controle e a rastreabilidade das garantias emitidas.

Equipamentos → Documentos (1:N):
Um equipamento pode ter vários documentos relacionados (como notas fiscais, certificados e manuais), mas cada documento está associado a apenas um equipamento específico, garantindo organização e referência direta.

Esse modelo de dados assegura coerência lógica, consistência referencial e escalabilidade, permitindo a expansão do sistema sem comprometer a integridade das informações entre lojas, usuários, equipamentos, garantias e documentos.

ON DELETE CASCADE: Entendendo o Conceito
O ON DELETE CASCADE é uma cláusula utilizada em bancos de dados relacionais para gerenciar a integridade referencial entre tabelas. Quando uma linha é excluída de uma tabela pai, essa cláusula automaticamente exclui as linhas relacionadas em tabelas filhas.

Se um cliente é excluído da tabela clientes, todos os pedidos relacionados a esse cliente serão automaticamente excluídos da tabela pedidos.
Quando é Útil?
Simplifica a Manutenção de Dados: Elimina a necessidade de excluir manualmente registros relacionados em tabelas filhas.
Mantém a Integridade Referencial: Garante que não haja registros órfãos em tabelas filhas após a exclusão de um registro na tabela pai.
Útil em Relacionamentos 1:N: Em relacionamentos onde um registro pai tem muitos registros filhos, como pedidos de um cliente.
Quando é Perigoso?
Perda de Dados Importantes: Se não for cuidadosamente planejado, pode levar à exclusão acidental de dados importantes em tabelas filhas.
Dificuldade em Recuperar Dados: Uma vez que os dados são excluídos, pode ser difícil ou impossível recuperá-los, especialmente se não houver backups.
Impacto em Desempenho: Em grandes bancos de dados, a exclusão em cascata pode impactar o desempenho, especialmente se houver muitas tabelas e registros envolvidos.
Boas Práticas
Use com Cuidado: Certifique-se de que a exclusão em cascata seja a ação desejada e que os dados possam ser excluídos sem problemas.
Teste em Ambientes de Desenvolvimento: Antes de aplicar em produção, teste em ambientes de desenvolvimento para garantir que o comportamento seja o esperado.
Mantenha Backups: Sempre mantenha backups regulares do banco de dados para evitar perda de dados importantes.

1. Quais equipamentos estão vinculados a cada loja?
   Notebook Lenovo Ideapad 3 esta vinculado a loja id - 1, nome_loja - Tech Store Niterói.
   Monitor LG 24" esta vinculado a loja id - 1, nome_loja - Tech Store Niterói.
   Impressora HP LaserJet esta vinculado a loja id - 2, nome_loja - Eletrônicos Alpha.
2. Quais garantias vencem nos próximos 30 dias?
   Nenhuma, todas estão com prazo de 1 ano
3. Qual loja possui o maior número de garantias vencidas?
   Ainda nenhuma, tem apenas itens com garantia ativa
4. Qual o tempo médio de garantia por loja?
   1 ano

Consultas e Aplicações
As consultas envolvendo ON DELETE CASCADE podem ser usadas em vários contextos de aplicação, dependendo das necessidades do negócio. Aqui estão alguns exemplos:
Relatórios de Clientes e Pedidos
Consulta: SELECT _ FROM clientes JOIN pedidos ON clientes.id_cliente = pedidos.id_cliente;
Aplicação: Gerar relatórios detalhados sobre os pedidos de cada cliente, incluindo data, valor e status do pedido.
Alertas de Pedidos Pendentes
Consulta: SELECT _ FROM pedidos WHERE id_cliente IN (SELECT id_cliente FROM clientes WHERE status = 'ativo');
Aplicação: Enviar alertas para clientes ativos com pedidos pendentes, incentivando-os a concluir a compra.
Análise de Comportamento do Cliente
Consulta: SELECT COUNT(\*) FROM pedidos WHERE id_cliente = ?;
Aplicação: Analisar o comportamento de compra de um cliente específico, identificando padrões e tendências.
Relatórios de Vendas
Consulta: SELECT SUM(valor_pedido) FROM pedidos WHERE data_pedido BETWEEN ? AND ?;
Aplicação: Gerar relatórios de vendas por período, ajudando a identificar tendências e sazonalidades.
Manutenção de Dados
Consulta: DELETE FROM clientes WHERE id_cliente = ?; (com ON DELETE CASCADE)
Aplicação: Excluir um cliente e todos os seus pedidos associados, mantendo a integridade referencial do banco de dados.
Exemplos de Uso em Aplicações Reais
E-commerce: Gerenciar pedidos e clientes, enviar alertas e relatórios de vendas.
CRM (Customer Relationship Management): Analisar o comportamento do cliente, identificar oportunidades de venda.
ERP (Enterprise Resource Planning): Gerenciar dados de clientes e pedidos, manter a integridade referencial.

Estrutura do Banco e Relações
O banco de dados é composto por três tabelas: loja, equipamento e garantia. A tabela garantia_estendida é uma extensão da tabela garantia.
loja:
id_loja (chave primária)
nome_loja
cnpj
telefone
cidade
estado
equipamento:
id_equipamento (chave primária)
id_loja (chave estrangeira)
nome
marca
numero_serie
data_compra
garantia:
id_garantia (chave primária)
id_equipamento (chave estrangeira)
id_loja (chave estrangeira)
data_inicio
data_fim
status
garantia_estendida:
id_garantia_estendida (chave primária)
id_garantia (chave estrangeira)
beneficios
custo

A classe Database é responsável por conectar ao banco de dados e realizar consultas. Ela utiliza a biblioteca psycopg2 para se conectar ao banco de dados PostgreSQL.
O script main.py é responsável por criar uma instância da classe Database e realizar consultas ao banco de dados. Ele imprime os resultados das consultas em um formato legível.

Reflexão Pessoal
O que aprendi neste estudo?
Aprendi a criar um banco de dados com relações entre tabelas.
Aprendi a realizar consultas ao banco de dados utilizando a biblioteca psycopg2.
Aprendi a criar uma classe para encapsular a lógica de conexão ao banco de dados.
Aprendi a não deixar de persistir mesmo que que erro em todas as etapas.
Que erros enfrentei e como resolvi?
Enfrentei um erro de índice de tupla ao tentar acessar os resultados da consulta. Resolvi verificando a estrutura da consulta e ajustando o índice.
Enfrentei um erro de conexão ao banco de dados. Resolvi verificando as credenciais de conexão e ajustando a configuração.
Tive problema ao instalar o dbeaver e conectar o banco de dados varias vezes.
Como este exercício se conecta ao projeto integrador?
Este exercício me ajudou a entender melhor como criar um projeto do zero, criar um banco de dados e realizar consultas, o que é fundamental para o projeto integrador tendo em vista que esse passo a passo é essencial para desenvolvimento pessoal e profissional deixando assim com que o nosso projeto integrador seja feito da melhor forma.
Este exercício me ajudou a praticar a criação de classes e scripts em Python.

1. Padrões de Projeto (MVC)
   Banco de dados → Model: O banco de dados PostgreSQL é o Model, responsável por armazenar e gerenciar os dados.
   Classes Python → Controller: As classes Python, como Database e GarantiaEstendida, são o Controller, responsáveis por interagir com o Model e realizar operações.
   Futuras views (APIs ou HTML) → View: As futuras views, como APIs ou páginas HTML, serão o View, responsáveis por apresentar os dados ao usuário.
2. Metodologias Ágeis
   Dividiu o trabalho em pequenas tarefas (sprints):
   Sprint 1: Criar o banco de dados e as tabelas.
   Sprint 2: Desenvolver as classes Python para interagir com o banco de dados.
   Sprint 3: Implementar a consulta de garantia estendida.
   Sprint 4: Testar e refatorar o código.
