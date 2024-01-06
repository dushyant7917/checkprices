import pandas as pd
import streamlit as st

st.set_page_config(layout="wide", page_title="Check Prices", page_icon="🤑")

st.title("Jawline Exercise Tools")
st.markdown("- Click on the column header to sort the table by that column.")
st.markdown("- Double click on any URL/link to open it.")
st.markdown("- Use the sidebar to filter the table rows.")

@st.cache_data
def load_data():
    data = pd.read_csv("jawline_exercise_tools_data.csv")
    return data

df = load_data()

# set up sidebar
price_range = st.sidebar.slider(
    "Select 'Price per unit' range",
    float(df['Price per unit (INR)'].min()),
    float(df['Price per unit (INR)'].max()),
    (float(df['Price per unit (INR)'].min()), float(df['Price per unit (INR)'].max()))
)
weight_range = st.sidebar.slider(
    "Select 'Weight per piece' range",
    float(df['Weight per piece (g)'].min()),
    float(df['Weight per piece (g)'].max()),
    (float(df['Weight per piece (g)'].min()), float(df['Weight per piece (g)'].max()))
)
name_filter = st.sidebar.text_input("Filter by 'Brand Name'")

filtered_df = df[
    (df['Price per unit (INR)'].between(price_range[0], price_range[1])) &
    (df['Weight per piece (g)'].between(weight_range[0], weight_range[1])) &
    (df['Brand Name'].str.contains(name_filter, case=False))
]

st.dataframe(
    filtered_df,
    hide_index=True,
    column_config={
        "Link": st.column_config.LinkColumn(
            help="Double click on the link to open the URL in a new tab.",
        ),
        "Name": st.column_config.Column(
            width=1300,
        )
    },
    height=600,
    width=1500,
)
