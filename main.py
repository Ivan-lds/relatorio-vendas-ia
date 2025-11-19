# Arquivo principal para execução do dashboard
import streamlit as st
import pandas as pd
from supabase import create_client, Client
from src.utils import detectar_coluna, converter_tipos
from src.metrics import calcular_metricas
from src.visuals import (
    show_metric_cards,
    show_geotemporal_analysis,
    show_client_product_analysis,
    show_commercial_financial_analysis,
    show_temporal_segmentation_analysis,
    show_report
)
from src.plans import show_pricing
from src.formulas import show_formulas_catalog
from src.spreadsheets import show_spreadsheets_catalog


st.set_page_config(
    page_title="Analytics BI Pro - Relatório Inteligente",
    layout="wide",
    initial_sidebar_state="expanded"
)

def get_supabase() -> Client:
    url = st.secrets.get("SUPABASE_URL", "")
    key = st.secrets.get("SUPABASE_ANON_KEY", "")
    if not url or not key:
        return None
    try:
        return create_client(url, key)
    except Exception:
        return None

def login_gate() -> bool:
    if "auth_user" not in st.session_state:
        st.session_state.auth_user = None
    if st.session_state.auth_user:
        return True
    sb = get_supabase()
    if not sb:
        st.info("Login desabilitado (credenciais Supabase ausentes). Prosseguindo sem login...")
        return True
    st.markdown("## Acesso")
    tab_login, tab_signup = st.tabs(["Entrar", "Criar conta"]) 

    with tab_login:
        with st.form("login_form", clear_on_submit=False):
            email = st.text_input("E-mail")
            password = st.text_input("Senha", type="password")
            submitted = st.form_submit_button("Entrar")
        if submitted:
            try:
                res = sb.auth.sign_in_with_password({"email": email, "password": password})
                if res and getattr(res, "user", None):
                    st.session_state.auth_user = {"email": email}
                    st.rerun()
                else:
                    st.error("Credenciais inválidas.")
            except Exception as e:
                st.error(f"Erro no login: {e}")

    with tab_signup:
        with st.form("signup_form", clear_on_submit=False):
            email_su = st.text_input("E-mail", key="signup_email")
            password_su = st.text_input("Senha", type="password", key="signup_password")
            submitted_su = st.form_submit_button("Criar conta")
        if submitted_su:
            try:
                res = sb.auth.sign_up({"email": email_su, "password": password_su})
                if res and getattr(res, "user", None):
                    st.success("Conta criada! Verifique seu e-mail para confirmar o cadastro.")
                    st.stop()
                else:
                    st.error("Não foi possível criar a conta.")
            except Exception as e:
                st.error(f"Erro no cadastro: {e}")
    st.stop()
    return False

col_menu, col_logout = st.columns([8, 0.65])
with col_menu:
    menu = st.radio("", ["Dashboard", "Fórmulas", "Planilhas", "Planos"], horizontal=True)
with col_logout:
    if st.session_state.get("auth_user"):
        if st.button("Sair"):
            sb_tmp = get_supabase()
            if sb_tmp:
                try:
                    sb_tmp.auth.sign_out()
                except Exception:
                    pass
            st.session_state.auth_user = None
            st.rerun()

if menu == "Planos":
    show_pricing()
    st.stop()

if menu == "Fórmulas":
    show_formulas_catalog()
    st.stop()

if menu == "Planilhas":
    show_spreadsheets_catalog()
    st.stop()

with st.sidebar:
    st.header("Informações")
    st.markdown("""
        ### Como usar
        1. Faça upload do arquivo CSV ou Excel (xlsx)
        2. Aguarde a análise automática
        3. Receba insights estratégicos
        
        ### Colunas aceitas (flexíveis)
        
        **Básicas (obrigatórias para relatório):**
        - Data: Dia, Data, Date, Dt, Data Venda
        - Vendas: Vendas, Valor, Faturamento, Receita, Total, Sales, Amount
        
        **Cliente:** Cliente, Nome, CPF/CNPJ, Segmento, Faixa Etária, Sexo
                
        **Produto:** Produto, Categoria, Marca, Quantidade, Preço, Desconto
                
        **Financeiro:** Receita Bruta/Líquida, Impostos, Lucro, Ticket Médio
                
        **Logística:** Estoque, Frete, Prazo, Transportadora
                
        **Temporal:** Dia da Semana, Mês, Ano, Horário
                
        **Comercial:** Vendedor, Canal, Campanha, Comissão, Meta
                
        - As colunas são detectadas por nome (aceita maiúsculas/minúsculas)
                
        Atenção: Se não houver dados suficientes, os gráficos e métricas não serão exibidos. Certifique-se de que seu arquivo contém pelo menos as colunas de Data e Vendas para liberar todas as análises!
        
        ---
        Suporte:
                
        Whatsapp - (75) 98885-5230
        Ligação - (75) 99941-5339
    """)
    

