import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuration de la page
st.set_page_config(page_title="Analyseur de Ventes", layout="wide")

st.title("📊 Analyseur de Ventes E-commerce")
st.markdown("---")

# Étape 1 : Chargement du fichier
st.subheader("📂 Étape 1 : Importer vos données")
uploaded_file = st.file_uploader("Choisissez votre fichier CSV", type="csv")

if uploaded_file is not None:
    # Lecture des données
    df = pd.read_csv(uploaded_file)

    # Calcul du CA Brut si non présent
    if 'CA_Brut' not in df.columns:
        df['CA_Brut'] = df['Prix'] * df['Quantite']
    
    # CORRECTION : On divise la remise par 100 pour le calcul
    df['CA_Net'] = df['CA_Brut'] * (1 - df['Remise'] / 100)

    # --- CALCUL DES INDICATEURS CLÉS (KPI) ---
    total_ca_net = df['CA_Net'].sum()
    # On cherche l'ID du produit qui a le plus grand CA Net
    best_id = df.loc[df['CA_Net'].idxmax(), 'ID']
    marge_moyenne = df['Remise'].mean()

    # Étape 2 : Affichage des indicateurs
    st.subheader("💡 Étape 2 : Indicateurs Clés de Performance (KPI)")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Chiffre d'Affaires Net Total", value=f"{total_ca_net:,.2f} €")
    
    with col2:
        st.metric(label="Produit le plus Rentable (ID)", value=best_id, help="ID du produit avec le plus grand CA Net.")
    
    with col3:
        st.metric(label="Remise Moyenne Accordée", value=f"{marge_moyenne:.1f} %")

    st.markdown("---")

    # Étape 3 : Visualisation Graphique
    st.subheader("📈 Étape 3 : Visualisation des Ventes")
    
    fig, ax = plt.subplots(figsize=(10, 4))
    # On change la couleur en vert émeraude comme sur l'image
    ax.bar(df['ID'].astype(str), df['CA_Net'], color='#2ecc71')
    ax.set_xlabel("ID Produit")
    ax.set_ylabel("CA Net (€)")
    ax.set_title("Chiffre d'Affaires Net par Produit")
    plt.xticks(rotation=45)
    
    st.pyplot(fig)

    # Étape 4 : Aperçu des données
    st.subheader("📋 Étape 4 : Aperçu des données finales")
    st.dataframe(df.style.format(subset=['Prix', 'CA_Brut', 'CA_Net'], formatter="{:.2f}"))

else:
    st.info("👆 Veuillez importer un fichier CSV pour voir l'analyse.")
    st.warning("Assurez-vous que votre fichier contient les colonnes : ID, Prix, Quantite, Remise")