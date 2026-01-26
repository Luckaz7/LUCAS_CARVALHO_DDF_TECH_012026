# Case Técnico - Analytics Engineer @ Dadosfera

Candidato: Lucas Carvalho Soares da Silva.
Data: Janeiro de 2026.
Dataset: Brazilian E-Commerce Public Dataset (Olist).


📑 # Sumário Executivo

Este projeto visa a implementação de uma plataforma de dados ponta a ponta utilizando a Dadosfera.

O foco é transformar dados brutos de e-commerce em ativos de inteligência de negócio, utilizando modelagem dimensional e enriquecimento via Inteligência Artificial(GenAI), entregando análises descritivas e prescritivas com agilidade e menor custo em todas as áreas da empresa.


🛠️ # Stack Utilizada:

    Data Platform: Dadosfera (Coleta, Explorar, Analisar)

    Linguagens: Python (Tratamento e Quality), SQL (Modelagem Star Schema)

    IA: LLM para enriquecimento de dados (GenAI)

    Visualização: Metabase & Streamlit


⚠️ # Nota sobre a Metodologia de Execução

Observação Técnica: Para garantir a máxima integridade e eficiência no carregamento de dados, optei por realizar os itens 4 (Data Quality) e 5 (Enriquecimento GenAI) previamente à etapa de 2 (Integração).

Motivação: Tratar os dados em Python e enriquecê-los com LLM antes da ingestão permite que o Data Lakehouse receba arquivos otimizados em .parquet, reduzindo custos de armazenamento, evitando processamento de dados nulos e garantindo que o Catálogo de Dados (Item 3) já nasça com as features de inteligência artificial integradas.

Narrativa de Negócio: O projeto simula a fase pós-kickoff de uma implementação real para uma grande empresa de e-commerce.


📋 # Itens do Case

0. Planejamento e Metodologia Ágil

Organização do projeto utilizando Kanban para gestão de tarefas e prazos.

• [INSIRA O PRINT DO TRELLO AQUI]
• Legenda: Board Kanban estruturado para o ciclo de vida do projeto de Analytics Engineering.

1. Seleção do Dataset

Escolha de uma base real de e-commerce com mais de 100k registros para garantir a escalabilidade da solução.

• [INSIRA O PRINT DO KAGGLE OU DOS ARQUIVOS BAIXADOS AQUI]
• Legenda: Dataset Olist selecionado pela sua complexidade relacional e volume de dados (+100k pedidos).

4. Processamento de Dados & Data Quality (Antecipado)

Aplicação de limpeza, tratamento de tipos e testes de qualidade via Python (Notebook anexo).

• [INSIRA O PRINT DO RELATÓRIO DE QUALIDADE/CÓDIGO NO COLAB AQUI]
• Legenda: Auditoria de dados via Python identificando integridade de chaves primárias e tratamento de valores nulos.

5. Inteligência de Dados (GenAI) (Antecipado)

Enriquecimento da base original utilizando modelos de linguagem para categorização inteligente.

• [INSIRA O PRINT DO CÓDIGO DA API GENAI OU DO DATAFRAME COM A NOVA COLUNA AQUI]
• Legenda: Extração de atributos de produtos via LLM para maior granularidade na análise de vendas.


🚧 # Etapas em Desenvolvimento (Aguardando Ingestão)

2. Integração (Módulo Integrar)

Status: Em progresso (Aguardando carga dos arquivos .parquet otimizados).

Nesta etapa, realizarei a configuração do pipeline de coleta para mover os dados tratados do ambiente local para a camada Standardized da Dadosfera.

• [INSIRA O PRINT]

3. Catalogação (Módulo Explorar)

Status: Aguardando carga.

Criação do Dicionário de Dados e documentação dos ativos no catálogo da plataforma para garantir a governança.

• [INSIRA O PRINT]

6 e 7. Modelagem e Visualização (Módulo Analisar)

Status: Planejado.

Construção do Star Schema (Kimball) e criação de Dashboards executivos no Metabase integrando as métricas de negócio.

• [INSIRA O PRINT]


🎥 # Apresentação do Case (Item 10)

Status: Planejado.

Link do vídeo com a proposta de valor e substituição da arquitetura legada pela Dadosfera (em breve).

• [INSIRA O PRINT]


📂 # Estrutura do Repositório

• /notebooks: Contém o código de tratamento e GenAI.
• /docs: Documentos de apoio e imagens.
• README.md: Documentação principal.

• [INSIRA O PRINT]
