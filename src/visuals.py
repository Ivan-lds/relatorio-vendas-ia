# Módulo de visualizações para o dashboard
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import requests
import io
import pandas as pd

# Função auxiliar para exportar tabela em Excel
def export_table_button_excel(df, label):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Dados')
    output.seek(0)
    st.download_button(
        label=f"Exportar (Excel)",
        data=output,
        file_name=f"{label.replace(' ', '_').lower()}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# Função auxiliar para exportar tabela
def export_table_button(df, label):
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=f"Exportar (CSV)",
        data=csv,
        file_name=f"{label.replace(' ', '_').lower()}.csv",
        mime="text/csv"
    )

def export_table_buttons(df, label):
    col_csv, col_excel = st.columns([0.5, 4])
    with col_csv:
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label=f"Exportar (CSV)",
            data=csv,
            file_name=f"{label.replace(' ', '_').lower()}.csv",
            mime="text/csv"
        )
    with col_excel:
        import io
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Dados')
        output.seek(0)
        st.download_button(
            label=f"Exportar (Excel)",
            data=output,
            file_name=f"{label.replace(' ', '_').lower()}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

def show_metric_cards(total_vendas, vendas_por_dia, numero_dias, total_estados, total_clientes, total_produtos, total_vendedores, receita_bruta, receita_liquida, total_impostos, lucro_bruto, lucro_liquido):
    st.markdown("### Métricas Principais")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total de Vendas", f"R$ {total_vendas:,.2f}" if total_vendas is not None else "N/D")
    with col2:
        st.metric("Média Diária", f"R$ {vendas_por_dia:,.2f}" if vendas_por_dia is not None else "N/D")
    with col3:
        st.metric("Período Analisado", f"{numero_dias} dias" if numero_dias is not None else "N/D")
    with col4:
        st.metric("Total de Estados", total_estados if total_estados is not None else "N/D")
    st.markdown("---")

    if any([total_clientes, total_produtos, total_vendedores, receita_bruta]):
        st.markdown("### Métricas de Cliente e Produto")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total de Clientes", total_clientes if total_clientes is not None else "N/D")
        with col2:
            st.metric("Total de Produtos", total_produtos if total_produtos is not None else "N/D")
        with col3:
            st.metric("Total de Vendedores", total_vendedores if total_vendedores is not None else "N/D")
        with col4:
            st.metric("Receita Bruta", f"R$ {receita_bruta:,.2f}" if receita_bruta is not None else "N/D")
        st.markdown("---")

    if any([receita_liquida, total_impostos, lucro_bruto, lucro_liquido]):
        st.markdown("### Métricas Financeiras")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Receita Líquida", f"R$ {receita_liquida:,.2f}" if receita_liquida is not None else "N/D")
        with col2:
            st.metric("Total Impostos", f"R$ {total_impostos:,.2f}" if total_impostos is not None else "N/D")
        with col3:
            st.metric("Lucro Bruto", f"R$ {lucro_bruto:,.2f}" if lucro_bruto is not None else "N/D")
        with col4:
            st.metric("Lucro Líquido", f"R$ {lucro_liquido:,.2f}" if lucro_liquido is not None else "N/D")

def show_geotemporal_analysis(top_estados, df_semanal, df, col_estado, col_vendas, col_data):
    st.markdown("#### Análise Geográfica e Temporal")
    col_graf1, col_graf2, col_graf3 = st.columns(3)
    with col_graf1:
        if top_estados is not None and len(top_estados) > 0:
            fig_estados = px.bar(x=top_estados.index, y=top_estados.values, title="Top 5 Estados por Volume de Vendas", labels={"x": col_estado or "Estado", "y": "Total de Vendas (R$)"})
            fig_estados.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig_estados, use_container_width=True)
            st.caption("Gráfico de barras mostrando os 5 estados com maior volume de vendas.")
        else:
            st.info("Sem dados suficientes para o gráfico de Top Estados.")
    with col_graf2:
        if df_semanal is not None and len(df_semanal) > 0:
            fig_tendencia = px.line(df_semanal, title="Tendência de Vendas ao Longo do Tempo", labels={"value": "Total de Vendas (R$)", col_data or "Dia": "Data"})
            fig_tendencia.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig_tendencia, use_container_width=True)
            st.caption("Gráfico de linha mostrando a tendência de vendas ao longo do tempo.")
        else:
            st.info("Sem dados de data e vendas para tendência.")
    with col_graf3:
        if col_estado and col_vendas and col_estado in df.columns and col_vendas in df.columns:
            df_estados_todos = df.groupby(col_estado)[col_vendas].sum()
            if len(df_estados_todos) > 0:
                fig_pizza = px.pie(values=df_estados_todos.values, names=df_estados_todos.index, title="Distribuição de Vendas por Estado")
                fig_pizza.update_layout(height=400)
                st.plotly_chart(fig_pizza, use_container_width=True)
                st.caption("Gráfico de pizza mostrando a distribuição das vendas por estado.")
            else:
                st.info("Sem dados suficientes para a distribuição por estado.")
        else:
            st.info("Colunas de estado e vendas não disponíveis para a pizza.")
    st.markdown("---")
    st.markdown("##### Tabela Dinâmica - Vendas por Estado")
    if col_estado and col_vendas and col_estado in df.columns and col_vendas in df.columns:
        tabela_estado = df.groupby(col_estado)[col_vendas].sum().reset_index().sort_values(col_vendas, ascending=False)
        st.dataframe(tabela_estado, use_container_width=True)
        export_table_buttons(tabela_estado, "Vendas por Estado")
    else:
        st.info("Não foi possível gerar a tabela dinâmica de estados.")

