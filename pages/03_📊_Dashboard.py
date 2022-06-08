import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(page_icon="📊", page_title="Dashboard", layout="wide")
st.title("Incremento médio por cliente")
chart_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['Distribuição', 'Controlo'])

st.line_chart(chart_data)