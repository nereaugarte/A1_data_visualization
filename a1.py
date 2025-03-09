import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import time
import pandas as pd


sheet_url = "https://docs.google.com/spreadsheets/d/1CKKyRQ43ufbyo8_4t2N-bQNQWQQ273iD7RA57X7lOKo/export?format=csv"

def load_titanic_data():
    try:
        df = pd.read_csv(sheet_url)
        return df
    except Exception as e:
        st.error(f"Error fetching data from Google Sheets: {e}")
        return pd.DataFrame()


# Business Question
st.title("A/B Test: Which Chart Helps Answer the Question Better?")
st.subheader("What proportion of Titanic passengers survived?")

# Initialize session state variables
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "chart_type" not in st.session_state:
    st.session_state.chart_type = None

# Button to Show Chart
if st.button("Show Chart"):
    st.session_state.start_time = time.time()  # Start time tracking
    st.session_state.chart_type = random.choice(["bar", "pie"])

    # Load Titanic data from Google Sheets
    data = load_titanic_data()

    if not data.empty:  # Ensure data is loaded before plotting
        survival_counts = data["Survived"].value_counts()

        if st.session_state.chart_type == "bar":
            st.subheader("Chart A: Bar Chart of Survival")
            fig, ax = plt.subplots(figsize=(5, 3))
            ax.bar(["Did not survive", "Survived"], survival_counts, color=["pink", "blue"])
            plt.xlabel("Survival Status")
            plt.ylabel("Number of Passengers")
            plt.title("Titanic Survival Counts (Bar Chart)")
            st.pyplot(fig)
        else:
            st.subheader("Chart B: Pie Chart of Survival")
            fig, ax = plt.subplots(figsize=(5, 3))
            ax.pie(survival_counts, labels=["Did not survive", "Survived"], autopct='%1.1f%%', colors=["pink", "blue"])
            plt.title("Titanic Survival Distribution (Pie Chart)")
            st.pyplot(fig)
    else:
        st.error("Could not load Titanic data. Please check your Google Sheets setup.")

# Button to Record Response Time
if st.session_state.start_time is not None:
    if st.button("I answered your question"):
        elapsed_time = round(time.time() - st.session_state.start_time, 2)
        st.write(f"You took {elapsed_time} seconds to answer.")
