#       CHEATSHEET INF2 : FINAUX

## Fichiers
- fichiers binaires ou fichiers texte
- Cycle de vie : Creation > Ouverture > Manipulation > Fermeture

### Ouvrir puis fermer un fichier
```python
try :
    with open("path","w",encoding="utf-8") as f:
        # code
        f.close()
except OSError as e:
    print(e)
```
| mode      | effet                                                            |
| --------- |:----------------------------------------------------------------:|
| "r"       | Lecture seule (par défaut), exception levée s’il n’existe pas    |
| "w"       | Écriture seule, fichier écrasé s’il existe déjà                  |
| "x"       | Création puis écriture, exception levée si le fichier existe déjà|
| "a"       | Ajout, écrit à la fin du fichier s'il existe, le crée sinon      |
| "b"       | Mode binaire                                                     |
| "t"       | Mode texte (par défaut)                                          |
| "+"       | Ouverture en lecture + écriture                                  |

### Parcourir un texte
```python
for line in texte :
    print(line)
```

### Lecture de la totalité d'un fichier
```python
print(file.read())
```

### La fonction split
- permet de transformer une chaîne de caractères en liste de caractères
- le séparateur par défaut est l'espace mais on peut le mettre en paramètre de la fonction
```python
liste=line.split()
```

### Ecrire dans un fichier
```python
f.write(f"content")

# pour écrire ligne par ligne ne pas oublier \n ou writelines
f.write(f"line \n")
f.writelines("lines")
```


## CSV - comma separated values
- import csv

### Lire un fichier csv
- attention, les items des listes sont tous des str même les nombres
```python
valeurs=csv.reader(f,delimiter=',')
# delimiter sépare les cellules
# permet d'obtenir un tableau (liste de liste)
# une ligne = une liste
```

### Utilisation du Dictreader
- permet de récupérer chaque ligne sous forme de dictionnaire
- les clés sont les noms des colonnes (première ligne)
```python
dict_reader = csv.DictReader(file)
for dict_row in dict_reader:
    # on obtient un dictionnaire par ligne
    print(dict_row)
```

### Créer un fichier csv à partir d'un dictionnaire
```python
dict.to_csv("file's name")
```


### Module pandas
- permet de manipuler des tableaux de données

- on peut ouvrir un fichier sans passer par open :
```python
inf2=pd.read_csv('file', delimiter=';')
# chaque colonne est un dictionnaire
```
- rajouter une clé en appliquant une fonction :
```python
dict['key']=dict.apply(function,axis=1) # pour chaque ligne
dict['key']=dict.apply(function,axis=0) # pour chaque colonne
```
- pour chaque dictionnaire, pour vérifier si une case (une valeur) est vide :
```python
# renvoie un booléen
# dictionnaire.nom de la clé (donc de la colonne)
pd.isnull(etudiant.median)
```


### Précisions sur le JSON
#### Comment stocker et partager les données de mon programme (hors format tableur) ?
- Le format JSON (JavaScript Object Notation) est un format d’échange de données très simple et répandu
- Un objet JSON est une représentation sous forme de texte d’un objet
- Un objet commence par ‘{‘ et termine par ‘}’


## Gestion des fichiers
- Retourne un booléen sur l'existence du chemin
```python
os.path.isfile(path)
```
- Vérifie que le chemin correspond à un dossier
```python
os.path.isdir(path)
```
- Récupérer le chemin absolu d'un fichier
```python
os.path.abspath(file)
```