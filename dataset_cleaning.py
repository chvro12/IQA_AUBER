import pandas as pd
import tkinter as tk
from tkinter import filedialog

def clean_numeric_data(value):
    if isinstance(value, str):
        value = value.replace(',', '.')
        if value.startswith('<'):
            return float(value[1:])
        elif value.startswith('>'):
            return float(value[1:])
        elif value == 'ND':
            return pd.NA
    try:
        return float(value)
    except ValueError:
        return pd.NA

def clean_data():
    # Configuration de l'interface graphique pour la sélection de notre fichier
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title='Sélectionnez le fichier de données')

    if file_path:
        # Chargement des données depuis le fichier Excel sélectionné
        data = pd.read_excel(file_path)

        # Gestion des dates-heures avec fuseaux horaires
        data['DATE/HEURE'] = pd.to_datetime(data['DATE/HEURE'], utc=True).dt.tz_localize(None)

        # Nettoyage et conversion des colonnes de polluants et des colonnes température et humidité
        columns_to_clean = ['NO', 'NO2', 'PM10', 'PM2.5', 'CO2', 'TEMP', 'HUMI']
        for col in columns_to_clean:
            data[col] = data[col].apply(clean_numeric_data)

        # Gestion des valeurs manquantes
        data.fillna(data.median(), inplace=True)

        # Sauvegarde des données nettoyées dans un nouveau fichier Excel
        cleaned_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[("Excel files", "*.xlsx")], title="Enregistrer le fichier nettoyé sous")
        if cleaned_file_path:
            data.to_excel(cleaned_file_path, index=False)
            print("Nettoyage terminé et fichier enregistré sous :", cleaned_file_path)
        else:
            print("Enregistrement annulé")
    else:
        print("Aucun fichier sélectionné")

# Appel de la fonction de nettoyage des données
if __name__ == "__main__":
    clean_data()
