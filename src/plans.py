# Módulo de planos e preços
import streamlit as st

stripe_public_key = st.secrets.get("STRIPE_PUBLIC_KEY", "")

STRIPE_PAYMENT_LINKS = {
    "basic": "https://buy.stripe.com/7sY00cbIu8ub6gleasbsc00",
    "pro": "https://buy.stripe.com/bJebIUdQCh0HawB6I0bsc01",
    "enterprise": "https://buy.stripe.com/28EcMYaEq7q77kp9Ucbsc02"
}

PLANOS = {
    "basic": {
        "nome": "Básico",
        "preco": 197,
        "features": [
            "Dashboard básico de vendas",
            "Atualização mensal",
            "Principais métricas",
            "1 usuário",
            "Suporte por email",
            "Até 1000 registros/mês"
        ]
    },
    "pro": {
        "nome": "Profissional",
        "preco": 397,
        "features": [
            "Todas as features do plano básico",
            "Atualização semanal",
            "Análises avançadas",
            "Relatório personalizado",
            "3 usuários",
            "Suporte por WhatsApp",
            "Até 5000 registros/mês",
            "Consultoria mensal (1h)"
        ]
    },
    "enterprise": {
        "nome": "Enterprise",
        "preco": 597,
        "features": [
            "Todas as features do plano profissional",
            "Atualização diária",
            "Dashboard personalizado",
            "Relatórios sob demanda",
            "Usuários ilimitados",
            "Suporte prioritário",
            "Registros ilimitados",
            "Consultoria quinzenal (2h)",
            "Treinamento da equipe"
        ]
    }
}

def show_pricing():
    st.markdown("## 💰 Planos e Preços")
    st.markdown("Escolha o plano ideal para seu negócio")
    
    cols = st.columns(3)
    
    for i, (plano_id, plano) in enumerate(PLANOS.items()):
        with cols[i]:
            st.markdown(f"""
            <div style='border:2px solid #636EFA; border-radius:12px; padding:20px; margin-bottom:16px; min-height:480px; height: 600px; display:flex; flex-direction:column; justify-content:space-between;'>
                <h3 style='text-align:center;'>{plano['nome']}</h3>
                <h2 style='text-align:center; color:#636EFA;'>R$ {plano['preco']}/mês</h2>
                <ul style='padding-left:18px;'>
                    {''.join([f'<li>✅ {feature}</li>' for feature in plano['features']])}
                </ul>
                <div style='text-align:center; margin-top:16px;'>
                    <a href='{STRIPE_PAYMENT_LINKS[plano_id]}' target='_blank'>
                        <button style='background:#636EFA; color:white; border:none; border-radius:6px; padding:10px 24px; font-size:16px;'>Assinar Plano</button>
                    </a>
                </div>
                <p style='text-align:center; color:#888; font-size:13px;'>Pagamento 100% seguro via Stripe</p>
            </div>
            """, unsafe_allow_html=True)
