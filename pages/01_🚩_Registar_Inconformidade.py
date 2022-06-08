import streamlit as st
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import io

import datetime

def _max_width_():
    max_width_str = f"max-width: 1800px;"
    st.markdown(
    f"""
    <style>
    .reportview-container .main .block-container{{
    {max_width_str}
    }}
    </style>    
    """,
    unsafe_allow_html=True,
    )
    
st.set_page_config(page_icon="🚩", page_title="Registar Inconformidade", layout="wide")
_max_width_()

st.sidebar.markdown("# Page 2 ❄️")
col1, mid, col2 = st.columns([1,1,20])
with col1:
    st.image('mc_logo.png', width=150)
with col2:
    st.title("Optimização de Entrega de Folhetos" )

st.markdown(
    '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">',
    unsafe_allow_html=True,
)


## Create week options
pd_calendar = pd.read_csv("data/calendar.csv")
pd_calendar = pd_calendar[(pd_calendar["WEEKKEY_FOLHETO"]>=2021031) & (pd_calendar["WEEKKEY_FOLHETO"]<=2022053)]
options = []
for a,s in  pd_calendar.iterrows():
    week = s['WEEKKEY_FOLHETO']
    time_i = datetime.datetime.strptime(str(s['TIME_I']), '%Y%m%d').strftime('%m/%d/%y')
    time_f = datetime.datetime.strptime(str(s['TIME_F']), '%Y%m%d').strftime('%m/%d/%y')
    option = str(f"{week} ({time_i} - {time_f})")
    options.append(option)




c29, c30, c31 = st.columns([1, 3, 1])

with c30:

    st.title("🚩 Registar Incoformidade")
    option = st.selectbox('Semana para previsão', options)
    st.text('Tipo de Semana: AMC')
    st.text('Inicio de Semana: 10-05-22')
    st.text('Fim de Semana: 16-05-22')
    st.subheader('Variáveis e restrições')
    st.number_input('Orçamento:', value=8400, step=1000,disabled =True)
    st.number_input('Custo de Impressão:', value=0.08, step=0.01,disabled =True)
    st.number_input('Número máximo de freguesias(modelo):', value=550, step=10,disabled =True)
    agree = st.checkbox('Excluir freguesias acima da distância minina definida?',disabled =True)
    st.text_input('Freguesias a excluir: ', placeholder="'000000', '000001', etc",disabled =True)
    st.write("##")

col1, col2, col3 = st.columns(3)
with col3:
    st.button('Registar inconformidade')