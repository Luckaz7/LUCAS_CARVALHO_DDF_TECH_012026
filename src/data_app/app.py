import streamlit as st
import pandas as pd

st.set_page_config(page_title="Olist Smart Explorer", layout="wide")

st.title("🚀 Olist Product Intelligence - Data App")
st.markdown("Exploração de similaridade de produtos enriquecidos via IA Generativa.")

df = pd.read_csv("amostra_olist.csv")

st.sidebar.header("Filtros de Inteligência")
categoria = st.sidebar.selectbox("Selecione uma Categoria (IA):", df['genai_category'].unique())

df_filtered = df[df['genai_category'] == categoria]

col1, col2 = st.columns(2)

with col1:
    st.subheader(f"Produtos em: {categoria}")
    st.dataframe(df_filtered[['product_id', 'product_category_name', 'genai_category']])

with col2:
    st.subheader("Insight da IA")
    st.info(f"A categoria '{categoria}' foi identificada em {len(df_filtered)} produtos que anteriormente estavam sem classificação ou mal mapeados.")
    