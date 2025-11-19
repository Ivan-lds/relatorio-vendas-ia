# Módulo de planos e preços
import streamlit as st

stripe_public_key = st.secrets.get("STRIPE_PUBLIC_KEY", "")

STRIPE_PAYMENT_LINKS = {
    "basic": "https://buy.stripe.com/00weV6bIufWDgUZfewbsc03",
    "pro": "https://buy.stripe.com/9B63co4g25hZ48d0jCbsc04",
    "enterprise": "https://buy.stripe.com/00weV65k6aCj349aYgbsc05"
}

PLANOS = {
    "basic": {
        "nome": "Básico",
        "preco": 60,
        "ideal": "Ideal para pequenas empresas que estão começando",
        "features": [
            "Dashboards Analíticos",
            "Principais métricas de vendas e desempenho",
            "Suporte por WhatsApp (48h)",
            "Até 150 gerações/mês",
        ]
    },
    "pro": {
        "nome": "Profissional",
        "preco": 120,
        "ideal": "Ideal para negócios em crescimento que precisam de mais suporte",
        "features": [
            "Dashboards Analíticos",
            "Principais métricas de vendas e desempenho",
            "Suporte por WhatsApp (24h)",
            "Até 450 gerações/mês",
            "Consultoria mensal (1h)",
        ]
    },
    "enterprise": {
        "nome": "Enterprise",
        "preco": 180,
        "ideal": "Ideal para empresas consolidadas que precisam de soluções completas",
        "features": [
            "Dashboards Analíticos",
            "Principais métricas de vendas e desempenho",
            "Suporte por WhatsApp (4h)",
            "Gerações ilimitadas",
            "Consultoria mensal (remoto - sob demanda)",
            "Treinamento da equipe (remoto)"
        ]
    }
}


def show_pricing():
    st.markdown("## Planos e Preços")
    st.markdown("Escolha o plano ideal para seu negócio")
    
    cols = st.columns(3)
    
    for i, (plano_id, plano) in enumerate(PLANOS.items()):
        with cols[i]:
            st.markdown(f"""
            <div style='border:2px solid #636EFA; border-radius:12px; padding:20px; margin-bottom:16px; min-height:480px; height: 600px; display:flex; flex-direction:column; justify-content:space-between;'>
                <h3 style='text-align:center;'>{plano['nome']}</h3>
                <h2 style='text-align:center; color:#636EFA;'>R$ {plano['preco']}/mês</h2>
                <ul style='padding-left:18px;'>
                    {''.join([f'<li>{feature}</li>' for feature in plano['features']])}
                </ul>
                <h4 style='text-align:center; color:#999; font-size:14px;'>{plano['ideal']}</h4>
                <div style='text-align:center; margin-top:16px;'>
                    <a href='{STRIPE_PAYMENT_LINKS[plano_id]}' target='_blank'>
                        <button style='background:#636EFA; color:white; border:none; border-radius:6px; padding:10px 24px; font-size:16px;'>Assinar Plano</button>
                    </a>
                </div>
                <p style='text-align:center; color:#888; font-size:13px;'>Pagamento 100% seguro via Stripe</p>
            </div>
            """, unsafe_allow_html=True)
        
    # end for

    # Seção de FAQ (Perguntas Frequentes) - exibida uma vez abaixo dos cards
    st.markdown("---")
    st.markdown("### Perguntas Frequentes")

    FAQ = [
        {
            "q": "Por que sua plataforma é melhor que usar Excel?",
            "a": "Nossa plataforma automatiza a preparação dos dados, calcula KPIs relevantes, gera dashboards interativos e produz um relatório executivo pronto para apresentação — tudo em minutos e sem montar tabelas-pivô ou fórmulas manualmente. Isso reduz erros, economiza tempo e entrega recomendações acionáveis que o Excel sozinho não fornece sem muito trabalho." 
        },
        {
            "q": "Por que eu devo pagar por isso?",
            "a": "Você paga por tempo e decisão. Em vez de gastar horas preparando relatórios, sua equipe recebe insights prontos para agir. Identificar produtos com baixa margem, canais ineficientes ou oportunidades de aumento de receita frequentemente traz retorno superior ao custo da assinatura." 
        },
        {
            "q": "Como a IA é usada aqui? Posso confiar nos relatórios gerados?",
            "a": "A IA (quando configurada) é usada apenas para transformar métricas tratadas em um relatório executivo claro. Os cálculos e visualizações são feitos sobre dados já processados pela plataforma — isso torna os resultados mais confiáveis que um texto gerado sem contexto. Você sempre pode revisar, exportar e validar os dados antes de tomar decisões." 
        },
        {
            "q": "Quais dados eu preciso enviar?",
            "a": "Basta um CSV ou Excel com pelo menos coluna de Data e Vendas. Quanto mais colunas (cliente, produto, estado, canal, forma de pagamento), mais análises e segmentações automáticas você receberá." 
        },
        {
            "q": "Meus dados estarão seguros?",
            "a": "Os uploads são processados pela infraestrutura do app e pagamentos são realizados via Stripe (seguro). Não usamos seus dados para treinar modelos públicos sem consentimento; podemos formalizar acordos de privacidade/NDA para clientes Enterprise." 
        },
        {
            "q": "O que significam 'gerações/mês' nos planos?",
            "a": "Refere-se ao número de análises/relatórios automáticos permitidos por mês. É um controle de uso pensado para garantir performance e custo previsível. Para necessidades maiores, o plano Enterprise permite acordos personalizados ou geração ilimitada conforme contrato." 
        },
        {
            "q": "Vocês fazem integração com meu ERP/CRM?",
            "a": "Atualmente aceitamos upload de CSV/XLSX. Para clientes Enterprise podemos planejar integrações customizadas para automatizar importações (via API, banco ou conexão direta)." 
        },
        {
            "q": "Posso testar antes de assinar?",
            "a": "Sim — oferecemos demonstrações e há garantia para os templates (7 dias). Para planos podemos criar trials comerciais conforme estratégia de vendas; entre em contato pelo WhatsApp para combinar uma demo rápida." 
        }
    ]

    for item in FAQ:
        with st.expander(item['q'], expanded=False):
            st.markdown(item['a'])
