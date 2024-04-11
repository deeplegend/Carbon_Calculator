# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/11rAxWN1wftay-bIpcMB3NsjgLkgg4Sw8LFAt49cyC_k/edit?usp=sharing"

conn = st.experimental_connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url,ttl=5)
st.dataframe(data)