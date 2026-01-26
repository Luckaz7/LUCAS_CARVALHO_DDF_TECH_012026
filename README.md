# Case Técnico - Analytics Engineer @ Dadosfera

**Candidato:** Lucas Carvalho Soares da Silva.

**Data:** Janeiro de 2026.

**Dataset:** Brazilian E-Commerce Public Dataset (Olist).

**link:** https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

# 📂 Estrutura do Repositório

    • /notebooks: Contém o código de tratamento e GenAI.
    
    • /img: prints.
    
    • README.md: Documentação principal.

# 🛠️ Stack Utilizada:

    Data Platform: Dadosfera (Coleta, Explorar, Analisar)

    Linguagens: Python(Processamento e Tratamento via Pandas, e Quality via Pandera), SQL(Modelagem Star Schema)

    IA: LLM para enriquecimento de dados(GenAI via API do Gemini)

    Visualização: Metabase & Streamlit

# 📖 Dicionário de Dados (Principais Entidades e Atributos de Valor)

Foco na documentação das colunas que trazem inteligência analítica para o case:

| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `order_id` | PK (String) | Identificador único do pedido. |
| `order_purchase_timestamp` | Datetime | Data e hora em que a compra foi realizada. |
| `order_hour` | String | Feature Engineering: Horário formatado (HH:mm) para análise de pico. |
| `delivery_diff_days` | Integer | Feature Engineering: Dias de diferença entre entrega real e estimada. |
| `lead_time_days` | Integer | Feature Engineering: Quantidade de dias para a realização da entrega. |
| `genai_category` | String | Inteligência Artificial: Categoria refinada via LLM (Gemini/OpenAI). |

# 📑 Sumário Executivo

Este projeto visa a implementação de uma plataforma de dados ponta a ponta utilizando a Dadosfera.

O foco é transformar dados brutos de e-commerce em ativos de inteligência de negócio, utilizando modelagem dimensional e enriquecimento via Inteligência Artificial(GenAI), entregando análises descritivas e prescritivas com agilidade e menor custo em todas as áreas da empresa.

# ⚠️ Nota sobre a Metodologia de Execução

**Observação Técnica:** Para garantir a máxima integridade e eficiência no carregamento de dados, optei por realizar os itens 4 (Data Quality) e 5 (Enriquecimento GenAI) previamente à etapa de 2 (Integração).

**Motivação:** Tratar os dados em Python e enriquecê-los com LLM antes da ingestão permite que o Data Lakehouse receba arquivos otimizados em .parquet, reduzindo custos de armazenamento, evitando processamento de dados nulos e garantindo que o Catálogo de Dados (Item 3) já nasça com as features de inteligência artificial integradas.

**Narrativa de Negócio:** O projeto simula a fase pós-kickoff de uma implementação real para uma grande empresa de e-commerce.

# 📋 Itens do Case

**0. Planejamento e Metodologia Ágil**

Organização do projeto utilizando Kanban para gestão de tarefas e prazos.

![Planejamento Ágil](img/planejamento_trello.png)
Legenda: Board Kanban estruturado para o ciclo de vida do projeto de Analytics Engineering.

**1. Seleção do Dataset**

Escolha de uma base real de e-commerce com mais de 100k registros para garantir a escalabilidade da solução.

[INSIRA O PRINT DO KAGGLE OU DOS ARQUIVOS BAIXADOS AQUI]
Legenda: Dataset Olist selecionado pela sua complexidade relacional e volume de dados (+100k pedidos).

**4. Processamento de Dados & Data Quality (Antecipado)**

Aplicação de limpeza, tratamento de tipos e testes de qualidade via Python (Notebook anexo).

![Processamento e Data Quality](img/teste_qualidade_dados_brutos_pedidos.png)
![Processamento e Data Quality](img/teste_qualidade_dados_brutos_clientes.png)
![Processamento e Data Quality](img/teste_qualidade_dados_brutos_produtos.png)
Legenda: Auditoria de dados via Python(Pandera) identificando integridade de chaves primárias e tratamento de valores nulos.

Verificação de Data Quality após correção:

![Processamento e Data Quality](img/teste_qualidade_dados_silver_pedidos.png)
Legenda: Nova auditoria de dados via Python(Pandera) corrigindo as falhas de integridade encontrada nos dados.

**5. Inteligência de Dados(GenAI) (Antecipado)**

Enriquecimento da base original utilizando modelos de linguagem para categorização inteligente.

**Nota de Implementação(GenAI via API do Gemini)**: Durante o enriquecimento, identifiquei respostas nulas da API devido aos filtros de segurança padrão(Safety Settings), onde implementei um tratamento de exceções no pipeline Python para garantir a continuidade da ingestão, mapeando retornos inválidos temporariamente como 'Não Mapeado' para manter a integridade do schema no carregamento para a Dadosfera.

![Inteligência de Dados(GenAI)](img/enriquecimento_dados_genai.png)
Legenda: Extração de atributos de produtos via LLM para maior granularidade na análise de vendas.

# 🚧 Etapas em Desenvolvimento (Aguardando Ingestão)

**2. Integração (Módulo Integrar)**

        Status: Em progresso (Aguardando carga dos arquivos .parquet otimizados).

        Nesta etapa, realizarei a configuração do pipeline de coleta para mover os dados tratados do ambiente local para a camada Standardized da Dadosfera.

        • [INSIRA O PRINT]

**3. Catalogação (Módulo Explorar)**

        Status: Aguardando carga.

        Criação do Dicionário de Dados e documentação dos ativos no catálogo da plataforma para garantir a governança.

        • [INSIRA O PRINT]

**6 e 7. Modelagem e Visualização (Módulo Analisar)**

        Status: Planejado.

        Construção do Star Schema (Kimball) e criação de Dashboards executivos no Metabase integrando as métricas de negócio.

        • [INSIRA O PRINT]

# 🎥 Apresentação do Case

        Status: Planejado.

        Link do vídeo com a proposta de valor e substituição da arquitetura legada pela Dadosfera (em breve).

        • [INSIRA O PRINT]
