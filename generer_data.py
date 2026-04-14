import pandas as pd
import matplotlib.pyplot as plt


# On lit le gros fichier de 500 lignes au lieu du petit
df = pd.read_csv('ventes_grosses.csv')

# Preuve du dynamisme : on affiche le nombre de lignes traitées
print(f"--- Analyse lancée sur {len(df)} lignes ---")

# les calculs habituels 
df['CA_Brut'] = df['Prix'] * df['Quantite']
df['CA_Net'] = df['CA_Brut'] * (1 - df['Remise'] / 100)

# On affiche un aperçu et le total pour vérifier
print(df.head()) 
print(f"Total CA Net du fichier : {df['CA_Net'].sum():.2f} €")

#  BONUS : Graphique
plt.bar(df["ID"], df["CA_Net"])
plt.title("CA Net par produit")
plt.xlabel("ID Produit")
plt.ylabel("CA Net")
plt.show()
