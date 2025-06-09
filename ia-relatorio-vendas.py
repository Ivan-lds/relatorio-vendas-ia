import os
import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
#from config import IAHUB_API_KEY, IAHUB_URL

IAHUB_API_KEY = st.secrets["IAHUB_API_KEY"]
IAHUB_URL = st.secrets["IAHUB_URL"]

# Configuração da página
st.set_page_config(
    page_title="Analytics BI Pro - Relatório Inteligente",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo CSS personalizado
st.markdown("""
    <style>
        .main {
            padding: 2rem;
        }
        .stTitle {
            font-size: 2.5rem !important;
            color: #1E3D59 !important;
            padding-bottom: 2rem;
        }
        .stSubheader {
            color: #17A2B8 !important;
        }
        .css-1d391kg {
            padding: 2rem;
            border-radius: 10px;
            background-color: #F7F7F7;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
col1, _ = st.columns([3,1])
with col1:
    st.title("📈 Analytics BI Pro")
    st.markdown("### Sistema Inteligente de Análise de Vendas")

# Sidebar com informações
with st.sidebar:
    st.header("ℹ️ Informações")
    st.markdown("""
        ### Como usar
        1. Faça upload do arquivo CSV
        2. Aguarde a análise automática
        3. Receba insights estratégicos
        
        ### Formato do CSV
        - Estado
        - Cidade
        - Loja
        - Dia
        - Vendas
        
        ### Sobre
        Versão 1.0.0
        © 2025
    """)

# Container principal
with st.container():
    st.markdown("### 📤 Upload de Dados")
    
    csv_file = st.file_uploader(
        "Selecione seu arquivo CSV de vendas",
        type="csv",
        help="O arquivo deve conter as colunas: Estado, Cidade, Loja, Dia, Vendas"
    )
    
    if not csv_file:
        st.warning("⚠️ Aguardando upload do arquivo...")
        st.stop()
    else:
        st.success("✅ Arquivo carregado com sucesso!")

if csv_file:
    df = pd.read_csv(csv_file)

    df["Dia"] = pd.to_datetime(df["Dia"], dayfirst=True, errors="coerce")
    df["Vendas"] = pd.to_numeric(df["Vendas"], errors="coerce")

    #METRICAS

    total_vendas = df["Vendas"].sum()
    numero_dias = df["Dia"].nunique()
    vendas_por_dia = total_vendas/numero_dias
    top_estados = df.groupby("Estado")["Vendas"].sum().nlargest(5)

    # Agrupa por semana 
    df_semanal = df.set_index("Dia")
    df_semanal = df_semanal.resample("W")["Vendas"].sum()

    prompt = f'''
    Você é um analista de BI. Gere um **relatório em Markdown** (português) contendo:
    1. Início e final do período de análise. 
    2. Visão geral com total de vendas e média diária.
    3. Tendência semanal, mencionando padrões notáveis.
    4. Ranking Top-5 Estados por Vendas.
    5. Três insights acionáveis para o time comercial.

    ### Dados

    Total vendas: {total_vendas}
    Vendas por dia: {vendas_por_dia}
    Top Estados: {top_estados}
    Vendas por semana: {df_semanal}

    '''   
    
        # Métricas em cards
    if csv_file:
        st.markdown("### 📊 Métricas Principais")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Total de Vendas",
                f"R$ {total_vendas:,.2f}",
                f"{((total_vendas/numero_dias) - vendas_por_dia)/vendas_por_dia:.1%}"
            )
        
        with col2:
            st.metric(
                "Média Diária",
                f"R$ {vendas_por_dia:,.2f}"
            )
            
        with col3:
            st.metric(
                "Período Analisado",
                f"{numero_dias} dias"
            )
            
        with col4:
            st.metric(
                "Total de Estados",
                len(df["Estado"].unique())
            )

    # Visualizações gráficas
    st.markdown("### 📈 Análise Visual")
    
    # Linha única de gráficos
    col_graf1, col_graf2, col_graf3 = st.columns(3)
    
    with col_graf1:
        # Gráfico de Vendas por Estado (Top 5)
        fig_estados = px.bar(
            x=top_estados.index,
            y=top_estados.values,
            title="Top 5 Estados por Volume de Vendas",
            labels={"x": "Estado", "y": "Total de Vendas (R$)"}
        )
        fig_estados.update_layout(
            showlegend=False,
            height=400  # Ajusta altura do gráfico
        )
        st.plotly_chart(fig_estados, use_container_width=True)
    
    with col_graf2:
        # Gráfico de Tendência de Vendas
        fig_tendencia = px.line(
            df_semanal,
            title="Tendência de Vendas ao Longo do Tempo",
            labels={"value": "Total de Vendas (R$)", "Dia": "Data"}
        )
        fig_tendencia.update_layout(
            showlegend=False,
            height=400  # Ajusta altura do gráfico
        )
        st.plotly_chart(fig_tendencia, use_container_width=True)
    
    with col_graf3:
        # Gráfico de Pizza - Distribuição de Vendas por Estado
        df_estados_todos = df.groupby("Estado")["Vendas"].sum()
        fig_pizza = px.pie(
            values=df_estados_todos.values,
            names=df_estados_todos.index,
            title="Distribuição de Vendas por Estado"
        )
        fig_pizza.update_layout(
            height=400  # Ajusta altura do gráfico
        )
        st.plotly_chart(fig_pizza, use_container_width=True)

    # Processamento do relatório
    with st.spinner("🔄 Gerando análise inteligente..."):
        headers = {
            "x-api-key": IAHUB_API_KEY,
            "Content-Type": "application/json",
            "Accept-Encoding": "gzip, deflate"
        }
        
        payload = {
            "model": "llama-2-7b",
            "messages": [
                {
                    "role": "system",
                    "content": "Você é um analista de BI especializado em gerar relatórios concisos e informativos."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
        
        try:
            response = requests.post(IAHUB_URL, json=payload, headers=headers)
            
            if response.status_code == 200:
                report = response.json()["resposta"]
            else:
                error_messages = {
                    400: "Mensagens inválidas",
                    402: "Modelo não suportado",
                    403: "Chave API inválida ou ausente",
                    500: "Erro interno no servidor"
                }
                error_msg = error_messages.get(response.status_code, f"Erro desconhecido: {response.status_code}")
                st.error(f"Erro na API: {error_msg}")
                st.error(f"Detalhes: {response.text}")
                st.stop()
                
        except requests.exceptions.RequestException as e:
            st.error(f"Erro na requisição: {str(e)}")
            st.stop()

    # Exibição do relatório
    if 'report' in locals():
        st.markdown("### 📑 Relatório Analítico")
        with st.expander("Visualizar Relatório Completo", expanded=True):
            st.markdown(report, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "Desenvolvido por Ivan Lima | Suporte: ivanlimadossantos4@gmail.com"
    "</div>",
    unsafe_allow_html=True
)