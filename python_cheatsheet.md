#       CHEATSHEET INF2 : FINAUX

## FICHIERS
- fichiers binaires ou fichiers texte
- Cycle de vie : Creation > Ouverture > Manipulation > Fermeture

### Ouvrir puis fermer un fichier
```python
try :
    with open("path","w",encoding="utf-8") as f:
        # code
        # pas besoin de f.close() car compris dans le with
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
- permet de transformer une chaîne de mots en liste de mots
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


## CSV - COMMA SEPERATED VALUES
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


## GESTION DES FICHIERS
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



## INTERFACES GRAPHIQUES
- application exécutée dans une unité d'interface graphique
- interaction plus conviviale et intuitive
- les widgets sont des objets graphiques rattachés à une fenêtre
- le gestionnaire d'évènements est une boucle infinie qui exécute une fonction lorsqu'un évènement intervient

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
        super().__init__()
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
# ma_fenetre = self si dans une classe
label=Label(ma_fenetre,text="Bienvenue")
label.pack()
```
### méthode grid
```python
# si dans une méthode ne pas oublier self.label=Label()
# puis self.label.grid()
label.grid(row=1,column=4)
```
- attribut sticky dans la méthode grid
```python
label.grid(sticky='e')
# n,s,o,e = position
# par défaut place le label au milieu
```

- ocuuper plusieurs colonnes ou lignes
```python
# occupe 2 colonnes
label.grid(columnspan=2)
# occupe 3 lignes
label.grid(rowspan=3)
```



### Classe Button
- lien entre une fonction et un clic
```python
bouton = Button(ma_fenetre,text="Bouton", command = self.ma_fonction)
bouton.pack()

bouton_quitter = Button(ma_fenetre, text ='Quitter', command = self.destroy)
bouton_quitter.pack()
```

- Marges autour du bouton ou label
```python
# marges côtés
label.pack(padx=10)
# marges dessus et dessous
button.pack(pady=30)
```

- remplir un espace
```python
# remplir la largeur
label.pack(fill=X, ipady=30)
# remplir la longueur
label.pack(fill=Y, ipadx=20)
```

### Classe Entry
```python
entry=Entry(ma_fenetre, relief='sunken',borderwidth=10, width=50)
# vider un entry
entry.config(text="")
```
- Récupérer la valeur d'un entry
```python
valeur = self.entry.get()
```
- supprimer une entrée
```python
entree.delete (0, END)
```

### Classe Canvas
```python
image = Canvas (self, width =400, height =240, bg = "ivory")
```
- création d'un objet photo
```python
self.photo = PhotoImage(file="figure.png")
self.image.create_image(200, 120, image=self.photo)
```

## CALCUL SCIENTIFIQUE, VISUALISATION

- utiliser les modules numpy et matplotlip.pyplot

### Les ndarray :
Les tableaux de NumPy (ndarray):
- taille fixe, éléments de même type
- plus de méthodes
- méthodes plus rapides et efficaces (implémentées en C)
- 1Darray, 2Darray, 3Darray... le plus souvent tableau 2D (= tableau de tableau)

### constructeur d'un tableau ndarray
```python
import numpy as np
# par défaut permet de convertir des listes en tableau ndarray
np.array(valeurs) 
# exemple
A=np.array([[1,2,3],[4,5,6]])
```

### attributs importants des ndarray

| attribut  | description                                                      |
| --------- |:----------------------------------------------------------------:|
| size      | Nombres d’élements dans le tableau (fixe)                        |
| dtype     | Type des éléments (unique)                                       |
| shape     | Taille dans chacune des dimensions sous forme de tuple           |

ex un cube avec des faces de 2x3 :
- ndim = 3
- shape = (2,3,2) (hauteur - largeur - profondeur)

### méthodes / fonctions
- axis 1 = horizontal = à droite
- axis 0 = vertical = en dessous

| méthode / fonction       |description                                                         |
| ------------------------ |:------------------------------------------------------------------:|
| copy()                   | copie                                                              |
| np.hstack((A,B))         | Assemblage horizontal (nombres de lignes doivent être identiques)  |
| np.vstack((A,B))         | Assemblage vertical (nombre de colonnes doivent être identiques)   |
|np.concatene((A,B),axis=…)| Concaténation selon un axe (vertical axis = 0, horizontal axis = 1)|
|np.unique()               | Retourne dans un tableau 1D les valeurs triées sans les doublons , |

