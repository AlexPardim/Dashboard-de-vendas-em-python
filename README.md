# Supermarket Sales Dashboard

Este repositório contém um dashboard interativo desenvolvido com Streamlit para visualizar dados de vendas de um supermercado. O dashboard apresenta várias visualizações, incluindo faturamento por unidade, tipo de produto mais vendido, contribuição por filial, desempenho das formas de pagamento e avaliações das filiais.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/AlexPardim/Dashboard-de-vendas-em-python.git

2. Navegue até o diretório do projeto:
cd seurepositorio

3. Crie um ambiente virtual e ative-o:
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

4. Instale as dependências:
pip install -r requirements.txt

## Uso
1. Coloque o arquivo supermarket_sales.csv no diretório do projeto.
2. Execute o aplicativo Streamlit:
streamlit run app.py

3. Acesse o dashboard no seu navegador em http://localhost:8501.

## Estrutura do Código

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Com uma visão mensal:
# - Faturamento por unidade
# - Tipo de produto mais vendido
# - Contribuição por filial
# - Desempenho das formas de pagamento
# - Como estão as avaliações das filiais?

# Leitura do arquivo CSV
df = pd.read_csv("C:\\Users\\alexj\\OneDrive\\Desktop\\Alex Desenvolvimento\\Asimov Academy\\Supermarket Sales\\supermarket_sales.csv", sep=";", decimal=",")

# Conversão e ordenação da data
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Extração do mês
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

# Filtragem dos dados com base no mês selecionado
df_filtered = df[df["Month"] == month]

# Criação de colunas para organizar os gráficos
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Gráfico de faturamento por dia
fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_width=True)

# Gráfico de faturamento por tipo de produto
fig_prod = px.bar(df_filtered, x="Product line", y="Total", color="City", title="Faturamento por tipo de produto", orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

# Gráfico de faturamento por filial
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", title="Faturamento por filial")
col3.plotly_chart(fig_city, use_container_width=True)

# Gráfico de faturamento por tipo de pagamento
fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind, use_container_width=True)

# Gráfico de avaliação por filial
city_rating = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(city_rating, x="City", y="Rating", title="Avaliação das filiais")
col5.plotly_chart(fig_rating, use_container_width=True)

## Licença
Este projeto está licenciado sob a licença MIT.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Contato
Para mais informações, entre em contato com alexjrpardim@hotmail.com
