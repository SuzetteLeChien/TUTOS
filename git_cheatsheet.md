# ATTENTION TOUJOURS ETRE A JOUR ENTRE GIT / VS
### Commencer par se placer dans le bon répertoire avec un cd

# Enregistrer les modifs git VERS vscode
```shell
git pull origin $BRANCH
# souvent BRANCH = main mais faire gaffe à ce qu'on soit dans la bonne branche
```
# Récupérer git VERS vscode sans enregistrer
```shell
git fetch
# pas trop compris
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
git add -p # demande si tu veux ajt les diff modifs
git remove $FILE # enlève le fichier qui a été add mais pas push
git reset # annule l'ancien ajout
```

## (2) commit avec un message expliquant les modifs
```shell
git commit -m "message"
git commit -am "message" # ajoute et commit
# par ex update cheatsheet
```

## (3) Enregistrer les modifs vscode VERS git
```shell
git push origin $BRANCH
git push # dans la branche courante
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

# Sur vscode
On peut lire dans quel état se situe un fichier :
    U : unversioned
    A : added
    M : modified
    rien : dans le commit donc c'est bon