def show_client_product_analysis(top_clientes, top_produtos, vendas_por_categoria):
    st.markdown("#### Análise de Clientes e Produtos")
    col_graf1, col_graf2, col_graf3 = st.columns(3)
    with col_graf1:
        if top_clientes is not None and len(top_clientes) > 0:
            fig_clientes = px.scatter(x=top_clientes.index, y=top_clientes.values, title="Top 5 Clientes por Volume de Compras", labels={"x": "Cliente", "y": "Total de Compras (R$)"}, size=top_clientes.values, color=top_clientes.values, color_continuous_scale='Blues')
            fig_clientes.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig_clientes, use_container_width=True)
            st.caption("Gráfico de dispersão dos 5 clientes que mais compraram.")
        else:
            st.info("Sem dados suficientes para o gráfico de Top Clientes.")
    with col_graf2:
        if top_produtos is not None and len(top_produtos) > 0:
            fig_produtos = px.bar(x=top_produtos.index, y=top_produtos.values, color=top_produtos.index, title="Top 5 Produtos por Volume de Vendas", labels={"x": "Produto", "y": "Total de Vendas (R$)"}, color_discrete_sequence=px.colors.qualitative.Safe)
            fig_produtos.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig_produtos, use_container_width=True)
            st.caption("Gráfico de barras dos 5 produtos mais vendidos.")
        else:
            st.info("Sem dados suficientes para o gráfico de Top Produtos.")
    with col_graf3:
        if vendas_por_categoria is not None and len(vendas_por_categoria) > 0:
            fig_categoria = px.pie(values=vendas_por_categoria.values, names=vendas_por_categoria.index, title="Distribuição de Vendas por Categoria")
            fig_categoria.update_layout(height=400)
            st.plotly_chart(fig_categoria, use_container_width=True)
            st.caption("Gráfico de pizza mostrando a distribuição das vendas por categoria de produto.")
        else:
            st.info("Sem dados suficientes para a distribuição por categoria.")
    st.markdown("---")
    st.markdown("##### Tabela Dinâmica - Top Clientes e Produtos")
    tabela_clientes = pd.DataFrame({"Cliente": top_clientes.index, "Total Compras": top_clientes.values}) if top_clientes is not None else pd.DataFrame()
    tabela_produtos = pd.DataFrame({"Produto": top_produtos.index, "Total Vendas": top_produtos.values}) if top_produtos is not None else pd.DataFrame()
    st.dataframe(tabela_clientes, use_container_width=True)
    export_table_buttons(tabela_clientes, "Top Clientes")
    st.dataframe(tabela_produtos, use_container_width=True)
    export_table_buttons(tabela_produtos, "Top Produtos")

