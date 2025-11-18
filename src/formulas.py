# Módulo de catálogo de fórmulas do Excel
import streamlit as st

FORMULAS = {
    "Estatísticas": [
        {
            "nome": "SOMA",
            "formula": "=SOMA(A1:A10)",
            "descricao": "Soma um conjunto de valores",
            "exemplo": "=SOMA(B2:B100) soma todos os valores no intervalo",
            "categoria": "Estatísticas"
        },
        {
            "nome": "MÉDIA",
            "formula": "=MÉDIA(A1:A10)",
            "descricao": "Calcula a média aritmética de um conjunto de números",
            "exemplo": "=MÉDIA(B2:B100) retorna a média dos valores na coluna B",
            "categoria": "Estatísticas"
        },
        {
            "nome": "MEDIANA",
            "formula": "=MEDIANA(A1:A10)",
            "descricao": "Retorna o valor mediano (valor do meio) de um conjunto de números",
            "exemplo": "=MEDIANA(C2:C50) encontra o valor central da distribuição",
            "categoria": "Estatísticas"
        },
        {
            "nome": "MODO",
            "formula": "=MODO(A1:A10)",
            "descricao": "Retorna o valor que aparece com mais frequência em um conjunto",
            "exemplo": "=MODO(D2:D200) encontra o valor mais comum",
            "categoria": "Estatísticas"
        },
        {
            "nome": "DESVPAD",
            "formula": "=DESVPAD(A1:A10)",
            "descricao": "Calcula o desvio padrão de uma amostra",
            "exemplo": "=DESVPAD(E2:E100) mede a dispersão dos dados",
            "categoria": "Estatísticas"
        },
        {
            "nome": "VAR",
            "formula": "=VAR(A1:A10)",
            "descricao": "Calcula a variância de uma amostra",
            "exemplo": "=VAR(F2:F80) mede a variabilidade dos dados",
            "categoria": "Estatísticas"
        },
        {
            "nome": "MÁXIMO",
            "formula": "=MÁXIMO(A1:A10)",
            "descricao": "Retorna o maior valor de um conjunto",
            "exemplo": "=MÁXIMO(G2:G500) encontra o valor máximo",
            "categoria": "Estatísticas"
        },
        {
            "nome": "MÍNIMO",
            "formula": "=MÍNIMO(A1:A10)",
            "descricao": "Retorna o menor valor de um conjunto",
            "exemplo": "=MÍNIMO(H2:H500) encontra o valor mínimo",
            "categoria": "Estatísticas"
        },
        {
            "nome": "CONT.VALORES",
            "formula": "=CONT.VALORES(A1:A10)",
            "descricao": "Conta o número de células que contêm valores numéricos",
            "exemplo": "=CONT.VALORES(I2:I100) conta quantas células têm números",
            "categoria": "Estatísticas"
        },
        {
            "nome": "CONT.SE",
            "formula": "=CONT.SE(A1:A10,\">100\")",
            "descricao": "Conta células que atendem a um critério específico",
            "exemplo": "=CONT.SE(J2:J200,\">500\") conta valores maiores que 500",
            "categoria": "Estatísticas"
        },
        {
            "nome": "SOMASE",
            "formula": "=SOMASE(A1:A10,\">100\",B1:B10)",
            "descricao": "Soma valores que atendem a um critério específico",
            "exemplo": "=SOMASE(K2:K100,\">1000\",L2:L100) soma valores de L onde K>1000",
            "categoria": "Estatísticas"
        },
        {
            "nome": "MÉDIASE",
            "formula": "=MÉDIASE(A1:A10,\">50\",B1:B10)",
            "descricao": "Calcula a média de valores que atendem a um critério",
            "exemplo": "=MÉDIASE(M2:M100,\">0\",N2:N100) média de N onde M>0",
            "categoria": "Estatísticas"
        }
    ],
    "Texto": [
        {
            "nome": "CONCATENAR",
            "formula": "=CONCATENAR(A1,\" \",B1)",
            "descricao": "Combina múltiplos textos em uma única célula",
            "exemplo": "=CONCATENAR(A2,\" \",B2) une o conteúdo de A2 e B2",
            "categoria": "Texto"
        },
        {
            "nome": "& (Operador)",
            "formula": "=A1&\" \"&B1",
            "descricao": "Operador para concatenar textos (mais simples que CONCATENAR)",
            "exemplo": "=A2&\" - \"&B2 une textos com separador",
            "categoria": "Texto"
        },
        {
            "nome": "ESQUERDA",
            "formula": "=ESQUERDA(A1,5)",
            "descricao": "Extrai caracteres do início de um texto",
            "exemplo": "=ESQUERDA(C2,3) retorna os 3 primeiros caracteres",
            "categoria": "Texto"
        },
        {
            "nome": "DIREITA",
            "formula": "=DIREITA(A1,5)",
            "descricao": "Extrai caracteres do final de um texto",
            "exemplo": "=DIREITA(D2,4) retorna os 4 últimos caracteres",
            "categoria": "Texto"
        },
        {
            "nome": "MEIO",
            "formula": "=MEIO(A1,2,5)",
            "descricao": "Extrai caracteres do meio de um texto",
            "exemplo": "=MEIO(E2,3,6) extrai 6 caracteres a partir da posição 3",
            "categoria": "Texto"
        },
        {
            "nome": "MAIÚSCULA",
            "formula": "=MAIÚSCULA(A1)",
            "descricao": "Converte texto para letras maiúsculas",
            "exemplo": "=MAIÚSCULA(F2) converte todo o texto para maiúsculas",
            "categoria": "Texto"
        },
        {
            "nome": "MINÚSCULA",
            "formula": "=MINÚSCULA(A1)",
            "descricao": "Converte texto para letras minúsculas",
            "exemplo": "=MINÚSCULA(G2) converte todo o texto para minúsculas",
            "categoria": "Texto"
        },
        {
            "nome": "PRIMEIRA.MAIÚSCULA",
            "formula": "=PRIMEIRA.MAIÚSCULA(A1)",
            "descricao": "Converte a primeira letra de cada palavra para maiúscula",
            "exemplo": "=PRIMEIRA.MAIÚSCULA(H2) formata como título",
            "categoria": "Texto"
        },
        {
            "nome": "PROCURAR",
            "formula": "=PROCURAR(\"texto\",A1)",
            "descricao": "Encontra a posição de um texto dentro de outro",
            "exemplo": "=PROCURAR(\"@\",I2) encontra a posição do @ no email",
            "categoria": "Texto"
        },
        {
            "nome": "SUBSTITUIR",
            "formula": "=SUBSTITUIR(A1,\"antigo\",\"novo\")",
            "descricao": "Substitui texto antigo por novo em uma string",
            "exemplo": "=SUBSTITUIR(J2,\" \",\"-\") substitui espaços por hífens",
            "categoria": "Texto"
        },
        {
            "nome": "TEXTO",
            "formula": "=TEXTO(A1,\"dd/mm/aaaa\")",
            "descricao": "Converte um valor em texto com formato específico",
            "exemplo": "=TEXTO(K2,\"R$ #,##0.00\") formata número como moeda",
            "categoria": "Texto"
        }
    ],
    "Data e Hora": [
        {
            "nome": "HOJE",
            "formula": "=HOJE()",
            "descricao": "Retorna a data atual",
            "exemplo": "=HOJE() retorna a data de hoje",
            "categoria": "Data e Hora"
        },
        {
            "nome": "AGORA",
            "formula": "=AGORA()",
            "descricao": "Retorna data e hora atuais",
            "exemplo": "=AGORA() retorna data e hora completas",
            "categoria": "Data e Hora"
        },
        {
            "nome": "DIA",
            "formula": "=DIA(A1)",
            "descricao": "Extrai o dia de uma data",
            "exemplo": "=DIA(B2) retorna o dia do mês da data em B2",
            "categoria": "Data e Hora"
        },
        {
            "nome": "MÊS",
            "formula": "=MÊS(A1)",
            "descricao": "Extrai o mês de uma data",
            "exemplo": "=MÊS(C2) retorna o mês (1-12) da data em C2",
            "categoria": "Data e Hora"
        },
        {
            "nome": "ANO",
            "formula": "=ANO(A1)",
            "descricao": "Extrai o ano de uma data",
            "exemplo": "=ANO(D2) retorna o ano da data em D2",
            "categoria": "Data e Hora"
        },
        {
            "nome": "DATA",
            "formula": "=DATA(2024,3,15)",
            "descricao": "Cria uma data a partir de ano, mês e dia",
            "exemplo": "=DATA(2024,12,25) cria a data 25/12/2024",
            "categoria": "Data e Hora"
        },
        {
            "nome": "DIA.DA.SEMANA",
            "formula": "=DIA.DA.SEMANA(A1,2)",
            "descricao": "Retorna o dia da semana (1=segunda, 7=domingo)",
            "exemplo": "=DIA.DA.SEMANA(E2,2) retorna 1-7 para dias da semana",
            "categoria": "Data e Hora"
        },
        {
            "nome": "DIATRABALHOTOTAL",
            "formula": "=DIATRABALHOTOTAL(A1,B1)",
            "descricao": "Calcula dias úteis entre duas datas",
            "exemplo": "=DIATRABALHOTOTAL(F2,G2) conta dias úteis excluindo fins de semana",
            "categoria": "Data e Hora"
        }
    ],
    "Financeiro": [
        {
            "nome": "VP",
            "formula": "=VP(taxa,nper,pgto)",
            "descricao": "Calcula o valor presente de um investimento",
            "exemplo": "=VP(0.05,12,-1000) calcula VP com taxa 5%, 12 períodos, pagamento 1000",
            "categoria": "Financeiro"
        },
        {
            "nome": "VF",
            "formula": "=VF(taxa,nper,pgto)",
            "descricao": "Calcula o valor futuro de um investimento",
            "exemplo": "=VF(0.08,10,-500) calcula VF com taxa 8%, 10 períodos, pagamento 500",
            "categoria": "Financeiro"
        },
        {
            "nome": "PGTO",
            "formula": "=PGTO(taxa,nper,vp)",
            "descricao": "Calcula o pagamento periódico de um empréstimo",
            "exemplo": "=PGTO(0.01,24,10000) calcula prestação mensal de empréstimo",
            "categoria": "Financeiro"
        },
        {
            "nome": "TAXA",
            "formula": "=TAXA(nper,pgto,vp)",
            "descricao": "Calcula a taxa de juros de um empréstimo",
            "exemplo": "=TAXA(12,-1000,10000) encontra a taxa para 12 pagamentos",
            "categoria": "Financeiro"
        },
        {
            "nome": "NPER",
            "formula": "=NPER(taxa,pgto,vp)",
            "descricao": "Calcula o número de períodos de um empréstimo",
            "exemplo": "=NPER(0.01,-500,10000) calcula quantos meses para pagar",
            "categoria": "Financeiro"
        },
        {
            "nome": "VPL",
            "formula": "=VPL(taxa,valores)",
            "descricao": "Calcula o valor presente líquido de um investimento",
            "exemplo": "=VPL(0.1,B2:B10) calcula VPL com taxa 10% e fluxos em B2:B10",
            "categoria": "Financeiro"
        },
        {
            "nome": "TIR",
            "formula": "=TIR(valores)",
            "descricao": "Calcula a taxa interna de retorno",
            "exemplo": "=TIR(C2:C20) calcula TIR dos fluxos em C2:C20",
            "categoria": "Financeiro"
        }
    ],
    "Lógica": [
        {
            "nome": "SE",
            "formula": "=SE(A1>100,\"Alto\",\"Baixo\")",
            "descricao": "Retorna um valor se a condição for verdadeira, outro se falsa",
            "exemplo": "=SE(B2>1000,\"Meta atingida\",\"Abaixo da meta\")",
            "categoria": "Lógica"
        },
        {
            "nome": "E",
            "formula": "=E(A1>10,B1<100)",
            "descricao": "Retorna VERDADEIRO se todas as condições forem verdadeiras",
            "exemplo": "=E(C2>50,C2<200) verifica se C2 está entre 50 e 200",
            "categoria": "Lógica"
        },
        {
            "nome": "OU",
            "formula": "=OU(A1>100,B1<50)",
            "descricao": "Retorna VERDADEIRO se pelo menos uma condição for verdadeira",
            "exemplo": "=OU(D2=\"Aprovado\",D2=\"Pendente\") verifica se D2 é Aprovado ou Pendente",
            "categoria": "Lógica"
        },
        {
            "nome": "NÃO",
            "formula": "=NÃO(A1>100)",
            "descricao": "Inverte o valor lógico (VERDADEIRO vira FALSO e vice-versa)",
            "exemplo": "=NÃO(E2=\"Cancelado\") retorna VERDADEIRO se não for Cancelado",
            "categoria": "Lógica"
        },
        {
            "nome": "SEERRO",
            "formula": "=SEERRO(A1/B1,\"Erro\")",
            "descricao": "Retorna um valor se houver erro, caso contrário retorna o resultado",
            "exemplo": "=SEERRO(F2/G2,0) retorna 0 se houver divisão por zero",
            "categoria": "Lógica"
        },
        {
            "nome": "PROCV",
            "formula": "=PROCV(valor,tabela,coluna,aproximado)",
            "descricao": "Procura um valor na primeira coluna e retorna valor de outra coluna",
            "exemplo": "=PROCV(H2,Tabela1,2,FALSO) busca H2 na tabela e retorna coluna 2",
            "categoria": "Lógica"
        },
        {
            "nome": "PROCH",
            "formula": "=PROCH(valor,tabela,linha,aproximado)",
            "descricao": "Procura um valor na primeira linha e retorna valor de outra linha",
            "exemplo": "=PROCH(I2,Tabela1,3,FALSO) busca I2 na tabela e retorna linha 3",
            "categoria": "Lógica"
        },
        {
            "nome": "ÍNDICE",
            "formula": "=ÍNDICE(tabela,linha,coluna)",
            "descricao": "Retorna o valor de uma célula específica em uma tabela",
            "exemplo": "=ÍNDICE(J2:K100,5,2) retorna valor da linha 5, coluna 2",
            "categoria": "Lógica"
        },
        {
            "nome": "CORRESP",
            "formula": "=CORRESP(valor,intervalo,tipo)",
            "descricao": "Retorna a posição de um valor em um intervalo",
            "exemplo": "=CORRESP(L2,M2:M100,0) encontra posição exata de L2 em M2:M100",
            "categoria": "Lógica"
        }
    ],
    "Análise de Dados": [
        {
            "nome": "SOMASES",
            "formula": "=SOMASES(intervalo_soma,intervalo1,critério1,intervalo2,critério2)",
            "descricao": "Soma valores que atendem a múltiplos critérios",
            "exemplo": "=SOMASES(N2:N100,O2:O100,\">100\",P2:P100,\"Aprovado\") soma N onde O>100 e P=\"Aprovado\"",
            "categoria": "Análise de Dados"
        },
        {
            "nome": "CONT.SES",
            "formula": "=CONT.SES(intervalo1,critério1,intervalo2,critério2)",
            "descricao": "Conta células que atendem a múltiplos critérios",
            "exemplo": "=CONT.SES(Q2:Q100,\">500\",R2:R100,\"2024\") conta onde Q>500 e R=2024",
            "categoria": "Análise de Dados"
        },
        {
            "nome": "MÉDIASES",
            "formula": "=MÉDIASES(intervalo_média,intervalo1,critério1,intervalo2,critério2)",
            "descricao": "Calcula média de valores que atendem a múltiplos critérios",
            "exemplo": "=MÉDIASES(S2:S100,T2:T100,\">0\",U2:U100,\"Ativo\") média de S onde T>0 e U=\"Ativo\"",
            "categoria": "Análise de Dados"
        },
        {
            "nome": "PROCV",
            "formula": "=PROCV(valor,tabela,coluna,FALSO)",
            "descricao": "Busca vertical com correspondência exata",
            "exemplo": "=PROCV(V2,TabelaClientes,3,FALSO) busca V2 e retorna coluna 3",
            "categoria": "Análise de Dados"
        },
        {
            "nome": "PROCURARV",
            "formula": "=PROCURARV(valor,tabela,coluna,aproximado)",
            "descricao": "Versão mais recente do PROCV (Excel 365)",
            "exemplo": "=PROCURARV(W2,Tabela1,2,FALSO) busca W2 na tabela",
            "categoria": "Análise de Dados"
        },
        {
            "nome": "AGRUPAR",
            "formula": "=AGRUPAR(valor1,valor2,valor3)",
            "descricao": "Agrupa valores em uma única célula (Excel 365)",
            "exemplo": "=AGRUPAR(X2,X3,X4) combina múltiplos valores",
            "categoria": "Análise de Dados"
        },
        {
            "nome": "FILTRO",
            "formula": "=FILTRO(tabela,condição)",
            "descricao": "Filtra uma tabela baseado em condições (Excel 365)",
            "exemplo": "=FILTRO(Y2:Z100,Y2:Y100>1000) filtra linhas onde Y>1000",
            "categoria": "Análise de Dados"
        },
        {
            "nome": "SOMARPRODUTO",
            "formula": "=SOMARPRODUTO(A1:A10,B1:B10)",
            "descricao": "Multiplica arrays e soma os resultados",
            "exemplo": "=SOMARPRODUTO(AA2:AA100,AB2:AB100) multiplica e soma AA*AB",
            "categoria": "Análise de Dados"
        }
    ]
}


