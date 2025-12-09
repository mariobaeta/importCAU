import streamlit as st
import math

# Título da aplicação
st.title("Calculadora de Importação Aduaneira")

# Entrada de dados
valor = st.number_input("Valor da mercadoria", min_value=0.0, format="%.2f")
moeda = st.selectbox("Moeda", ["EUR", "Outra"])
taxa_cambio = 1.0

if moeda != "EUR":
    taxa_cambio = st.number_input("Taxa de câmbio para EUR", min_value=0.0, format="%.4f")

peso = st.number_input("Peso da mercadoria (kg)", min_value=0.0, format="%.2f")
transporte = st.selectbox("Modo de transporte", ["Camião", "Aéreo"])

# Valores das taxas
direitos_percentual = st.number_input("Percentual de Direitos Aduaneiros (%)", value=10.0, format="%.2f")
iva_percentual = st.number_input("Percentual de IVA (%)", value=23.0, format="%.2f")

# Conversão para euro se necessário
valor_euro = valor * taxa_cambio

# Cálculo do valor aduaneiro
valor_aduaneiro = valor_euro

# Cálculo de taxas optativas por transporte (por blocos de 100 kg)
blocos = math.ceil(peso / 100)
if transporte == "Camião":
    taxa_optativa = blocos * 6.75
else:
    taxa_optativa = blocos * 37.40

# Cálculo dos direitos aduaneiros
direitos = (direitos_percentual / 100) * valor_aduaneiro

# Cálculo do IVA sobre valor aduaneiro + direitos + taxa optativa
iva = (iva_percentual / 100) * (valor_aduaneiro + direitos + taxa_optativa)

# Valor total
valor_total = valor_aduaneiro + direitos + taxa_optativa

# Exibição dos resultados
st.subheader("Resultados")
st.write(f"Valor Aduaneiro (EUR): €{valor_aduaneiro:.2f}")
st.write(f"Taxa Optativa ({transporte}, {blocos} bloco(s) de 100kg): €{taxa_optativa:.2f}")
st.write(f"Direitos Aduaneiros ({direitos_percentual}%): €{direitos:.2f}")
st.write(f"**Valor Total a Pagar: €{valor_total:.2f}**")

st.write(f"Direitos Aduaneiros ({direitos_percentual}%): €{direitos:.2f}")
st.write(f"IVA ({iva_percentual}%): €{iva:.2f}")

