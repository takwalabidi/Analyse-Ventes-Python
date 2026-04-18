<h1 align="center">📊Analyse des Ventes E-commerce</h1> <p align="center"> <img src="logo.png" alt="Status"> </p>

---

> 🚀 Script Python automatisé pour le traitement de données financières et l’analyse des performances de ventes.

---

# 📝 Contexte du Projet

Ce projet a pour objectif de remplacer la gestion manuelle des données (Excel) par une solution automatisée en Python.

Il permet de :
- Gérer de grands volumes de données
- Automatiser les calculs financiers
- Générer des rapports fiables et exploitables

---

# ⚙️ Travail Réalisé

Le script exécute les étapes suivantes :

## 1️⃣ Génération des données
- Création automatique du fichier `ventes.csv`

## 2️⃣ Calculs financiers
- **Chiffre d'Affaires Brut (CA Brut)**  
  CA Brut = Prix × Quantité  

- **Chiffre d'Affaires Net (CA Net)**  
  CA Net = CA Brut après remise (%)  

- **TVA (20%)**  
  TVA = 20% × CA Net  

## 3️⃣ Analyse
- Identification automatique du produit le plus rentable

## 4️⃣ Export
- Génération d’un fichier final enrichi :  
  `resultats_final.csv`

---

# 🎯 Bonus Implémentés

- ✔️ Visualisation des données avec Matplotlib  
- ✔️ Support de fichiers CSV de tailles variables  
- ✔️ Dashboard interactif avec Streamlit  

---

# 🛠️ Technologies Utilisées

- **Langage** : Python 3  
- **Librairies** : Pandas, Matplotlib, Streamlit  
- **Outils** : VS Code  
- **Format** : CSV  

---

# 🚀 Installation et Démarrage

## 1️⃣ Cloner le dépôt
```bash
git clone https://github.com/takwalabidi/Analyse-Ventes-Python.git
cd Analyse-Ventes-Python
```

## 2️⃣ Créer un environnement virtuel
```bash
python -m venv venv
```

## 3️⃣ Activer l’environnement

### Windows
```bash
.\venv\Scripts\activate
```

### macOS / Linux
```bash
source venv/bin/activate
```

## 4️⃣ Installer les dépendances
```bash
pip install -r requirements.txt
```

---

# 💻 Exécution du Script
```bash
python main.py
```

---

# 🌐 Mode Web (Dashboard)

Pour lancer l’interface interactive :

```bash
streamlit run app.py
```

---

# 📌 Résultats

- 📄 Fichier traité : `resultats_final.csv`
- 📊 Graphiques générés automatiquement
- 📈 Indicateurs de performance calculés

---

# 👩‍💻 Auteur

**Takwa Labidi**  
🎓 Étudiante en Mathématiques & Informatique  
📍 Faculté des Sciences de Tunis  

---

# ⭐ Objectif

Ce projet démontre :
- L'automatisation des traitements de données
- L'analyse financière avec Python
- La capacité à transformer des données en décisions