def show_formulas_catalog():
    """Exibe o catálogo de fórmulas do Excel organizado por categorias"""
    st.markdown("## 📚 Catálogo de Fórmulas do Excel")
    st.markdown("---")
    
    # Barra de pesquisa
    search_term = st.text_input("🔍 Pesquisar fórmula:", placeholder="Digite o nome da fórmula ou descrição...")
    
    # Filtro por categoria
    categorias = list(FORMULAS.keys())
    categoria_selecionada = st.selectbox("📂 Filtrar por categoria:", ["Todas"] + categorias)
    
    # Filtrar fórmulas por categoria primeiro
    formulas_filtradas = {}
    
    if categoria_selecionada == "Todas":
        formulas_filtradas = FORMULAS
    else:
        formulas_filtradas = {categoria_selecionada: FORMULAS[categoria_selecionada]}
    
    # Aplicar busca sobre as fórmulas já filtradas por categoria
    if search_term:
        formulas_buscadas = {}
        for categoria, formulas in formulas_filtradas.items():
            filtradas = [
                f for f in formulas 
                if search_term.lower() in f["nome"].lower() 
                or search_term.lower() in f["descricao"].lower()
                or search_term.lower() in f["exemplo"].lower()
            ]
            if filtradas:
                formulas_buscadas[categoria] = filtradas
        formulas_filtradas = formulas_buscadas
    
    # Exibir fórmulas
    if not formulas_filtradas or all(not formulas for formulas in formulas_filtradas.values()):
        st.warning("🔍 Nenhuma fórmula encontrada com os critérios de busca.")
    else:
        for categoria, formulas in formulas_filtradas.items():
            if not formulas:
                continue
                
            st.markdown(f"### 📁 {categoria}")
            
            # Criar cards para cada fórmula
            for i in range(0, len(formulas), 4):
                cols = st.columns(4)
                
                for j, col in enumerate(cols):
                    idx = i + j
                    if idx < len(formulas):
                        formula = formulas[idx]
                        with col:
                            st.markdown(f"""
                            <div style='
                                border: 2px solid #636EFA;
                                border-radius: 12px;
                                padding: 20px;
                                margin-bottom: 16px;
                                background: transparent;
                                min-height: 320px;
                            '>
                                <h3 style='margin-top: 0; font-size: 18px; font-weight: bold;'>{formula['nome']}</h3>
                                <div style='padding: 10px; border-radius: 8px; margin: 10px 0; border-left: 3px solid #636EFA;'>
                                    <code style='color: #636EFA; font-size: 13px; font-weight: bold; word-break: break-all;'>{formula['formula']}</code>
                                </div>
                                <p style='font-size: 14px; margin: 8px 0; line-height: 1.5;'>
                                    <strong>📝 Descrição:</strong><br/>
                                    {formula['descricao']}
                                </p>
                                <p style='font-size: 13px; margin: 8px 0; line-height: 1.5;'>
                                    <strong>💡 Exemplo:</strong><br/>
                                    <code style='color: #ccc; padding: 4px 8px; border-radius: 4px; font-size: 11px; word-break: break-all; display: inline-block; margin-top: 4px;'>{formula['exemplo']}</code>
                                </p>
                            </div>
                            """, unsafe_allow_html=True)
            
            st.markdown("---")
    
    # Seção de dicas
    st.markdown("### 💡 Dicas de Uso")
    st.info("""
    **Dicas importantes:**
    - Use **FALSO** no PROCV para busca exata, **VERDADEIRO** para aproximada
    - Combine fórmulas para análises mais complexas (ex: =SE(SOMASE(...)>1000,"Alto","Baixo"))
    - Use **SEERRO** para evitar erros em fórmulas que podem falhar
    - **SOMASES** e **CONT.SES** são mais poderosos que SOMASE e CONT.SE
    - No Excel 365, prefira **PROCURARV** ao invés de **PROCV**
    """)
    
    # Estatísticas
    total_formulas = sum(len(formulas) for formulas in FORMULAS.values())
    st.markdown(f"### 📊 Estatísticas")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Fórmulas", total_formulas)
    with col2:
        st.metric("Categorias", len(FORMULAS))
    with col3:
        st.metric("Fórmulas por Categoria", round(total_formulas / len(FORMULAS), 1))

