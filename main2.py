import pandas as pd
import matplotlib.pyplot as plt

# 1. GÉNÉRATION DES DONNÉES
# On crée directement les données en mémoire 

data = {
    "ID": [101, 102, 103],
    "Prix": [15.0, 25.0, 10.0],
    "Quantite": [3, 2, 5],
    "Remise": [10, 5, 0]
}

df = pd.DataFrame(data)

# Sauvegarde automatique du fichier CSV
df.to_csv("ventes.csv", index=False)
print(" Fichier ventes.csv généré automatiquement !")

# 2. Calcul du Chiffre d’Affaires Brut (Prix × Quantité)
df["CA_Brut"] = df["Prix"] * df["Quantite"]
print(df["CA_Brut"])

# 3. Application des remises (%) → CA Net
df["CA_Net"] = df["CA_Brut"] * (1 - df["Remise"] / 100)
print(df["CA_Net"])

# 4. Calcul de la TVA (20%) sur le CA Net
df["TVA"] = df["CA_Net"] * 0.20
print(df["TVA"])

# 5. Calcul du CA Total de l’entreprise
ca_total = df["CA_Net"].sum()
print("CA Total =", ca_total)

#6. Identifier l’ID du produit avec le plus grand bénéfice (CA Net max)
id_best_product = df.loc[df["CA_Net"].idxmax(), "ID"]
print("Produit avec le plus grand bénéfice :", id_best_product)

# 7. Export du fichier final
df.to_csv("resultats_final.csv", index=False)
print("Fichier exporté avec succès !")

# 8. VISUALISATION

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

#  Titre général
fig.suptitle("Analyse des ventes", fontsize=14, fontweight="bold")

# --- Graphique 1 : Cercle (Camembert) 
axes[0].pie(
    df["CA_Net"],
    labels=df["ID"],
    autopct="%1.1f%%",
    startangle=90
)
axes[0].set_title("Répartition du chiffre d'affaires")

# --- Graphique 2 : Graphique avec axes (courbe simple) 
axes[1].plot(df["ID"], df["CA_Net"], marker='o')
axes[1].set_title("CA Net par produit")
axes[1].set_xlabel("ID Produit")
axes[1].set_ylabel("CA Net (€)")
axes[1].grid()

plt.tight_layout()
plt.savefig("graphiques_ventes.png")
plt.show()

print(" Graphiques générés !")