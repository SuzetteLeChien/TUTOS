# Commandes unix pratiques


alt + tab pour changer de fenêtre boloss
``` bash
clear # permet d'effacer les lignes de code

pwd # affiche le chemin du répertoire courant

cd ~ # à l'origine des dossiers de l'utilisateur actif dans le shell

ls # affiche les fichiers du répertoire courant
ls -a # tout même fichiers cachés
ls -l # fichiers sous forme de liste
ls -la # -l affiche la taille et les droits et -a affiche les fichiers cachés

man # manuel des commandes

cp $FILEACOPIE $NEWFILE # copier un fichier

mv $source $target # déplace la source dans la target
                   # si target existe, remplace son contenu par source
                   # target peut être un répertoire
                   # crée un nv répertoire s'il n'existe pas

rm $FILE # remove = supp

ctrl+c # annule la commande (utile pour arrêter des boucles)

file $FILE # affiche le type du fichier

cat $FILE # imprime le contenu du fichier dans le terminal

less $FILE # lit le contenu d'un fichier
           # l'affiche page par page

nano $FILE # modifier un fichier dans le terminal
           # si on change le nom du fichier crée une copie des modifications
           # ^X = ctrl X

vim $FILE # pareil que nano mais pas le guide des commandes donc plus difficiles

code $FILE # ouvre le fichier sur vscode
           # si le fichier n'existe pas, le crée sur vscode
```