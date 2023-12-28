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
- rajouter une clé tout court
```python
# par exemple rajouter une colonne avec la somme des deux premières colonnes
dict['key']=dict['c1']+dict['c2']
```

- pour chaque dictionnaire, pour vérifier si une case (une valeur) est vide :
```python
# renvoie un booléen
# dictionnaire.nom de la clé (donc de la colonne)
pd.isnull(etudiant.median)
```

- trier le dictionnaire en fonction des valeurs
```python
# ascending --> valeurs (False=decr)
# inplace --> modifie le dataframe dict
dict.sort_values('nom_colonne',ascending=False,inplace=True)
```

- transformer un dictionnaire en fichier csv
```python
dict.to_csv('name.csv')
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



## Interfaces graphiques
- application exécutée dans une unité d'interface graphique
- interaction plus conviviale et intuitive
- les widgets sont des objets graphiques rattachés à une fenêtre
- le gestionnaire d'évènements est une boucle infinie qui exécute une focntion lorsqu'un évènement intervient

```python
def main():
    ma_fenetre=Fenetre()
    # code
    ma_fenetre.mainloop()
```

### Callback
- fonction passée en paramèter d'une autre fonction

### Module Tkinter
- classe Tk et collection de composants d'interface - graphique
- Button (bouton poussoir)
- Checkbutton (case à cocher)
- Radiobutton (bouton radio)
- Label (étiquette)
- Entry (champ de texte en entrée)
- Listbox (liste défilante)
- tk_optionMenu (liste)
- Menu (menu déroulant)
- Menubutton (menu déroulant à partir d'un bouton)
- Scale (curseur horizontal et vertical)
- Spinbox (zone de sélection numérique)
- Frame (cadre)
- Labelframe (cadre avec titre)
- Scrollbar (barre de défilement)
- Panedwindow (panneau coulissant)
- Text (conteneur hypertexte évolué)
- Canvas (conteneur d'objets graphiques 2D évolué)
- tk_chooseColor (sélecteur de couleur)
- tk_chooseDirectory (sélecteur de répertoire)
- tk_dialog (boîte de dialogue modale)
- tk_getOpenFile (sélecteur de fichier)
- tk_messageBox (boîte de message)
- tk_popup (menu contextuel)

```python
import tkinter as tk
fenetre=tk.Tk()
fenetre.mainloop()
```
#### On utilise la fenêtre comme une classe
```python
class Fenetre(Tk):
    def __init__(self):
        Tk._init(self)
```

### Pour arrêter la fenêtre
```python
fenetre.destroy()
fenetre.quit()
```

### Créer un bouton pour quitter
```python
def main():
    fenetre = Tk()
    label = Label(fenetre, text="cours de Python")
    bouton = Button(fenetre, text="Quitter", fg="red",command=fenetre.des)
    label.pack()
    bouton.pack()
    fenetre.mainloop()
```

### Placer la fenêtre au centre de l'écran
```python
def placer_fenetre_principale(self):
    ecran_x = self.winfo_screenwidth()
    ecran_y = self.winfo_screenheight()

    fenetre_x, fenetre_y = self.largeur, self.hauteur
    pos_x = ecran_x // 2 - fenetre_x // 2  # placement de la fenêtre par rapport au coin supérieur gauche
    pos_y = ecran_y // 2 - fenetre_y // 2  # distance entre le haut de l'écran et le haut de la fenêtre Tk
    self.geometry(f"{fenetre_x}x{fenetre_y}+{pos_x}+{pos_y}")
```

### Titre de la fenêtre, attributs dans le init
```python
class Fenetre(Tk):
    def __init__(self,l,h):
        Tk.__init__(self)
        self.title("title")
        # placer la fenetre
        self.placer_fenetre_principale()
        # créer les labels
        self.create_label()
        # créer les bouttons
        self.create_buttons()
```

### Modifier les attributs d'un bouton
```python
self.config(bg="yellow",relief="solid",borderwidth = 3)
```

### Classe Label
- affichage d'un texte à position précise
```python
label=Label(ma_fenetre,text="Bienvenue")
label.pack()
```

### Classe Button
- lien entre une fonction et un clic
```python
bouton = Button(ma_fenetre,text="Bouton", command = self.ma_fonction)
bouton.pack()

bouton_quitter = Button(ma_fenetre, text ='Quitter', command = self.destroy)
bouton_quitter.pack()
```

## Bases de données
- apprendre les requêtes sql
- diagrammes UML