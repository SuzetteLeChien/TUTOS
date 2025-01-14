# [GIT CHEATSHEET](#FF0000)
## ATTENTION A ETRE A JOUR ENTRE GIT / VS
### Commencer par se placer dans le bon répertoire avec un cd

## Enregistrer les modifs DE git VERS vscode
```shell
git pull origin $BRANCH
# souvent BRANCH = main mais faire gaffe à ce qu'on soit dans la bonne branche
```
## Récupérer DE git VERS vscode sans enregistrer
```shell
git fetch
# pas trop compris
```

## Verifier l'état
```shell
git status
```

## Enregistrer des modifs DE vs VERS git en trois étapes
### (1) ajout (AVANT DE PUSH)
Bien sûr s'assurer que les ajouts sont enregistrés sur vscode
```shell
git add $FILE
git add . # tous les fichiers de git status en rouge
git add -p # demande si tu veux ajt les diff modifs
git remove $FILE # enlève le fichier qui a été add mais pas push
git reset # annule l'ancien ajout
```

### (2) commit avec un message expliquant les modifs
```shell
git commit -m "message"
git commit -am "message" # ajoute et commit
# par ex update cheatsheet
```

### (3) Enregistrer les modifs vscode VERS git
```shell
git push origin $BRANCH
git push # dans la branche courante
# attention à la branche
```


## Vérifier l'état de l'avancement
```shell
git log
```

## Créer une nouvelle branche
partir d'une branche à jour (par ex main) suivi d'un git pull origin main
```shell
git checkout -b $BRANCH
```

## Changer de branche
```shell
git checkout $BRANCH
```

## Voir les modifications faites depuis le dernier pull
```shell
git diff
git diff $FILE
```

## Annuler toutes les mofifs vues par le git diff
```shell
git checkout .
git checkout $FILE
```

## permet de créer un dossier local du repo
### se placer là où on veut copier le repo
```shell
git clone git@github.com:SuzetteLeChien/nomdurepo.git
```

## créer un repo à partir d'un dossier local
- se placer dans le dossier
- le dossier doit être non vide
```shell
git init
git add .
git commit -m "first commit"
# aller sur git et créer un repo du même nom
# taper ces trois commandes sur le terminal
git remote add origin git@github.com:SuzetteLeChien/nomdurepo.git
git branch -M main
git push -u origin main
```

## Retirer un fichier git caché
- se placer dans le dossier
```shell
rm -rf .git

# on peut vérifier si le fichier git est toujours dans le dossier en se plaçant dans le répertoire d'avant puis :
# ls -la $FOLDER
```

## Renommer une branche localement
```shell
# se placer dans la branche
git chekout <ancien_nom>

# renommer la branche
git branch -m <ancien-nom> <nouveau-nom>

# supprimer l'ancienne branche
git push origin --delete <ancien-nom>

# push la nouvelle branche
git push origin <nouveau-nom>
```

## Sur vscode
```
On peut lire dans quel état se situe un fichier :
    U : unversioned
    A : added
    M : modified
    rien : dans le commit donc c'est bon
```

## Erreurs à éviter
### (1) Créer un submodule sans faire exprès
En copiant ou déplaçant un repo dans un autre repo on crée un submodule qu'on ne pourra pas ouvrir sur git et dont il sera compliqué d'afficher les modifications.
Pour éviter ça il faut supprimer les fichier .git cachés dans les repo avant de les déplacer dans le repo principal et de les push.
