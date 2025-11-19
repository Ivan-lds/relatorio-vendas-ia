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
