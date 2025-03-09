# streamlit_app.py

import streamlit as st

# Create a connection object.
st.write(st.secrets)


conn = st.connection("gsheets", type="gcsheets")

df = conn.read()

st.dataframe(df)