# Analytics BI Pro 📊

Sistema inteligente de análise de vendas com geração automática de relatórios e visualizações utilizando IA.

## 📌 Funcionalidades

- Upload de arquivos CSV de vendas
- Análise automática de dados
- Geração de insights com IA
- Visualizações interativas:
  - Top 5 estados por volume de vendas
  - Tendência temporal de vendas
  - Distribuição geográfica das vendas
- Métricas principais em tempo real
- Relatório analítico detalhado em Markdown

## 🚀 Tecnologias Utilizadas

- Python 3.12+
- Streamlit
- Pandas
- Plotly
- IA Hub API

## 📋 Pré-requisitos

```bash
Python 3.12 ou superior
pip (gerenciador de pacotes Python)
```

## 🔧 Instalação

1. Clone o repositório:

```bash
git clone https://seu-repositorio/analytics-bi-pro.git
cd analytics-bi-pro
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure as credenciais:

- Renomeie `config.example.py` para `config.py`
- Adicione sua chave API do IA Hub

## 📊 Formato do CSV

O arquivo de dados deve conter as seguintes colunas:

- Estado
- Cidade
- Loja
- Dia
- Vendas

Exemplo:

```csv
Estado,Cidade,Loja,Dia,Vendas
SP,São Paulo,Loja 1,2025-01-01,1000.00
RJ,Rio de Janeiro,Loja 2,2025-01-01,800.00
```

## 🚀 Como Usar

1. Execute o aplicativo:

```bash
streamlit run ia-relatorio-vendas.py
```

2. Acesse através do navegador (geralmente http://localhost:8501)

3. Faça upload do seu arquivo CSV de vendas

4. Aguarde o processamento automático

## 🛠️ Configuração

As configurações podem ser ajustadas no arquivo `config.py`:

```python
IAHUB_API_KEY = "sua_chave_api"
IAHUB_URL = "https://api.iahub.site/chat"
```

## 📈 Recursos

- Interface responsiva
- Visualizações interativas
- Análise em tempo real
- Insights acionáveis
- Relatórios personalizados

## 🤝 Suporte

Para suporte e dúvidas, entre em contato:

- Email: ivanlimadossantos4@gmail.com

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para mais detalhes.

## 🎁 Agradecimentos

- IA Hub pela API de processamento de linguagem natural
- Comunidade Streamlit pelos recursos e documentação