def export_report_pdf(report_md):
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    import streamlit as st
    import tempfile
    if not report_md:
        st.info("Relatório não disponível para exportação.")
        return
    # Converte Markdown para texto simples
    texto = report_md.replace('**', '').replace('#', '').replace('###', '').replace('##', '')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
        c = canvas.Canvas(tmpfile.name, pagesize=A4)
        width, height = A4
        y = height - 40
        for linha in texto.splitlines():
            if linha.strip():
                c.drawString(40, y, linha.strip())
                y -= 16
                if y < 40:
                    c.showPage()
                    y = height - 40
        c.save()
        tmpfile.seek(0)
        st.download_button(
            label="Exportar Relatório Analítico (PDF)",
            data=tmpfile.read(),
            file_name="relatorio_analitico.pdf",
            mime="application/pdf"
        )

def show_report(report, dados_suficientes, col_data, col_vendas, col_estado):
    col_pause, col_pdf = st.columns([3.6, 1])
    with col_pause:
        if st.button("Pausar geração do relatório", key="pause_report"):
            st.warning("Geração do relatório pausada pelo usuário.")
            st.stop()
    report_md = None
    if report and dados_suficientes:
        with st.spinner("Gerando análise inteligente..."):
            try:
                IAHUB_API_KEY = st.secrets.get("IAHUB_API_KEY", "")
                IAHUB_URL = st.secrets.get("IAHUB_URL", "")
                headers = {
                    "x-api-key": IAHUB_API_KEY,
                    "Content-Type": "application/json",
                    "Accept-Encoding": "gzip, deflate"
                }
                payload = {
                    "model": "llama-2-7b",
                    "messages": [
                        {"role": "system", "content": "Você é um analista de BI especializado em gerar relatórios concisos e informativos."},
                        {"role": "user", "content": report}
                    ]
                }
                response = requests.post(IAHUB_URL, json=payload, headers=headers)
                if response.status_code == 200:
                    report_md = response.json().get("resposta", "Relatório não gerado pela API.")
                    st.markdown("### Relatório Analítico")
                    with st.expander("Visualizar Relatório Completo", expanded=True):
                        st.markdown(report_md, unsafe_allow_html=True)
                else:
                    st.error(f"Erro na API: {response.status_code}")
                    st.error(f"Detalhes: {response.text}")
            except Exception as e:
                st.error(f"Erro ao gerar relatório: {str(e)}")
    if report_md:
        with col_pdf:
            export_report_pdf(report_md)
    if not dados_suficientes:
        st.warning("**Dados Insuficientes para Relatório**")
        st.info(f"""
        Para gerar um relatório analítico, o CSV deve conter pelo menos:
        - **Coluna de Data**: para análise temporal
        - **Coluna de Vendas**: para cálculos financeiros

        **Colunas detectadas no seu arquivo:**
        - Data: {'Sim' if col_data else 'Não'} {col_data or 'Não encontrada'}
        - Vendas: {'Sim' if col_vendas else 'Não'} {col_vendas or 'Não encontrada'}
        - Estados: {'Sim' if col_estado else 'Não'} {col_estado or 'Não encontrada'}
        """)
    if not report and not dados_suficientes:
        st.info("Relatório não disponível: verifique se a API respondeu corretamente.")

