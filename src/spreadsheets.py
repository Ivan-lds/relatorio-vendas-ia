import streamlit as st

# Dicionário de planilhas organizadas por categoria
PLANILHAS = {
    "Financeiro": [
        {
            "nome": "Controle Financeiro Completo",
            "descricao": "Sistema completo para controle financeiro pessoal ou empresarial com fluxo de caixa, contas a pagar e receber, relatórios e dashboards.",
            "preco": 49.90,
            "caracteristicas": [
                "Fluxo de caixa automatizado",
                "Controle de contas a pagar e receber",
                "Relatórios financeiros mensais e anuais",
                "Dashboard com gráficos interativos",
                "Categorização de despesas",
                "Projeção financeira"
            ],
            "categoria": "Financeiro",
            "formato": "Excel (.xlsx)",
            "link_stripe": "https://buy.stripe.com/5kQeV613Q11J9sx5DWbsc0i" 
        },
        {
            "nome": "Gestão de Orçamento Familiar",
            "descricao": "Planilha intuitiva para gerenciar o orçamento familiar, acompanhar gastos, definir metas de economia e planejar investimentos.",
            "preco": 29.90,
            "caracteristicas": [
                "Controle de receitas e despesas",
                "Categorização de gastos",
                "Metas de economia",
                "Gráficos visuais de acompanhamento",
                "Planilha de investimentos",
                "Relatórios mensais"
            ],
            "categoria": "Financeiro",
            "formato": "Excel (.xlsx)",
            "link_stripe": "https://buy.stripe.com/6oU28keUG6m39sx5DWbsc0h"
        },
        {
            "nome": "Calculadora de Empréstimos e Financiamentos",
            "descricao": "Ferramenta completa para calcular parcelas, juros, valor presente e futuro de empréstimos, financiamentos e investimentos.",
            "preco": 19.90,
            "caracteristicas": [
                "Cálculo de parcelas (PRICE, SAC)",
                "Tabela de amortização completa",
                "Comparador de opções de crédito",
                "Calculadora de investimentos",
                "Simulação de cenários",
                "Fórmulas automatizadas"
            ],
            "categoria": "Financeiro",
            "formato": "Excel (.xlsx)",
            "link_stripe": "https://buy.stripe.com/4gM3co5k64dVfQV9Ucbsc0g"
        }
    ],
    "Vendas": [
        {
            "nome": "Controle de Vendas e Comissões",
            "descricao": "Sistema completo para controle de vendas, cálculo automático de comissões, acompanhamento de metas e performance de vendedores.",
            "preco": 79.90,
            "caracteristicas": [
                "Registro de vendas detalhado",
                "Cálculo automático de comissões",
                "Acompanhamento de metas por vendedor",
                "Dashboard de performance",
                "Relatórios de vendas por período",
                "Análise de produtos mais vendidos"
            ],
            "categoria": "Vendas",
            "formato": "Excel (.xlsx)",
            "link_stripe": "https://buy.stripe.com/5kQdR28wi4dVcEJ3vObsc0f"
        },
        {
            "nome": "CRM Básico em Excel",
            "descricao": "Sistema de gestão de relacionamento com clientes (CRM) em Excel para pequenas e médias empresas.",
            "preco": 59.90,
            "caracteristicas": [
                "Cadastro completo de clientes",
                "Histórico de interações",
                "Pipeline de vendas",
                "Agendamento de follow-ups",
                "Relatórios de oportunidades",
                "Gestão de contatos"
            ],
            "categoria": "Vendas",
            "formato": "Excel (.xlsx)",
            "link_stripe": "https://buy.stripe.com/6oU9AMfYK5hZ8ot7M4bsc0e"
        },
        {
            "nome": "Análise de Vendas com Dashboard",
            "descricao": "Planilha avançada para análise de vendas com múltiplos dashboards, KPIs e métricas de performance.",
            "preco": 89.90,
            "caracteristicas": [
                "Dashboards interativos",
                "Análise de tendências",
                "Segmentação de clientes",
                "Análise de produtos",
                "Previsão de vendas",
                "KPIs automatizados"
            ],
            "categoria": "Vendas",
            "formato": "Excel (.xlsx)",
            "link_stripe": "https://buy.stripe.com/14A3co3bY5hZgUZ7M4bsc0d"
        }
    ],
    "Recursos Humanos": [
        {
            "nome": "Controle de Ponto e Folha de Pagamento",
            "descricao": "Sistema completo para controle de ponto, cálculo de horas trabalhadas e folha de pagamento automatizada.",
            "preco": 99.90,
            "caracteristicas": [
                "Registro de entrada e saída",
                "Cálculo automático de horas extras",
                "Folha de pagamento completa",
                "Cálculo de INSS, IRRF e FGTS",
                "Relatórios de frequência",
                "Banco de horas"
            ],
            "categoria": "Recursos Humanos",
            "formato": "Excel (.xlsx)",
            "link_stripe": "https://buy.stripe.com/aFa5kwfYK6m3gUZ4zSbsc0c"
        },
        {
            "nome": "Gestão de Funcionários e Benefícios",
            "descricao": "Sistema para gestão completa de funcionários, benefícios, férias, afastamentos e avaliações de desempenho.",
            "preco": 69.90,
            "caracteristicas": [
                "Cadastro de funcionários",
                "Controle de férias",
                "Gestão de benefícios",
                "Avaliações de desempenho",
                "Histórico de treinamentos",
                "Relatórios gerenciais"
            ],
            "categoria": "Recursos Humanos",
            "formato": "Excel (.xlsx)",
            "link_stripe": "https://buy.stripe.com/28E3co6oadOvcEJ5DWbsc0b"
        }
    ],
    "Estoque": [
        {
            "nome": "Controle de Estoque Completo",
            "descricao": "Sistema completo para controle de estoque com entrada, saída, inventário, alertas de reposição e relatórios.",
            "preco": 89.90,
            "caracteristicas": [
                "Controle de entrada e saída",
                "Cálculo de estoque atual",
                "Alertas de estoque mínimo",
                "Inventário físico",
                "Valuation de estoque",
                "Relatórios de movimentação"
            ],
            "categoria": "Estoque",
            "formato": "Excel (.xlsx)",
            "link_stripe": "https://buy.stripe.com/aFa7sE8wi5hZawBgiAbsc0a"
        },
        {
            "nome": "Gestão de Fornecedores e Compras",
            "descricao": "Planilha para gestão de fornecedores, controle de compras, cotações e avaliação de fornecedores.",
            "preco": 59.90,
            "caracteristicas": [
                "Cadastro de fornecedores",
                "Controle de pedidos de compra",
                "Sistema de cotações",
                "Avaliação de fornecedores",
                "Histórico de compras",
                "Relatórios de custos"
            ],
            "categoria": "Estoque",
            "formato": "Excel (.xlsx)",
            "link_stripe": "https://buy.stripe.com/3cI7sE3bYcKrdIN9Ucbsc09"
        }
    ],
    "Projetos": [
        {
            "nome": "Gerenciamento de Projetos",
            "descricao": "Ferramenta completa para gerenciamento de projetos com cronograma, controle de tarefas, recursos e prazos.",
            "preco": 79.90,
            "caracteristicas": [
                "Planejamento de tarefas",
                "Cronograma visual (Gantt)",
                "Controle de recursos",
                "Acompanhamento de prazos",
                "Dashboard de status",
                "Relatórios de progresso"
            ],
            "categoria": "Projetos",
            "formato": "Excel (.xlsx)",
            "link_stripe": "https://buy.stripe.com/28E4gsfYKaCjdIN2rKbsc08"
        }
    ],
    "Outros": [
        {
            "nome": "Agenda de Compromissos e Tarefas",
            "descricao": "Sistema completo para organização pessoal e profissional com agenda, lembretes e controle de tarefas.",
            "preco": 24.90,
            "caracteristicas": [
                "Agenda semanal e mensal",
                "Lista de tarefas",
                "Lembretes e prazos",
                "Priorização de atividades",
                "Controle de tempo",
                "Relatórios de produtividade"
            ],
            "categoria": "Outros",
            "formato": "Excel (.xlsx)",
            "link_stripe": "https://buy.stripe.com/3cIfZah2OfWDgUZaYgbsc07"
        },
        {
            "nome": "Controle de Estudos e Aprendizado",
            "descricao": "Planilha para organizar estudos, planejar rotina de aprendizado, acompanhar progresso e definir metas.",
            "preco": 19.90,
            "caracteristicas": [
                "Planejamento de estudos",
                "Controle de horas estudadas",
                "Metas de aprendizado",
                "Acompanhamento de progresso",
                "Calendário de provas",
                "Análise de desempenho"
            ],
            "categoria": "Outros",
            "formato": "Excel (.xlsx)",
            "link_stripe": "https://buy.stripe.com/dRm5kwh2OeSzcEJeasbsc06"
        }
    ]
}


