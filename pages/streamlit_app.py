import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# url = "https://docs.google.com/spreadsheets/d/11rAxWN1wftay-bIpcMB3NsjgLkgg4Sw8LFAt49cyC_k/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(worksheet="Sheet2",usecols=list(range(4)),  ttl=5)
data = data.dropna(how="all")

with st.form(key='personal_form'):
    person_name=st.text_input(label='Name*')
    age=st.number_input(label='Age*',step=1,value=None)
    phone_number=st.number_input(label='Phone No.',step=1,value=None)
    aadhar=st.number_input(label='Aadhar No. *',step=1,value=None)
    st.markdown("**required*")
    submit_button=st.form_submit_button(label='Submit the form')

    if submit_button:
        if not person_name or not age or not aadhar:
            st.warning("Ensure all mandatory fields are filled.")
            st.stop()
        elif data["Name"].str.contains(person_name).any():
            st.warning("Another person with same name already exists.")
            st.stop()
        else:
            person_data=pd.DataFrame(
                [
                    {
                        "Name": person_name,
                        "Age": age,
                        "Phone": phone_number,
                        "Aadhar": aadhar,
                    }
                ]
            )

            updated_df=pd.concat([data,person_data], ignore_index=True)

            conn.update(worksheet="Sheet2",data=updated_df)

            st.success("All details are successfully submited!")



