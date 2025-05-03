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

st.write(
    "Die folgende Tabelle zeigt aktuelle und ehemalige Websites des Bundes, die in der Antwort auf eine [Kleine Anfrage](https://dserver.bundestag.de/btd/20/150/2015028.pdf) vom 20.02.2025 dokumentiert wurden."
)

only_reachable = st.checkbox("Nur erreichbare Websites anzeigen", value=True)
advanced = st.checkbox("Erweiterte Ansicht", value=False)

df_view = df.copy()

if only_reachable:
    df_view = df_view[df_view["final_status"] == "200"]

if not advanced:
    df_view = df_view.loc[:, ["ressort", "url", "title", "description"]]

st.write(df_view)

st.markdown("""Erklärung der Spalten:  
- **ressort**: Ressort, dem die Website zugeordnet ist
- **url**: URL der Website
- **title**: Titel der Website (lt. Title-Tag)
- **description**: Beschreibung der Website (lt. Meta-Description-Tag)
- **final_status**: HTTP-Statuscode der Website zum Zeitpunkt der Abfrage
- **hreflang**: Alternative Sprachversionen der Website (lt. Alternate-Link-Tags)
- **canonical_url**: Kanonische URL der Website (lt. Canonical-Link-Tag)
- **uses_gsb**: Gibt an, ob die Website mit dem Government Site Builder erstellt wurde (lt. Generator-Tag)""")
