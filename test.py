import streamlit as st
import pandas as pd

df = pd.DataFrame({'a':['uno','due','tre'], 'b':[1,2,3]})

st.write(df)
st.write('ok')