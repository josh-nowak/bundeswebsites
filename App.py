import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Bundeswebsites",
    page_icon="🏛️",
    layout="wide",
)


@st.cache_data(ttl=3600)  # Cache data for 1 hour
def load_data(file_path):
    """Load data from CSV file with caching."""
    return pd.read_csv(file_path)


@st.cache_data  # Cache filtered data
def filter_reachable_urls(dataframe):
    """Filter dataframe to only include reachable URLs."""
    return dataframe[dataframe["final_status"].isin(["200", "202"])]


df = load_data("bundeswebsites.csv")
df_only_reachable_urls = filter_reachable_urls(df)


st.title("Bundeswebsites")

st.markdown(
    "Quelle: [Antwort auf eine Kleine Anfrage zur IT des Bundes](https://dserver.bundestag.de/btd/20/150/2015028.pdf) vom 20.02.2025"
)

only_reachable = st.checkbox("Nur erreichbare Websites anzeigen", value=True)
if only_reachable:
    st.write(df_only_reachable_urls.loc[:, ["url", "title", "description"]])
else:
    st.write(df.loc[:, ["url", "title", "description"]])
