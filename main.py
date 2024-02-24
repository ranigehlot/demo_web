import streamlit as st

import pandas as pd

#dataset=pd.read_csv("data")


st.title("welcome to my website")
st.header("python")
st.subheader("Mearnstack")
st.code ("""print("hello")""")


data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

st.dataframe(data)


name=st.text_input("Enter Your name: ")
fname=st.text_input("Enter Your father name: ")
adr=st.text_area("Enter Your address: ")
classdata=st.selectbox("Enter Your class name:",(1,2,3,4,5,6,7,8,9,10,11,12))


button=st.button("Done")
if button:
    st.markdown(f"""
    name :{name}
    fahter name :{fname}
    address :{adr}
    class :{classdata}
""")