def show_commercial_financial_analysis(top_vendedores, vendas_por_canal, vendas_por_pagamento):
    st.markdown("#### Análise Comercial e Financeira")
    col_graf1, col_graf2, col_graf3 = st.columns(3)
    with col_graf1:
        if top_vendedores is not None and len(top_vendedores) > 0:
            fig_vendedores = px.bar(x=top_vendedores.index, y=top_vendedores.values, color=top_vendedores.index, title="Top 5 Vendedores por Volume de Vendas", labels={"x": "Vendedor", "y": "Total de Vendas (R$)"}, color_discrete_sequence=px.colors.qualitative.Safe)
            fig_vendedores.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig_vendedores, use_container_width=True)
            st.caption("Gráfico de barras dos 5 vendedores com maior volume de vendas.")
        else:
            st.info("Sem dados suficientes para o gráfico de Top Vendedores.")
    with col_graf2:
        if vendas_por_canal is not None and len(vendas_por_canal) > 0:
            fig_canal = px.pie(values=vendas_por_canal.values, names=vendas_por_canal.index, title="Distribuição de Vendas por Canal", hole=0.4, color_discrete_sequence=px.colors.qualitative.Pastel)
            fig_canal.update_layout(height=400)
            st.plotly_chart(fig_canal, use_container_width=True)
            st.caption("Gráfico de pizza mostrando a distribuição das vendas por canal.")
        else:
            st.info("Sem dados suficientes para a distribuição por canal.")
    with col_graf3:
        if vendas_por_pagamento is not None and len(vendas_por_pagamento) > 0:
            total_pagamento = vendas_por_pagamento.values.sum()
            labels = [f"{nome}<br>R$ {valor:,.2f}<br>{valor/total_pagamento*100:.1f}%" for nome, valor in zip(vendas_por_pagamento.index, vendas_por_pagamento.values)]
            fig_pagamento = px.treemap(
                names=vendas_por_pagamento.index,
                parents=[""]*len(vendas_por_pagamento),
                values=vendas_por_pagamento.values,
                title="Distribuição de Vendas por Forma de Pagamento",
                custom_data=[vendas_por_pagamento.values, [f"{v/total_pagamento*100:.1f}%" for v in vendas_por_pagamento.values]]
            )
            fig_pagamento.update_traces(
                textinfo="label+value+percent entry",
                texttemplate=labels,
                hovertemplate='<b>%{label}</b><br>Valor: R$ %{value:,.2f}<br>Percentual: %{customdata[1]}'
            )
            fig_pagamento.update_layout(height=400)
            st.plotly_chart(fig_pagamento, use_container_width=True)
            st.caption("Gráfico de treemap mostrando a distribuição das vendas por forma de pagamento.")
        else:
            st.info("Sem dados suficientes para a distribuição por pagamento.")
    st.markdown("---")
    st.markdown("##### Tabela Dinâmica - Vendedores e Canais")
    tabela_vendedores = pd.DataFrame({"Vendedor": top_vendedores.index, "Total Vendas": top_vendedores.values}) if top_vendedores is not None else pd.DataFrame()
    tabela_canais = pd.DataFrame({"Canal": vendas_por_canal.index, "Total Vendas": vendas_por_canal.values}) if vendas_por_canal is not None else pd.DataFrame()
    st.dataframe(tabela_vendedores, use_container_width=True)
    export_table_buttons(tabela_vendedores, "Vendedores")
    st.dataframe(tabela_canais, use_container_width=True)
    export_table_buttons(tabela_canais, "Canais")

