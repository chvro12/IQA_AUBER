import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import tkinter as tk
from tkinter import filedialog

def calculer_iqa_pm25(pm25):
    # Implémentation de la fonction de calcul de l'IQA pour PM2.5
    iqa = pm25 * 1.5
    return iqa

def categoriser_iqa(iqa):
    # Implémenter la logique de catégorisation de l'IQA
    # Exemple simplifié, veuillez adapter selon vos critères spécifiques
    if iqa < 50:
        return 'Bon'
    elif iqa < 100:
        return 'Modéré'
    else:
        return 'Mauvais'

def plot_confusion_matrix(y_true, y_pred):
    labels = np.unique(y_true)
    conf_matrix = confusion_matrix(y_true, y_pred, labels=labels)
    fig, ax = plt.subplots(figsize=(10, 7))
    cax = ax.matshow(conf_matrix, cmap=plt.cm.Blues)
    fig.colorbar(cax)
    ax.set_xticks(np.arange(len(labels)))
    ax.set_yticks(np.arange(len(labels)))
    ax.set_xticklabels(labels, rotation=45)
    ax.set_yticklabels(labels)
    plt.xlabel('Prédictions')
    plt.ylabel('Valeurs réelles')
    plt.title('Matrice de confusion')
    plt.show()

def main():
    # Interface graphique pour sélectionner le fichier
    root = tk.Tk()
    root.withdraw()  # Cacher la fenêtre Tk principale
    file_path = filedialog.askopenfilename(title='Sélectionnez le fichier de données de qualité de l\'air')  # Ouvre la boîte de dialogue pour sélectionner le fichier

    # Charger les données
    data = pd.read_excel(file_path, engine='openpyxl')

    # Pré-traitement des données
    data['NO'] = data['NO'].replace({'<2': 1, 'ND': np.nan}).astype(float)
    data.fillna(data.median(), inplace=True)

    # Calcul et catégorisation de l'IQA pour PM2.5
    data['IQA_PM2.5'] = data['PM2.5'].apply(calculer_iqa_pm25)
    data['Categorie_IQA'] = data['IQA_PM2.5'].apply(categoriser_iqa)

    # Préparation des caractéristiques
    data['DATE/HEURE'] = pd.to_datetime(data['DATE/HEURE'], utc=True)
    data['Heure'] = data['DATE/HEURE'].dt.hour
    data['Jour_semaine'] = data['DATE/HEURE'].dt.weekday

    features = ['NO', 'NO2', 'PM10', 'CO2', 'TEMP', 'HUMI', 'Heure', 'Jour_semaine']
    X = data[features]
    y = data['Categorie_IQA']

    # Normalisation des caractéristiques
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Séparation en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Entraînement du modèle
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Prédiction et évaluation
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Visualisation des résultats
    plot_confusion_matrix(y_test, y_pred)

if __name__ == '__main__':
    main()