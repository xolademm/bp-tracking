"""
It says import streamlit could not be resolved on my code so I do not know how it'll show on yours,
but i just run [streamlit run webapp.py] in my terminal so it works on the local host just fine.
I also used pandas for my tabular data
"""

import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt

st.title("Yasmeen's Daily Health Tracker :)")

# Collect today's input
with st.form("health_form"):
    date = st.date_input("Date", datetime.date.today())
    bp_taken = st.radio("Did you take your BP today?", ["YES", "NO"])
    systolic = st.number_input("Systolic", min_value=0)
    diastolic = st.number_input("Diastolic", min_value=0)
    activity = st.number_input("Minutes of physical activity", min_value=0)
    medication = st.radio("Did you take your medication today?", ["YES", "NO"])

    reason = None
    if medication == "NO":
        reason = st.selectbox("Why did you not take the medication?",
                              ["Forgot", "Ran out", "Felt fine", "Side effects"])

    submitted = st.form_submit_button("Submit")

if "data" not in st.session_state:
    st.session_state.data = []

if submitted:
    st.success("Data submitted!")
    st.session_state.data.append({
        "Date": date,
        "Systolic": systolic,
        "Diastolic": diastolic,
        "Activity": activity,
        "BP Taken": bp_taken,
        "Medication Taken": medication,
        "Reason": reason
    })

# Show historical data & plot
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.write("## Health Data")
    st.dataframe(df)

    st.write("## Weekly Trend")
    fig, ax = plt.subplots()
    df_week = df.tail(7).copy()
    df_week["Entry"] = range(1,len(df_week) + 1)
    ax.plot(df_week["Entry"], df_week["Systolic"], label="Systolic")
    ax.plot(df_week["Entry"], df_week["Diastolic"], label="Diastolic")
    ax.plot(df_week["Entry"], df_week["Activity"], label="Activity")
    ax.set_xlabel("Entry Number")
    ax.set_ylabel("Values")
    ax.legend()
    st.pyplot(fig)
