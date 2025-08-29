# Módulo de métricas e agrupamentos para o dashboard
import pandas as pd

def calcular_metricas(df, colunas):
    # Inicializa variáveis
    resultados = {}
    # Total de vendas
    col_vendas = colunas.get('col_vendas')
    resultados['total_vendas'] = df[col_vendas].sum() if col_vendas and col_vendas in df.columns else None
    # Número de dias
    col_data = colunas.get('col_data')
    resultados['numero_dias'] = df[col_data].nunique() if col_data and col_data in df.columns else None
    # Vendas por dia
    if resultados['total_vendas'] is not None and resultados['numero_dias']:
        resultados['vendas_por_dia'] = resultados['total_vendas'] / resultados['numero_dias']
    else:
        resultados['vendas_por_dia'] = None
    # Top estados
    col_estado = colunas.get('col_estado')
    if col_estado and col_vendas and col_estado in df.columns and col_vendas in df.columns:
        resultados['top_estados'] = df.groupby(col_estado)[col_vendas].sum().nlargest(5)
        resultados['total_estados'] = len(df[col_estado].dropna().unique())
    else:
        resultados['top_estados'] = None
        resultados['total_estados'] = None
    # Top clientes
    col_cliente = colunas.get('col_cliente')
    if col_cliente and col_vendas and col_cliente in df.columns and col_vendas in df.columns:
        resultados['top_clientes'] = df.groupby(col_cliente)[col_vendas].sum().nlargest(5)
        resultados['total_clientes'] = len(df[col_cliente].dropna().unique())
    else:
        resultados['top_clientes'] = None
        resultados['total_clientes'] = None
    # Top produtos
    col_produto = colunas.get('col_produto')
    if col_produto and col_vendas and col_produto in df.columns and col_vendas in df.columns:
        resultados['top_produtos'] = df.groupby(col_produto)[col_vendas].sum().nlargest(5)
        resultados['total_produtos'] = len(df[col_produto].dropna().unique())
    else:
        resultados['top_produtos'] = None
        resultados['total_produtos'] = None
    # Top vendedores
    col_vendedor = colunas.get('col_vendedor')
    if col_vendedor and col_vendas and col_vendedor in df.columns and col_vendas in df.columns:
        resultados['top_vendedores'] = df.groupby(col_vendedor)[col_vendas].sum().nlargest(5)
        resultados['total_vendedores'] = len(df[col_vendedor].dropna().unique())
    else:
        resultados['top_vendedores'] = None
        resultados['total_vendedores'] = None
    # Vendas por canal
    col_canal_venda = colunas.get('col_canal_venda')
    if col_canal_venda and col_vendas and col_canal_venda in df.columns and col_vendas in df.columns:
        resultados['vendas_por_canal'] = df.groupby(col_canal_venda)[col_vendas].sum()
    else:
        resultados['vendas_por_canal'] = None
    # Vendas por categoria
    col_categoria_produto = colunas.get('col_categoria_produto')
    if col_categoria_produto and col_vendas and col_categoria_produto in df.columns and col_vendas in df.columns:
        resultados['vendas_por_categoria'] = df.groupby(col_categoria_produto)[col_vendas].sum()
    else:
        resultados['vendas_por_categoria'] = None
    # Vendas por mês
    col_mes = colunas.get('col_mes')
    if col_mes and col_vendas and col_mes in df.columns and col_vendas in df.columns:
        resultados['vendas_por_mes'] = df.groupby(col_mes)[col_vendas].sum()
    else:
        resultados['vendas_por_mes'] = None
    # Vendas por dia da semana
    col_dia_semana = colunas.get('col_dia_semana')
    if col_dia_semana and col_vendas and col_dia_semana in df.columns and col_vendas in df.columns:
        resultados['vendas_por_dia_semana'] = df.groupby(col_dia_semana)[col_vendas].sum()
    else:
        resultados['vendas_por_dia_semana'] = None
    # Receita bruta/liquida
    col_receita_bruta = colunas.get('col_receita_bruta')
    col_receita_liquida = colunas.get('col_receita_liquida')
    resultados['receita_bruta'] = df[col_receita_bruta].sum() if col_receita_bruta and col_receita_bruta in df.columns else None
    resultados['receita_liquida'] = df[col_receita_liquida].sum() if col_receita_liquida and col_receita_liquida in df.columns else None
    # Total impostos
    col_impostos = colunas.get('col_impostos')
    resultados['total_impostos'] = df[col_impostos].sum() if col_impostos and col_impostos in df.columns else None
    # Lucro bruto
    col_lucro_bruto = colunas.get('col_lucro_bruto')
    resultados['lucro_bruto'] = df[col_lucro_bruto].sum() if col_lucro_bruto and col_lucro_bruto in df.columns else None
    # Lucro líquido
    col_lucro_liquido = colunas.get('col_lucro_liquido')
    resultados['lucro_liquido'] = df[col_lucro_liquido].sum() if col_lucro_liquido and col_lucro_liquido in df.columns else None
    # Vendas por forma de pagamento
    col_forma_pagamento = colunas.get('col_forma_pagamento')
    if col_forma_pagamento and col_vendas and col_forma_pagamento in df.columns and col_vendas in df.columns:
        resultados['vendas_por_pagamento'] = df.groupby(col_forma_pagamento)[col_vendas].sum()
    else:
        resultados['vendas_por_pagamento'] = None

    # Vendas por segmento
    col_segmento = colunas.get('col_segmento')
    if col_segmento and col_vendas and col_segmento in df.columns and col_vendas in df.columns:
        resultados['vendas_por_segmento'] = df.groupby(col_segmento)[col_vendas].sum()
    else:
        resultados['vendas_por_segmento'] = None

    # Agrupamento semanal
    if col_data and col_vendas and col_data in df.columns and col_vendas in df.columns:
        resultados['df_semanal'] = df.set_index(col_data).resample("W")[col_vendas].sum()
    else:
        resultados['df_semanal'] = None

    # Dados suficientes para relatório
    dados_suficientes = (
        col_vendas and col_data and
        resultados['total_vendas'] is not None and
        resultados['numero_dias'] is not None and
        resultados['numero_dias'] > 0
    )
    resultados['dados_suficientes'] = dados_suficientes

    # Geração do prompt do relatório
    if dados_suficientes:
        resultados['report'] = f'''
        Você é um analista de BI sênior. Gere um relatório analítico em Markdown, com foco executivo, para apresentação a gestores de empresas. O relatório deve conter:

        1. **Resumo Executivo**: Destaque os principais resultados e tendências do período.
        2. **Período de Análise**: Informe datas de início e fim.
        3. **Visão Geral das Vendas**: Total, média diária, ticket médio, principais canais e produtos.
        
        4. **Tendências e Sazonalidades**: Analise padrões semanais/mensais, picos e quedas.
        5. **Ranking de Estados e Segmentos**: Apresente os Top-5 estados e segmentos com gráficos e tabelas.
        
        6. **Insights Acionáveis**: Três recomendações estratégicas para o time comercial e marketing, baseadas nos dados.
        7. **Riscos e Oportunidades**: Identifique possíveis gargalos, oportunidades de expansão e pontos de atenção.
        8. **Conclusão**: Resuma o panorama e sugira próximos passos.

        Utilize linguagem clara, objetiva e profissional. Estruture o texto com títulos, subtítulos, listas e tabelas. Destaque valores relevantes em negrito e use bullet points para recomendações.

        ### Dados

        Total vendas: {resultados['total_vendas']:,.2f}
        Vendas por dia: {resultados['vendas_por_dia']:,.2f}
        Top Estados: {resultados['top_estados'].to_dict() if resultados['top_estados'] is not None else 'N/D'}
        Vendas por semana: {resultados['df_semanal'].to_dict() if resultados['df_semanal'] is not None else 'N/D'}
        '''
    else:
        resultados['report'] = None

    return resultados
