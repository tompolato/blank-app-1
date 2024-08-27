import streamlit as st
import pandas as pd
import numpy as np

#importo file collegati
import data_search, statistics_calc
import style

#IMPOSTO LAYAOUT DELLA PAGINA 
st.set_page_config(
    layout="wide",
    page_title="Design Database", 
    initial_sidebar_state = "expanded",
    menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "mailto:office@onesails.com",
        'About': "Descrzione e note di riservatezza"
     }) 

#richiamo funct per stile pagina
style.general_style()


#STRUTTUTO IL SIDEBAR
# Inizializza lo stato della sessione
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Search and Selection"

# Sidebar per la navigazione

if st.sidebar.button("Search & Selection", use_container_width = True):
    st.session_state.current_page = "Search and Selection"
if st.sidebar.button("Statistics", use_container_width = True):
    st.session_state.current_page = "Statistics"
if st.sidebar.button("Structure Comparator", use_container_width = True):
    st.session_state.current_page = "Structure Comparator"
if st.sidebar.button("Shape Comparator", use_container_width = True):
    st.session_state.current_page = "Shape Comparator"
if st.sidebar.button("Single Sail Deep Analyzer", use_container_width = True):
    st.session_state.current_page = "Shape Deep Analyzer"
if st.sidebar.button("FSI Results", use_container_width = True):
    st.session_state.current_page = "FSI Results"
if st.sidebar.button("Pics Shapes", use_container_width = True):
    st.session_state.current_page = "Pics Shapes"


#IMPORTAZIONE DEI DATI DEL FOGLIO GOOGLE DEL DATABASE
from streamlit_gsheets import GSheetsConnection

#url = "https://docs.google.com/spreadsheets/d/g9vuUolxFud-dgTY-juY6IFgtjMHq4uIocHLk5tvX1E/gviz/tq?tqx=out:csv&sheet=303042284"


url = "https://docs.google.com/spreadsheets/d/1g9vuUolxFud-dgTY-juY6IFgtjMHq4uIocHLk5tvX1E/edit?usp=sharing"
conn = st.connection("gsheets", type=GSheetsConnection)
data = conn.read(spreadsheet=url ,worksheet="303042284",header=1 )
#data = pd.read_csv(url)
#st.dataframe(data) #print dataframe per check dati importati Gsheet
#first=data.columns.values
#st.write(first)
df = pd.DataFrame(data, columns= data.columns.values)
#st.write(df)


# Mostra diverse sezioni in base alla pagina selezionata in dashboard
if st.session_state.current_page == "Search and Selection":
    data_search.search_page(df)
elif st.session_state.current_page == "Statistics":
    statistics_calc.statistics_page()
elif st.session_state.current_page == "Structure Comparator":
    st.write("seleziona file pagina structure comparator")

