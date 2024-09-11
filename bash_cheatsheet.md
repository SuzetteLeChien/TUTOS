# Commandes unix pratiques


alt + tab pour changer de fenêtre boloss

## Effacer les lignes de code
```bash
clear
```
## Chemin du répertoire courant
```bash
pwd
```
## Se replacer à l'origine des dossiers de l'utilisateur actif dans le shell
```bash
cd ~
```
## Afficher les fichiers
```bash
ls # affiche les fichiers du répertoire courant
ls -a # tout même fichiers cachés
ls -l # fichiers sous forme de liste
ls -la # -l affiche la taille et les droits et -a affiche les fichiers cachés
```
## Manuel des commandes
```bash
man
```
## Copier un fichier
```bash
cp $FILEACOPIE $NEWFILE
```
## Déplacer la source dans la target
```bash
mv $SOURCE $TARGET
# si target existe, remplace son contenu par source
# target peut être un répertoire
# crée un nv répertoire s'il n'existe pas
```
## Supprimer un fichier
```bash
rm $FILE
```
## Supprimer un répertoire
```bash
rm -r $FILE
```
## Annuler la commande
```bash
ctrl+c # utile pour arrêter les boucles
```
## Afficher le type du fichier
```bash
file $FILE
```
## Imprimer le contenu d'un fichier dans le terminale
```bash
cat $FILE
```
## Afficher le cocntenu d'un fichier page par page
```bash
less $FILE
```
## Modifier un fichier dans le terminal
```bash
nano $FILE
# si on change le nom du fochierr, crée une copie des modifications
# ^X = ctrl X

# pareil que nano mais commandes plus difficiles
vim $FILE
```
## Ouvrir un fichier sur vscode
```bash
code $FILE
# si le fichier n'xiste pas, le crée sur vscode
```
