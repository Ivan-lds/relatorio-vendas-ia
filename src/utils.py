# Funções utilitárias para detecção de colunas e manipulação de DataFrame
import pandas as pd

def detectar_coluna(df, possiveis_nomes):
    lower_to_actual = {c.lower(): c for c in df.columns}
    for nome in possiveis_nomes:
        if nome in lower_to_actual:
            return lower_to_actual[nome]
    for nome in possiveis_nomes:
        for col in df.columns:
            if nome.lower() == col.lower():
                return col
    return None

# Função para conversão condicional de tipos
def converter_tipos(df, col_data, col_vendas):
    if col_data and col_data in df.columns:
        df[col_data] = pd.to_datetime(df[col_data], dayfirst=True, errors="coerce")
    if col_vendas and col_vendas in df.columns:
        df[col_vendas] = pd.to_numeric(df[col_vendas], errors="coerce")
    return df