def show_temporal_segmentation_analysis(vendas_por_mes, vendas_por_dia_semana, vendas_por_segmento):
    st.markdown("#### Análise Temporal e Segmentação")
    col_graf1, col_graf2, col_graf3 = st.columns(3)
    with col_graf1:
        if vendas_por_mes is not None and len(vendas_por_mes) > 0:
            df_mes = pd.DataFrame({"Mês": vendas_por_mes.index, "Total de Vendas": vendas_por_mes.values})
            fig_line = px.line(
                df_mes,
                x="Mês",
                y="Total de Vendas",
                title="Vendas por Mês",
                markers=True,
                line_shape="linear",
                color_discrete_sequence=["#636EFA"]
            )
            fig_line.update_traces(marker=dict(color=px.colors.qualitative.Safe, size=10), line_color="#636EFA")
            fig_line.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig_line, use_container_width=True)
            st.caption("Gráfico de linha mostrando a evolução das vendas por mês.")
        else:
            st.info("Sem dados suficientes para o gráfico de Vendas por Mês.")
    with col_graf2:
        if vendas_por_dia_semana is not None and len(vendas_por_dia_semana) > 0:
            fig_dia_semana = px.bar(x=vendas_por_dia_semana.values, y=vendas_por_dia_semana.index, title="Vendas por Dia da Semana", labels={"x": "Dia da Semana", "y": "Total de Vendas (R$)"})
            fig_dia_semana.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig_dia_semana, use_container_width=True)
            st.caption("Gráfico de barras mostrando as vendas por dia da semana.")
        else:
            st.info("Sem dados suficientes para o gráfico de Vendas por Dia da Semana.")
    with col_graf3:
        if vendas_por_segmento is not None and len(vendas_por_segmento) > 0:
            fig_segmento = px.pie(values=vendas_por_segmento.values, names=vendas_por_segmento.index, title="Distribuição de Vendas por Segmento de Cliente")
            fig_segmento.update_layout(height=400)
            st.plotly_chart(fig_segmento, use_container_width=True)
            st.caption("Gráfico de pizza mostrando a distribuição das vendas por segmento de cliente.")
        else:
            st.info("Sem dados suficientes para a distribuição por segmento.")
    st.markdown("---")
    st.markdown("##### Tabela Dinâmica - Vendas por Mês, Dia da Semana e Segmento")
    tabela_mes = pd.DataFrame({"Mês": vendas_por_mes.index, "Total Vendas": vendas_por_mes.values}) if vendas_por_mes is not None else pd.DataFrame()
    tabela_dia_semana = pd.DataFrame({"Dia da Semana": vendas_por_dia_semana.index, "Total Vendas": vendas_por_dia_semana.values}) if vendas_por_dia_semana is not None else pd.DataFrame()
    tabela_segmento = pd.DataFrame({"Segmento": vendas_por_segmento.index, "Total Vendas": vendas_por_segmento.values}) if vendas_por_segmento is not None else pd.DataFrame()
    st.dataframe(tabela_mes, use_container_width=True)
    export_table_buttons(tabela_mes, "Vendas por Mês")
    st.dataframe(tabela_dia_semana, use_container_width=True)
    export_table_buttons(tabela_dia_semana, "Vendas por Dia da Semana")
    st.dataframe(tabela_segmento, use_container_width=True)
    export_table_buttons(tabela_segmento, "Vendas por Segmento")

def plot_visao_geral(df_semanal, vendas_por_dia_semana, df, col_vendas, col_dia_semana, col_data):
    st.markdown("#### Visão Geral das Vendas")
    if df_semanal is not None and len(df_semanal) > 0:
        fig_area = px.area(df_semanal, title="Tendência de Vendas (Área)", labels={"value": "Total de Vendas (R$)", col_data or "Dia": "Data"})
        fig_area.update_layout(height=350)
        st.plotly_chart(fig_area, use_container_width=True)
    if vendas_por_dia_semana is not None and len(vendas_por_dia_semana) > 0:
        fig_box = px.box(df, y=col_vendas, x=col_dia_semana, title="Distribuição de Vendas por Dia da Semana (Boxplot)")
        fig_box.update_layout(height=350)
        st.plotly_chart(fig_box, use_container_width=True)

# Outras funções de visualização podem ser criadas para cada aba
