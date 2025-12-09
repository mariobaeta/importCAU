import streamlit as st
import math

# Título da aplicação
st.title("Calculadora de Importação Aduaneira")

# ===================== ENTRADA DE DADOS =====================

# Valor da mercadoria
valor = st.number_input("Valor da mercadoria", min_value=0.0, format="%.2f")

# Moeda e câmbio
moeda = st.selectbox("Moeda", ["EUR", "Outra"])
taxa_cambio = 1.0
if moeda != "EUR":
    taxa_cambio = st.number_input("Taxa de câmbio para EUR", min_value=0.0, format="%.4f")

# Peso e transporte
peso = st.number_input("Peso da mercadoria (kg)", min_value=0.0, format="%.2f")
transporte = st.selectbox("Modo de transporte", ["Camião", "Aéreo"])

# Valor do transporte internacional (que conta no valor aduaneiro!)
valor_transporte = st.number_input("Valor do Transporte (se aplicável)", min_value=0.0, format="%.2f")

# Percentuais
direitos_percentual = st.number_input("Percentual de Direitos Aduaneiros (%)", value=10.0, format="%.2f")
iva_percentual = st.number_input("Percentual de IVA (%)", value=23.0, format="%.2f")

# ===================== CÁLCULOS =====================

# Conversão para EUR
valor_mercadoria_euro = valor * taxa_cambio
valor_transporte_euro = valor_transporte * taxa_cambio

# Valor Aduaneiro = mercadoria + transporte
valor_aduaneiro = valor_mercadoria_euro + valor_transporte_euro

# Taxa optativa por blocos de 100kg
blocos = math.ceil(peso / 100)
if transporte == "Camião":
    taxa_optativa = blocos * 6.75
else:
    taxa_optativa = blocos * 37.40

# Direitos Aduaneiros
direitos = (direitos_percentual / 100) * valor_aduaneiro

# IVA sobre: valor aduaneiro + direitos + taxa optativa
iva = (iva_percentual / 100) * (valor_aduaneiro + direitos + taxa_optativa)

# Valor Total a pagar na alfândega
valor_total = valor_aduaneiro + direitos + taxa_optativa

# ===================== RESULTADOS =====================

st.subheader("Resultados")
st.write(f"Valor Aduaneiro (Mercadoria + Transporte): **€{valor_aduaneiro:.2f}**")
st.write(f"Taxa Optativa ({transporte}, {blocos} bloco(s) de 100kg): **€{taxa_optativa:.2f}**")
st.write(f"Direitos Aduaneiros ({direitos_percentual}%): **€{direitos:.2f}**")
st.write(f"IVA ({iva_percentual}%): **€{iva:.2f}**")
st.write("---")
st.write(f"### 💰 Valor Total s/IVA: **€{valor_total:.2f}**")

