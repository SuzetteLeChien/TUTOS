# Makefile

**Constat** : Programmation modulaire, fragmentation de code --> la compilation séparée peut devenir longue et fastidieuse.

## Principe
1) Créer un fichier Makefile en spécifiant les dépendances entre fichiers sources, objets et exécutables.
2) Utiliser la commande Unix **make** pour lancer la compilation du projet
- la commande recherche par défaut un fichier de nom Makefile
- sinon lancer la commande avec l'option -f nom_fichier

## Utilité
- gère la compilation de grands programmes codés sur plusieurs fichiers sources
- peut réaliser une compilation séparée des modules
- peut compiler uniquement les parties du code qui ont été changées
- utile pour dev ou mise à jour d'app

## Exemple
Calculatrice avec historique :
- historique.h, operations.h
- calc_main.c, calc_historique.c, calc_operations.c
- calc_main.o, calc_historique.o, calc_operations.o
- calculatrice.exe

```makefile
Calculatrice : calc_main.o calc_historique.o \
    calc_operations.o
    gcc -o Calculatrice calc_main.o calc_historique.o \
        calc_operations.o
calc_main.o : calc_main.c historique.h \
    operations.h
    gcc -c calc_main.c
calc_historique.o : calc_historique.c historique.h
    gcc -c calc_historique.c
calc_operations.o : calc_operations.c historique.h \
    operations.h
    gcc -c calc_operations.c
```
## Analyse : 
### 1) Déclaration de la cible principale 
- Calculatrice : cible principale, nom de l'exécutable final
- calc_main.o calc_historique.o calc_operations.o : fichiers objets nécessaires pour créer l'exécutable

### 2) Règle pour construire l'exécutable
```makefile
gcc -o Calculatrice calc_main.o calc_historique.o \
    calc_operations.o
```
- Cette commande est exécutée lorsque la cible Calculatrice doit être construite
- gcc -o produit un exécutable nommé Calculatrice en liant les fichiers objets mentionnés

### 3) Règle pour construire calc_main.o
```makefile
calc_main.o : calc_main.c historique.h \
    operations.h
    gcc -c calc_main.c
```
Dépendances :
- calc_main.c : le fichier source correspondant
- historique.h et operations.h : fichiers d'en-tête inclus dans calc_main.c  

Commande gcc -c : 
- l'option -c compile sans lier et produit un fichier objet calc_main.o

### 4) Règle pour construire calc_historique.o
```makefile
calc_historique.o : calc_historique.c historique.h
    gcc -c calc_historique.c
```
Dépendances :
- calc_historique.c : fichier source principal
- historique.h : fichier d'en-tête utilisé par calc_historique.c  

Commande :
- compile le ficheir source calc_historique.c en fichier objet calc_historique.o

### 5) Règle pour construire calc_operations.o
```makefile
calc_operations.o : calc_operations.c historique.h \
    operations.h
    gcc -c calc_operations.c
```
Dépendances :
- calc_operations.c : fichier source principal
- historique.h et operations.h : fichiers d'en-tête nécessaires  

Commande :
- compile le fichier source calc_operations.c en fichier objet calc_operations.o
