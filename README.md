# **Rapport de Projet sur l'Analyse et la Classification de la Qualité de l'Air - Auber**

### **Introduction**

Le projet vise à développer un modèle pour l'analyse et la classification de la qualité de l'air à partir de données environnementales. Le processus comprend deux grandes phases : le nettoyage des données et la classification basée sur les indices de qualité de l'air (IQA) pour PM2.5. Le modèle est conçue pour être utilisée via une interface graphique Tkinter qui facilite la sélection et la manipulation des fichiers de données.

### **Première Partie : Nettoyage des Données**

### **Description du Code**

Le script Python commence par importer les bibliothèques nécessaires, notamment **`pandas`** pour la manipulation de données et **`tkinter`** pour l'interface graphique. La fonction **`clean_numeric_data`** est définie pour convertir et nettoyer les données numériques, gérant les valeurs spéciales comme '<', '>', et 'ND'. Les données sont ensuite chargées à partir d'un fichier sélectionné par l'utilisateur, avec les dates et heures ajustées pour le fuseau horaire.

Les colonnes spécifiques, telles que les concentrations de divers polluants et les paramètres météorologiques, sont nettoyées à l'aide de cette fonction. Après le nettoyage, les valeurs manquantes sont remplacées par la médiane des données disponibles, et les résultats sont sauvegardés dans un nouveau fichier Excel.

### **Fonctionnalité et Performance**

L'interface utilisateur simplifie la sélection et la sauvegarde des fichiers, ce qui rend le processus transparent pour l'utilisateur. Le script gère efficacement les différentes formats et valeurs spéciales dans les données environnementales, garantissant que les données nettoyées sont prêtes pour une analyse ultérieure.

### **Deuxième Partie : Classification de la Qualité de l'Air**

### **Description du Code**

Le deuxième script prend en charge le chargement des données nettoyées et leur préparation pour la modélisation. Après le nettoyage initial, il calcule l'IQA pour PM2.5 et catégorise ce dernier en 'Bon', 'Modéré', ou 'Mauvais' selon des seuils prédéfinis. Le script prépare ensuite les données pour le machine learning, en normalisant les caractéristiques et en divisant les données en ensembles d'entraînement et de test.

Un modèle de forêt aléatoire est entraîné avec ces données. Les résultats sont évalués à l'aide de rapports de classification et de matrices de confusion, qui sont également visualisés pour faciliter l'interprétation.

### **Fonctionnalité et Performance**

Le script intègre des techniques avancées de machine learning pour prédire la qualité de l'air, offrant une évaluation précise basée sur plusieurs variables environnementales. La visualisation des résultats à travers la matrice de confusion fournit une validation claire de la performance du modèle, permettant aux utilisateurs de vérifier intuitivement l'exactitude des prédictions.

### **Analyse de la Matrice de Confusion pour la Classification de la Qualité de l'Air**

<img width="485" alt="Capture d’écran 2024-05-02 à 12 04 36" src="https://github.com/chvro12/IQA_AUBER/assets/134718881/6d0d4bf3-77b6-45da-a86e-39bf9ca13d31">


### **Contexte**

La matrice de confusion est un outil essentiel pour évaluer la performance des modèles de classification. Elle permet de visualiser les performances d'un modèle en comparant les valeurs prédites avec les valeurs réelles. Dans votre projet, la matrice de confusion révèle la précision du modèle de forêt aléatoire utilisé pour classer la qualité de l'air en trois catégories: "Bon", "Mauvais" et "Modéré".

### **Détails de la Matrice**

Voici les éléments clés de la matrice de confusion présentée :

- **Bon**: Le modèle a prédit correctement 3606 cas comme 'Bon', avec 621 prédictions incorrectes classées comme 'Modéré' et seulement 5 comme 'Mauvais'.
- **Mauvais**: Le modèle a très bien performé pour cette catégorie avec 3167 prédictions correctes. Il y a eu quelques erreurs, avec 15 prédictions comme 'Bon' et 575 comme 'Modéré'.
- **Modéré**: Cette catégorie montre une performance impressionnante avec 10660 prédictions correctes, mais avec des erreurs significatives comprenant 550 prédictions comme 'Bon' et 430 comme 'Mauvais'.

### **Analyse**

- **Performance Globale**: Le modèle montre une forte capacité à identifier correctement les catégories 'Bon' et 'Modéré', qui sont les plus fréquentes. La performance pour la catégorie 'Mauvais' est également bonne, bien que le nombre d'erreurs soit un peu plus élevé comparé aux autres catégories.
- **Erreurs de Classification**: Les principales erreurs semblent se produire lors de la classification de 'Bon' en 'Modéré' et vice versa, ce qui peut indiquer une certaine confusion du modèle dans la distinction entre ces deux catégories. Cela peut être dû à des chevauchements dans les plages de valeurs des indicateurs ou à un manque de distinction claire dans les données d'entraînement.
- **Implications**: L'exactitude des prédictions pour 'Bon' et 'Modéré' suggère que le modèle est bien calibré pour ces conditions, ce qui est crucial pour les applications pratiques, car ces conditions sont les plus susceptibles d'influencer les décisions publiques et individuelles concernant la qualité de l'air.
- **Améliorations Possibles**: Pour réduire les erreurs de classification entre 'Bon' et 'Modéré', il serait judicieux de revoir les seuils utilisés pour la catégorisation ou d'incorporer plus de caractéristiques qui pourraient aider à distinguer ces conditions plus précisément.