def show_spreadsheets_catalog():
    """Exibe o catálogo de planilhas Excel organizado por categorias"""
    st.markdown("## Catálogo de Planilhas Excel")
    st.markdown("### Planilhas profissionais prontas para uso")
    
    # Barra de pesquisa
    search_term = st.text_input("Pesquisar planilha:", placeholder="Digite o nome da planilha ou descrição...")
    
    # Filtro por categoria
    categorias = list(PLANILHAS.keys())
    categoria_selecionada = st.selectbox("Filtrar por categoria:", ["Todas"] + categorias)
    
    st.markdown("---")
    
    # Filtrar planilhas por categoria primeiro
    planilhas_filtradas = {}
    
    if categoria_selecionada == "Todas":
        planilhas_filtradas = PLANILHAS
    else:
        planilhas_filtradas = {categoria_selecionada: PLANILHAS[categoria_selecionada]}
    
    # Aplicar busca sobre as planilhas já filtradas por categoria
    if search_term:
        planilhas_buscadas = {}
        for categoria, planilhas in planilhas_filtradas.items():
            filtradas = [
                p for p in planilhas 
                if search_term.lower() in p["nome"].lower() 
                or search_term.lower() in p["descricao"].lower()
                or any(search_term.lower() in carac.lower() for carac in p["caracteristicas"])
            ]
            if filtradas:
                planilhas_buscadas[categoria] = filtradas
        planilhas_filtradas = planilhas_buscadas
    
    # Exibir planilhas
    if not planilhas_filtradas or all(not planilhas for planilhas in planilhas_filtradas.values()):
        st.warning("Nenhuma planilha encontrada com os critérios de busca.")
    else:
        for categoria, planilhas in planilhas_filtradas.items():
            if not planilhas:
                continue
                
            st.markdown(f"### {categoria}")
            
            # Criar cards para cada planilha
            for i in range(0, len(planilhas), 3):
                cols = st.columns(3)
                
                for j, col in enumerate(cols):
                    idx = i + j
                    if idx < len(planilhas):
                        planilha = planilhas[idx]
                        with col:
                            # Formatar preço
                            preco_formatado = f"R$ {planilha['preco']:.2f}".replace(".", ",")
                            
                            st.markdown(f"""
                            <div style='
                                border: 2px solid #636EFA;
                                border-radius: 12px;
                                padding: 20px;
                                margin-bottom: 16px;
                                background: transparent;
                                min-height: 480px;
                                display: flex;
                                flex-direction: column;
                                justify-content: space-between;
                            '>
                                <div>
                                    <h3 style='margin-top: 0; font-size: 18px; font-weight: bold; color: #636EFA;'>{planilha['nome']}</h3>
                                    <div style='font-size: 24px; font-weight: bold; color: #28a745; margin: 10px 0;'>
                                        {preco_formatado}
                                    </div>
                                    <p style='font-size: 14px; margin: 12px 0; line-height: 1.5; color: #666;'>
                                        {planilha['descricao']}
                                    </p>
                                    <div style='margin: 15px 0;'>
                                        <strong style='font-size: 13px;'>Características:</strong>
                                        <ul style='font-size: 12px; padding-left: 20px; margin-top: 8px; line-height: 1.6;'>
                                            {''.join([f'<li>{carac}</li>' for carac in planilha['caracteristicas'][:4]])}
                                            {f'<li style="color: #999;"><em>+{len(planilha["caracteristicas"])-4} mais...</em></li>' if len(planilha['caracteristicas']) > 4 else ''}
                                        </ul>
                                    </div>
                                    <p style='font-size: 11px; color: #999; margin-top: 10px;'>
                                        {planilha['formato']}
                                    </p>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            # Botão funcional do Streamlit
                            if planilha.get('link_stripe'):
                                st.markdown(f"""
                                <div style='text-align: center; margin-top: -50px; margin-bottom: 20px;'>
                                    <a href='{planilha['link_stripe']}' target='_blank' style='text-decoration: none;'>
                                        <button style='
                                            background: #636EFA;
                                            color: white;
                                            border: none;
                                            border-radius: 6px;
                                            padding: 12px 24px;
                                            font-size: 15px;
                                            font-weight: bold;
                                            cursor: pointer;
                                            width: 100%;
                                        '>Comprar Agora</button>
                                    </a>
                                </div>
                                """, unsafe_allow_html=True)
                            else:
                                st.button("Comprar Agora", key=f"comprar_{categoria}_{idx}", disabled=True, 
                                         help="Link de compra em breve. Entre em contato para mais informações.")
            
            st.markdown("---")
    
    # Seção de informações
    st.markdown("### Informações Importantes")
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Entrega:**
        - Planilhas enviadas por e-mail após confirmação do pagamento
        - Formato Excel (.xlsx)
        - Compatível com Excel 2010 ou superior
        
        **Suporte:**
        - Vídeo tutorial incluso
        - Manual de uso detalhado
        - Suporte por email (até 30 dias após compra)
        """)
    
    with col2:
        st.info("""
        **Garantia:**
        - 7 dias para testar
        - Reembolso garantido se não atender suas necessidades
        - Planilhas testadas e validadas
        
        **Pagamento:**
        - Pagamento seguro via Stripe
        - Aceita cartão de crédito e PIX
        - Acesso imediato após pagamento
        """)
    
    # Estatísticas
    total_planilhas = sum(len(planilhas) for planilhas in PLANILHAS.values())
    preco_medio = sum(
        sum(p['preco'] for p in planilhas) / len(planilhas) 
        for planilhas in PLANILHAS.values() 
        if planilhas
    ) / len([p for p in PLANILHAS.values() if p])
    
    st.markdown("### Estatísticas")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Planilhas", total_planilhas)
    with col2:
        st.metric("Categorias", len(PLANILHAS))
    with col3:
        st.metric("Preço Médio", f"R$ {preco_medio:.2f}".replace(".", ","))

