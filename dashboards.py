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