### méthodes de calcul
```python
# somme
b.sum() # somme de toutes les valeurs
b.sum(axis=0) # retourne une liste de la somme de chaque colonne
b.sum(axis=1) # liste de la somme de chaque ligne
# produit
b.prod(axis=0)

# min / max
b.min() or b.max()

# retourne l'indice du min
b.argmin()

# trier le tableau
b.sort()

# moyenne (en fonction de l'axe)
b.mean()

# retourne un tableau de la somme cumulée
b.cumsum()
```

on peut appliquer des fonctions mathématiques à chaque valeur :
```python
np.sin()
np.cos()
np.exp()
np.log()
```

- remplir un array avec des valeurs aléatoires
```python
# on peut mettre qu'une valeur 
A = np.random.rand(n,m)
# ou
A = np.random.random((n, m))
```

- créer un tableau 1D rempli de valeurs qui se suivent
```python
x=np.arange($bornedebut,$bornefin,$pas)
```

- créer une matrice avec que des 1
```python
A=np.ones(lignes,colonnes)
```

- remplir de 0
```python
monde3D= np.zeros((dimx,dimy,dimz),dtype=int)
monde3D[-1, :,:] = 4 # tout en 4
```

- ajouter un cadre noir épais de 3 pixels
```python
# haut = bas = gauche = droite = noir
A[:3, :] = A[-3:, :] = A[:, :3] = A[:, -3:] = 0
```

### Le broadcasting
-  Mécanisme puissant qui consiste à étendre les dimensions d’un tableau 

### Les masques booléens
```python
A = np.array([[1, 2, 3], [4, 5, 6]])
B = A<5 # masque booléen
A[A<5] = 10 # convertit les valeurs sélectionnées.
```

### Graphiques
- module matplotlib.pyplot

- afficher une image
```python
# à partir d'un ndarray A
# cmap = gray -> noir et blanc
plt.imshow(A, cmap="gray")
# afficher la colorbar
plt.colorbar()
plt.show()
```

- afficher un graphique / figure
```python
# plusieurs courbe sur un graphique
plt.figure()
plt.plot(x, y1, c='green', label='label 1')
plt.plot(x, y2, c='blue', label='label 2')
plt.xlabel('x label')
plt.title('title')
plt.legend()
plt.savefig('$file')
plt.show()
```

### Scipy
```python
# raton gris
# si gray alors tableau 2D donc shape a deux arguments
# sinon 3D donc 3 args avec taille du tableau RGB
raton = datasets.face(gray=True)
plt.imshow(raton, cmap='gray') # ou cmap='Greys'
plt.show()
```
```python
# obtenir dimensions
l,c = raton.shape
# zoom 1/4
zoom=raton[l//4:l//4*3,c//4:c//4*3]
```

- afficher l'histogramme d'une image
```python
# ravel transforme la matrice en liste
# bins = niveau de gris (répartit en fonction des valeurs des pixels)
plt.hist(zoom.ravel(), bins=256)
plt.title('histogramme du zoom')
plt.show()
```

- faire un contraste
```python
# pixels les plus bas sur l'histo
contraste[contraste<40]=0 
# pixels les plus hauts sur l'histo
contraste[contraste>200]=255
```
- répartir les couleurs sur l'histo
```python
val,nb=np.unique(zoom,return_counts=True)
s=nb.cumsum(nb)
total=zoom.size
quatreniveaux=np.copy(zoom)

for i in range(len(s)):
    if s[i]<total//4:
        quatreniveaux[zoom==val[i]]=0
```
ou sinon :
```python
s=np.cumsum(nb)
i=0
while s[i]<=total//4:
    i+=1
seuil_0=i
# faire les autres while
quatreniveaux[zoom<val[seuil_0]]=0
quatreniveaux[(zoom>=val[seuil_0] and zoom<val[seuil_84])]=84
# etc..
```

### Ouverture d'un fichier png
```python
image=plt.imread('$FILE')
plt.imshow(image)
plt.title('image')
plt.show()
```

### Canaux RGB
```python
# [:,:,x] = tt les lignes et colonnes pour x couleur 
image[:,:,0] # rouge
image[:,:,1] # vert
image[:,:,2] # bleu
# pour obtenir du jaune on enlève le bleu
```

