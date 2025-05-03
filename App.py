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


df = load_data("bundeswebsites.csv")


st.title("Bundeswebsites")

st.markdown(
    "Quelle: [Antwort auf eine Kleine Anfrage zur IT des Bundes](https://dserver.bundestag.de/btd/20/150/2015028.pdf) vom 20.02.2025"
)

only_reachable = st.checkbox("Nur erreichbare Websites anzeigen", value=True)
advanced = st.checkbox("Erweiterte Ansicht", value=False)

df_view = df.copy()

if only_reachable:
    df_view = df_view[df_view["final_status"] == "200"]

if not advanced:
    df_view = df_view.loc[:, ["ressort", "url", "title", "description"]]

st.write(df_view)
