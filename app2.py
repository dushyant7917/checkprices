import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="Check Prices", page_icon="🤑")

st.markdown("""
<style>
#MainMenu {
  display: none;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def get_data():
    # Read CSV file into a DataFrame
    df = pd.read_csv("jawline_exercise_tools_data.csv")  # Replace with your CSV file path
    return df

df = get_data()

def get_html_table(df):
    # Create HTML table with clickable links
    html_table = "<h1>Jawline Exercise Tools</h1><br><br>"
    cols = df.columns.tolist()
    for col in cols:
        if col == "Link":
            continue
        html_table += f"<th>{col}</th>"

    for _, row in df.iterrows():
        row_html = "<tr>"
        for col in cols:
            if col == "Link":
                continue
            if col == "Name":
               row_html += f"<td><a href='{row['Link']}'>{row[col]}</a></td>"
            else:
                row_html += f"<td>{row[col]}</td>"
        row_html += "</tr>"
        html_table += f"<tr>{row_html}</tr>"

    html_table = f"<table>{html_table}</table>"
    return html_table

def display_table(html_table):
    st.markdown(html_table, unsafe_allow_html=True)

# Define the different pages of your app
def page1():
    global df
    df = df.sort_values(by=["Price per unit (INR)"], ascending=True)
    html_table = get_html_table(df)
    display_table(html_table)

def page2():
    global df
    df = df.sort_values(by=["Weight per piece (g)"], ascending=True)
    html_table = get_html_table(df)
    display_table(html_table)

def page3():
    global df
    df = df.sort_values(by=["Rating (out of 5)"], ascending=False)
    html_table = get_html_table(df)
    display_table(html_table)

def page4():
    global df
    df = df.sort_values(by=["Number of people rated"], ascending=False)
    html_table = get_html_table(df)
    display_table(html_table)

tabs = st.tabs(["Sort by 'Price per unit'", "Sort by 'Weight per unit'", "Sort by 'Rating'", "Sort by 'Number of ratings'"])

with tabs[0]:
    page1()
with tabs[1]:
    page2()
with tabs[2]:
    page3()
with tabs[3]:
    page4()
