
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
import altair as alt
st.set_page_config(
    page_title="Impact covid",
    page_icon="✅",
    layout="wide",
)


st.title("Propagation du COVID19 et impact des vaccins")

tab1, tab2,tab3,tab4 = st.tabs(["Découverte du COVID19", "Propagation du COVID19","Evolution du COVID19 et vaccins","Bilan COVID19"])

with tab1:
    st.header("Découverte du COVID19")
    st.image("https://github.com/Project-covid-streamlit/projet_data_Data-storytelling/blob/alimou/date_covid.png?raw=true",width=200)
    st.markdown("<p style='text-align:justify;'>Depuis le 16 novembre 2019,le monde est plongé dans une pandémie qu’on nomme SARS-COV-2 aussi connu sur le nom de Covid-19. En effet, ce virus, qui porte son origine de la ville de Wuhan, dans la province de Hubei en Chine centrale,a très vite conquis une bonne partie du monde,plongeant celui-là dans une angoisse profonde, à la quête de traitement et de solution pour le contrer. De par ses caractéristiques très contagieuses, ce virus a su se propager très rapidement dans nos sociétés, nous obligeant ainsi à réfléchir autrement et à trouver des alternatives afin de pallier cette crise sanitaire.Il faut savoir qu’une personne qui est malade est successible de contaminer 3 personnes en l’absence de mesures de protection.</p>" , unsafe_allow_html=True)
    
    st.image("https://raw.githubusercontent.com/Project-covid-streamlit/projet_data_Data-storytelling/6ca2fcb3982a6df3785215fd4a3a94b6a8bf2a78/wuhan.png", width=200)
    st.markdown("<p style='text-align:justify;'>C'est la ville où a été identifiée le virus 🦠 pour la première fois suite à une vague de personnes malades.</p>",unsafe_allow_html=True)
    
    st.image("https://raw.githubusercontent.com/Project-covid-streamlit/projet_data_Data-storytelling/6ca2fcb3982a6df3785215fd4a3a94b6a8bf2a78/originea.png", width=200)
    
    st.markdown("<p style='text-align:justify;'>Le Covid-19 est un virus qui se transmet relativement,facilement.Il est possible de transmettre cette maladie de trois manières : par projection de postillons (lorsqu’une personne malade tousse ou éternue par exemple),par contact physique direct (une accolade, une bise avec une personne portante du virus pourrait réussir à contaminer une personne saine),et enfin une contamination indirecte via des surfaces ou des objets contaminés par une personne porteuse du virus. </p>",unsafe_allow_html=True)
    

with tab2:
    st.markdown("<h2 style='text-align:center;'>Propagation du COVID19</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>(5 mois!C'est le temps qu'il a fallu au virus pour se propager dans le monde')</h3>",unsafe_allow_html=True)
    
    df_e=pd.read_csv("https://raw.githubusercontent.com/Project-covid-streamlit/projet_data_Data-storytelling/alimou/EXPANSION%20DU%20COVID.csv")
    job_filter = st.select_slider("Date", df_e["Date"].sort_values(ascending=True))
    df_e = df_e[df_e["Date"] <= job_filter]
    
  
    fig_col3, fig_col4 = st.columns(2)
    
    with fig_col3:
        st.markdown("### Premiers cas de COVID19 par pays")
        st.dataframe(df_e)
         
    with fig_col4:
        st.markdown("### Propagation du COVID19 dans le monde")
        st.map(df_e)

    st.markdown("<h2 style='text-align:center;'>Question</h2>", unsafe_allow_html=True)
    if st.button('Quel est le dernier pays à être affecté par le COVID 19 ?'):
        st.write('Palau: pays à revenu intermediare de 21500 habitants situé en Micronésie.Date des premiers cas de COVID19 detectés : 22 août 2021.')
        st.image("https://github.com/Project-covid-streamlit/projet_data_Data-storytelling/blob/alimou/2023_01_05_07j_Kleki.png?raw=true",width=380)
    else:
        st.write('')
  

with tab3:
   st.header("Evolution du COVID19 et vaccins")
   df_c=pd.read_csv("https://raw.githubusercontent.com/Project-covid-streamlit/projet_data_Data-storytelling/f728acc123fc629946391f1aa4d8d5703383400d/COVID%20et%20VACCINS%20par%20pays.csv")

   # top-level filters
   job_filte = st.selectbox("Pays ou Continent", pd.unique(df_c["location"]))

   df_c = df_c[df_c["location"] == job_filte]
   
       # creating KPIs
   med_age = np.mean(df_c["median_age"])
   agé = np.mean(df_c["aged_65_older"])   
   densité = np.mean(df_c["population_density"])
   #lits = np.mean(df_c["hospital_beds_per_thousand"])
   #idh= np.mean(df_c["human_development_index"])
   
   kpi1, kpi2, kpi3 = st.columns(3)

   
   kpi1.metric(
            label="Age médian",
            value=round(med_age))
   
   kpi2.metric(
            label="Par de population de plus de 65 ans (%)",
            value=round(agé))
   kpi3.metric(
            label="Densité de population",
            value=round(densité))
  
   st.markdown("### Evolution nombre de cas COVID19 et de personnes vaccinées")
   st.line_chart(df_c, x="date", y=["total_cases","people_vaccinated","people_fully_vaccinated"])
   
   st.markdown("### Evolution du nombre de décès")
   st.line_chart(df_c, x="date", y=["total_deaths"])
   
   

with tab4:
   st.header("Bilan")
  
   df_u=pd.read_csv("https://raw.githubusercontent.com/Project-covid-streamlit/projet_data_Data-storytelling/alimou/Les%20pays%20les%20plus%20touch%C3%A9s.csv")
   job_filter = st.select_slider("Nombre de pays", df_u["Index"].sort_values(ascending=True))
   df_u = df_u[df_u["Index"] <= job_filter]    

   fig_col1, fig_col2 = st.columns(2)
  
   with fig_col1:
        st.markdown("### Nombre de morts pour un million d'habitants")
        fig=px.bar(df_u,x='Nombre de morts par million',y='location', orientation='h')
        st.write(fig)
            
   with fig_col2:

        st.markdown("### Nombre de vaccinés pour un million d'habitants")
        fig2=px.bar(df_u,x='Nombre de vaccinés ( toutes les doses) par million' , y='location', orientation='h')
        st.write(fig2)
    
   st.markdown("### Caractéristiques des pays")
   st.dataframe(df_u)