- moyenne et écart-type
```python
A.mean(axis=1)
A.std(axis=0)
```
### Opérations matricielles
```python
np.allclose() #retourne vrai si 2 éléments sont égaux à une tolérance près

# produit matricielle
A@B
A.dot(B)

#transposée
A.T
A.transpose()
```

### Créer une matrice aléatoire
```python
R = np.random.randint(xmin, xmax, (n_lignes, n_colonnes))
```

- matrice identité In,n
```python
I = np.eye(n)
```

## BASES DE DONNEES
- apprendre les requêtes sql
- diagrammes UML

### étapes modélisation - conception :
- diagramme conseptuel sans les clés
- identifier les clés primaires
- traiter les relations (types) et clés étrangères (nom clé vers nom table)
- diagramme relationnel à l'écrit ou avec les tables dessinés (sans les relations)

### Pour un type m-n :
On peut créer une table de liaison entre les deux qui contient deux clés étrangères qui renvoient aux deux tables avec comme clé primaire le couple des deux clés étrangères.

### diagramme relationnel
```
Table(#PK:int,nom:str,sexe:{F,M,N},FK->Table')
tels attributs non nuls
clés primaires soulignés
```
### Utiliser le module sqlite3 sur python
```python
import sqlite3

try :
    connexion = sqlite3.connect('$FILE')
    cursor = connexion.cursor()
    cursor.execute("COMMAND SQL")
    result=cursor.fetchall()
    for element in result :
        # code

except sqlite3.Error as e :
    print(e)

finally :
    cursor.close()
    connexion.close()
```
### récupérer le contraire d'une commande
```python
cursor.execute("SELECT * FROM table WHERE NOT attribut=''")
```

### différents types de jointure
- INNER JOIN : jointure interne pour retourner les enregistrements quand la condition est vrai dans les 2 tables. C’est l’une des jointures les plus communes
- LEFT JOIN (ou LEFT OUTER JOIN) : jointure externe pour retourner tous les enregistrements de la table de gauche (LEFT = gauche) même si la condition n’est pas vérifié dans l’autre table.
- RIGHT JOIN (ou RIGHT OUTER JOIN) : jointure externe pour retourner tous les enregistrements de la table de droite (RIGHT = droite) même si la condition n’est pas vérifié dans l’autre table.
- FULL JOIN (ou FULL OUTER JOIN) : jointure externe pour retourner les résultats quand la condition est vrai dans au moins une des 2 tables.
- SELF JOIN : permet d’effectuer une jointure d’une table avec elle-même comme si c’était une autre table.
- UNION JOIN : jointure d’union

### ajouter une info dans une table
```python
cursor.execute("INSERT INTO table (attribut1,attribut2) VALUES (value1,value2)")
# quand on modifie la BDD
connexion.commit()
```
### créer une table
```python
cursor.execute("CREATE TABLE IF NOT EXISTS table
(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
label Enum [1, 2, 3] INTEGER NULL,
FOREIGN KEY(table2_id) REFERENCES table2(id))") 
```

### supprimer un élément de la BDD
```python
cursor.execute("DELETE FROM table WHERE attribut='...'")
```

### modifier la base de donnée
```python
cursor.execute("UPDATE table SET attribut1 = '...' WHERE attribut2='...'")
connexion.commit()
```

### sous requête
```python
cursor.execute("UPDATE table SET attribut1=(SELECT etrangere FROM table 2 WHERE (...)) WHERE attribut2='...'")
connexion.commit()
```

### mettre plusieurs conditions
```sql
WHERE (condition1 OR condition2);
```

### trier les valeurs
```sql
    # par ordre décroissant
SELECT (...) ORDER BY attribut DESC;
    # par ordre croissant
SELECT (...) ORDER BY attribut ASC;
```

### pour ne pas afficher plusieurs fois des informations
```sql
SELECT DISTINCT attribut FROM table;
```

### faire un self JOIN
```sql
SELECT A.attribut AS attribut1, B.attribut AS attribut2
FROM table A, table B   # même nom pour les deux tables
```


## COURS
- fonction callback : fonction qui est passée en argument à une autre fonction
- rajouter les qcm des annales et du groupe 
- random.choice([1,-1])