if not login_gate():
    st.stop()

st.title("Analytics BI Pro")
st.markdown("### Sistema Inteligente de Análise de Vendas")

csv_file = st.file_uploader("Selecione o arquivo de vendas (CSV ou Excel)", type=["csv", "xlsx"])
if not csv_file:
    st.warning("Aguardando upload do arquivo...")
    st.stop()
else:
    st.success("Arquivo carregado com sucesso!")
    filename = csv_file.name.lower()
    if filename.endswith(".csv"):
        df = pd.read_csv(csv_file)
    else:
        df = pd.read_excel(csv_file, engine="openpyxl")
    df.columns = df.columns.str.strip()
    # Detecta colunas principais
    colunas = {
        'col_data': detectar_coluna(df, ["dia", "data", "date", "dt", "data_venda", "data venda", "data_compra"]),
        'col_vendas': detectar_coluna(df, ["vendas", "valor", "valor_venda", "faturamento", "receita", "total", "sales", "amount", "receita_bruta"]),
        'col_estado': detectar_coluna(df, ["estado", "uf", "regiao"]),
        'col_dia_semana': detectar_coluna(df, ["dia_semana"]),
        'col_cliente': detectar_coluna(df, ["cliente", "nome_cliente"]),
        'col_produto': detectar_coluna(df, ["produto", "nome_produto"]),
        'col_vendedor': detectar_coluna(df, ["vendedor"]),
        'col_canal_venda': detectar_coluna(df, ["canal", "canal_venda"]),
        'col_categoria_produto': detectar_coluna(df, ["categoria", "categoria_produto"]),
        'col_mes': detectar_coluna(df, ["mes", "mês"]),
        'col_receita_bruta': detectar_coluna(df, ["receita_bruta"]),
        'col_receita_liquida': detectar_coluna(df, ["receita_liquida"]),
        'col_impostos': detectar_coluna(df, ["impostos", "total_impostos"]),
    'col_lucro_bruto': detectar_coluna(df, ["lucro_bruto"]),
    'col_lucro_liquido': detectar_coluna(df, ["lucro_liquido"]),
    'col_forma_pagamento': detectar_coluna(df, ["forma_pagamento"]),
    'col_segmento': detectar_coluna(df, ["segmento"])
    }
    df = converter_tipos(df, colunas['col_data'], colunas['col_vendas'])
    metricas = calcular_metricas(df, colunas)
    tabs = st.tabs([
        "Visão Geral", "Geográfica/Temporal", "Clientes/Produtos", "Comercial/Financeiro", "Temporal/Segmentação", "Relatório"
    ])
    with tabs[0]:
        show_metric_cards(
            metricas.get('total_vendas'), metricas.get('vendas_por_dia'), metricas.get('numero_dias'), metricas.get('total_estados'),
            metricas.get('total_clientes'), metricas.get('total_produtos'), metricas.get('total_vendedores'),
            metricas.get('receita_bruta'), metricas.get('receita_liquida'), metricas.get('total_impostos'), metricas.get('lucro_bruto'), metricas.get('lucro_liquido')
        )
    with tabs[1]:
        show_geotemporal_analysis(
            metricas['top_estados'], metricas['df_semanal'], df,
            colunas['col_estado'], colunas['col_vendas'], colunas['col_data']
        )
    with tabs[2]:
        show_client_product_analysis(
            metricas['top_clientes'], metricas['top_produtos'], metricas['vendas_por_categoria']
        )
    with tabs[3]:
        show_commercial_financial_analysis(
            metricas.get('top_vendedores'), metricas.get('vendas_por_canal'), metricas.get('vendas_por_pagamento')
        )
    with tabs[4]:
        show_temporal_segmentation_analysis(
            metricas.get('vendas_por_mes'), metricas.get('vendas_por_dia_semana'), metricas.get('vendas_por_segmento')
        )
    with tabs[5]:
        show_report(
            metricas.get('report'), metricas.get('dados_suficientes'),
            colunas['col_data'], colunas['col_vendas'], colunas['col_estado']
        )

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "Suporte: "
    "Whatsapp - (75) 98885-5230"
    " | Ligação - (75) 99941-5339"
    "</div>",
    unsafe_allow_html=True
)
