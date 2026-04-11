import pandas as pd
import matplotlib.pyplot as plt

# 1. Lire le fichier CSV
df = pd.read_csv("ventes.csv", encoding="latin-1")

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

# 8. BONUS : Graphique
plt.bar(df["ID"], df["CA_Net"])
plt.title("CA Net par produit")
plt.xlabel("ID Produit")
plt.ylabel("CA Net")
plt.show()
