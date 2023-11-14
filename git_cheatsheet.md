# ATTENTION TOUJOURS ETRE A JOUR ENTRE GIT / VS

# Enregistrer les modifs git VERS vscode
```shell
git pull origin $BRANCH
# souvent BRANCH = main mais faire gaffe à ce qu'on soit dans la bonne branche
```

# Verifier l'état
```shell
git status
```

# Enregistrer des modifs de vs vers git en trois étapes
## (1) ajout (AVANT DE PUSH)
Bien sûr s'assurer que les ajouts sont enregistrés sur vscode
```shell
git add $FILE
git add . # tous les fichiers de git status en rouge
git reset # annule l'ancien ajout
```

## (2) commit avec un message expliquant les modifs
```shell
git commit -m "message"
# par ex update cheatsheet
```

## (3) Enregistrer les modifs vscode VERS git
```shell
git push origin $BRANCH
# attention à la branche
```


# Vérifier l'état de l'avancement
```shell
git log
```

# Créer une nouvelle branche
partir d'une branche à jour (par ex main) suivi d'un git pull origin main
```shell
git checkout -b $BRANCH
```

# Changer de branche
```shell
git checkout $BRANCH
```

# Voir les modifications faites depuis le dernier pull
```shell
git diff
git diff $FILE
```

# Annuler toutes les mofifs vues par le git diff
```shell
git checkout .
git checkout $FILE
```

# Extra
commandes unix pratiques
alt + tab pour changer de fenêtre boloss
```
clear # permet d'effacer les lignes de code
pwd # affiche le chemin du répertoire courant
cd ~ # replace l'utilisateur à l'origine des répertoires
ls # affiche les fichiers du répertoire courant
ls -la # -l affiche la taille et les droits et -a affiche les fichiers cachés
man # manuel des commandes
cp $FILEACOPIE $NEWFILE # copier un fichier
rm $FILE # remove = supp
```

