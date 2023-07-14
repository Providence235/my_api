import streamlit as st
import pandas as pd
from flask import Flask, jsonify
import plotly.express as px
st.title("TABLEAU DE BORD DES INDICATEURS")
st.write("BIENVENUE")

#Chargement des bases

data1 = pd.read_csv("impressions.csv")
data2= pd.read_csv("clics.csv")
data3= pd.read_csv("achats.csv")

# jointure des bases
imp_clic=pd.merge(data1, data2, on='cookie_id')
imp_clic_achat=pd.merge(imp_clic, data3, on='cookie_id')
imp_clic_achat

app = Flask(__name__)
@app.route('/imp_clic_achat', methods=['GET'])
def get_imp_clic_achat():
    return jsonify(imp_clic_achat)

#Afficher le chiffre_affaires
chiffre_affaires =imp_clic_achat['price'].sum()

st.write(f"<span style ='color:red; font-size:40px;'>Chiffre d'affaires:{chiffre_affaires} € </span>", unsafe_allow_html=True)

#Histogramme

st.subheader('Prix en fonction du produit')
histo=px.histogram(imp_clic_achat, x='product_id', y='price')
st.plotly_chart(histo)

#boxplot
st.subheader('Age en fonction des produit')
box=px.box(imp_clic_achat, x='product_id', y='age')
st.plotly_chart(box)

#diagrammme circulaire
st.subheader('Répartition de la dépense par tête suivant le sexe')
circulaire=px.pie(imp_clic_achat, values='dept', names='gender')
st.plotly_chart(circulaire)