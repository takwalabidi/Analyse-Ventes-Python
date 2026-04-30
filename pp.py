import pandas as pd
import matplotlib.pyplot as plt
import random

# 1. GÉNÉRATION DE 1000 PRODUITS UNIQUES

nb_lignes = 1000

data = {
    "ID": list(),  #  1000 ID uniques
    "Prix": [],
    "Quantite": [],
    "Remise": []
}

df = pd.DataFrame(data)

# Sauvegarde CSV
df.to_csv("ventes.csv", index=False)
print("Fichier ventes.csv (1000 produits uniques) généré !")

# 2. CALCULS
df["CA_Brut"] = df["Prix"] * df["Quantite"]
df["CA_Net"] = df["CA_Brut"] * (1 - df["Remise"] / 100)
df["TVA"] = df["CA_Net"] * 0.20

# 3. ANALYSE
ca_total = df["CA_Net"].sum()

# Ici chaque produit est unique → pas besoin de groupby
top_produit = df.loc[df["CA_Net"].idxmax()]
print(f"\n CA Total = {ca_total:.2f} €")
print(f" Meilleur produit : ID {top_produit['ID']} → {top_produit['CA_Net']:.2f} €")

# 4. EXPORT FINAL
df.to_csv("resultats_final.csv", index=False)
print(" resultats_final.csv exporté !")

# 5. VISUALISATION
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

#  Titre général
fig.suptitle("Analyse des ventes", fontsize=14, fontweight="bold")

# --- Graphique 1 : Camembert ---
# On ne peut pas afficher 1000 parts → on prend TOP 10
top10 = df.sort_values(by="CA_Net", ascending=False).head(10)

axes[0].pie(
    top10["CA_Net"],
    labels=top10["ID"],
    autopct="%1.1f%%",
    startangle=90
)
axes[0].set_title("Top 10 produits (CA Net)")

# --- Graphique 2 : Courbe ---
axes[1].plot(df["ID"], df["CA_Net"])
axes[1].set_title("CA Net des produits")
axes[1].set_xlabel("ID Produit")
axes[1].set_ylabel("CA Net (€)")
axes[1].grid()

plt.tight_layout()
plt.savefig("graphiques_ventes.png")
plt.show()

print(" Graphiques générés !")