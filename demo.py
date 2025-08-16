import streamlit as st
import pandas as pd
import numpy as np

st.title("welcome to PIET")
st.subheader("welcome to AIML dept")
st.text("welcome to piet website")
st.write("chose your favrt spot")
spot=st.selectbox("your favrt spot at PIET:",["libraray","netcafe","sports complex "])
st.write("you chose your favrt spot as {spot}")

st.success("enjoy your time at piet")

st.title("event registration")

if st.button("register event"):
    st.success("Event Registration Successful")

add_club=st.checkbox("join  a club")
if add_club:
    st.write("You joined a club")

event_type=st.radio("select a evnt type:",["technicla","culutural","sports"])

role=st.selectbox("chose your role:",["participant","corrdinator","organizer"])

st.write(f"you have selected {role} role")

team_size=st.slider("team size",1,10,4)
st.write(f"you have selected {team_size} team")
st.number_input("enter the team size ",min_value=1,max_value=100,step=1)
name=st.text_input("enter your name")
if name:
    st.write(f"welcome {name} to club")
DOB=st.date_input("select your DOB")
st.write(f"you have selected {DOB} ")

st.title("PIET Sports Club")

col1,col2=st.columns(2)
with col1:
    st.header("cricket")
    st.image("https://www.piet.co.in/wp-content/uploads/2024/10/IMG_2904-scaled.jpg",width=200)
    st.button("vote for cricket")
with col2:
    st.header("football")
    st.image("https://www.piet.co.in/wp-content/uploads/2024/10/IMG_2953-scaled.jpg", width=200)
    st.button("vote for football")

st.sidebar.subheader("PIET Sports Club")
st.sidebar.selectbox("enter your favrt sports",['cricket','football'])
with st.expander("soprts instructions"):
    st.write("""
    1. carry your id card
    2. report to ground 30 min befor game starts
    3. follow all fair play instructions"
    """)
st.markdown(""" welcome to PIET Sports Club""")

file=st.file_uploader("upload your csv file",type="csv")

if file:
    df = pd.read_csv(file)
    st.subheader("Data preview")
    st.dataframe(df)
if file:
    st.dataframe(df.head())
    counts = df.groupby("release_year")["type"].count()
    st.bar_chart(counts)



