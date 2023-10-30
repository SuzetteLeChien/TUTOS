# ATTENTION toujours être à jour avec git
## à chaque fois que j'ouvre github --> visual
```shell
git pull origin $BRANCH
```

# Verifier l etat
```shell
git status
```

# (1) ajout (AVANT DE PUSH)
```shell
git add $FILE
git add . # tous les fichiers de git status en rouge
git reset # annule l'ancien ajout
```

# (2) après un ajout faire un commit avec un message expliquant les modifs
```shell
git commit -m "message"
```

# (3) après un commit faire un push visual --> github
```shell
git push origin $BRANCH
```


# vérifier l'état de l'avancement
```shell
git log
```

# créer une nouvelle branche
partir d'une branche à jour (par ex main) suivi d'un git pull origin main
```shell
git checkout -b $BRANCH
```

# changer de branche
```shell
git checkout $BRANCH
```

# voir les modifications qui ont été faites depuis le dernier pull
```shell
git diff
git diff $FILE
```

# annuler toutes les mofifs vues par le git diff
```shell
git checkout .
git checkout $FILE
```

# Extra
```
clear
pwd
cd ~
ls # affiche les fichiers du répertoire courant
ls -la # -l affiche la taille et les droits et -a affiche les fichiers cachés
man # manuel des commandes
cp $FILEACOPIE $NEWFILE # copier un fichier
rm $FILE # remove = supp
```

