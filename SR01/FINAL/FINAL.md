# SR01 : A RETENIR POUR LE FINAL

## TD

1) Grep
- sert à rechercher des motifs spécifiques dans des fichiers ou des flux de données

2) Sed
- sert à éditer des textes : modifier, supprimer, insérer ou transformer

## GREP + REGEX
### options du GREP
```bash
grep -E // extended, pareil que egrep
grep -P // Perl regular expression --> compatible avec des expressions régulières Perl
grep -l // liste des fichiers avec match
grep -L // liste des fichiers sans match
grep -v // affichage des lignes ne contenant pas la chaîne précisée
grep -n // affiche les numéros de ligne
grep -c // compte le nombre de ligne
```
- On peut cumuler des options (par ex grep -vcE)
- on peut utiliser un pipe | par exemple sur un echo

```bash
[:punct:] // ponctuation
[:space:] // espaces
[:digit:] // chiffres
[:alpha:] // lettres
[:alnum:] // alphanumérique
```

- **Comment vérifier qu'une chaîne contient les deux**
```bash
echo "salut, " | grep [[:punct:]] | grep [[:space:]]
```

- **Comment vérifier qu'une chaîne contient un des deux**
```bash
echo "," | grep -E "[[:punct:]|[:space:]]"
// guillemets pour ne pas confondre le ou avec un pipe
// expression étendue donc -E
```

- **Afficher les téléphone qui commencent par 06 et qui ont 10 chiffres**
```bash
grep -E ^06[[:digit:]]{8}$ tel.txt
```

--> dès qu'on veut compter un ou des caractères on les mets entre crochets puis on met le nombre de fois attendu  

- **Compter les numéros qui ne correspondent pas**
```bash
grep -vcE ^06[[:digit:]]{8}$ tel.txt
// -v = lignes qui ne correspondent pas
// -c = count
// -E = extended version
```

- **Un caractère ou un caractère**
```bash
"[a|b]"
[ab]
// si suite de caractère
(abc|def)
```
> Par exemple numéros qui commencent par 06 ou 07
```bash
grep -E "^0[6|7][[:digit:]]{8}$" tel.txt
// ou
grep -E ^0[67][[:digit:]]{8}$ tel.txt
```

- **On veut maintenant intégrer les signes de ponctuation**
```bash
// première approche
grep -E ^0[67][[:punct:]]?[[:digit]]{2}\
[[:punct:]]?[[:digit:]]{2}\
[[:punct:]]?[[:digit:]]{2}\
[[:punct:]]?[[:digit:]]{2}$ tel.txt

// ? == {0,1}
// on peut simplifier

grep -E "^0[67]([[:punct:]]?[[:digit:]]{2}){4}$" tel.txt
// on répète quatre fois ce qui est entre parenthèse
// guillemets à cause des parenthèses
```

- **Trouver les URL de la forme lettre://lettre ou chiffre ou ponctuation**
```bash
grep -E ^[[:alpha:]]+://[[:alnum:]\.]+$ url.txt

// + == {1,} --> au moins une fois
// \. caractère spécial .
```

- **Trouver les URL de la même forme mais sans commencer ou finir par un point et sans avoir plusieurs points d'affilé**
```bash
grep -E "^[[:alpha:]]{4}://([[:alnum:]][\.]?[[:alnum:]]+)*$" url.txt

// * signifie 0 ou plusieurs occurrences
// premier alnum avec rien après signifie qu'il est obligatoire
```

- **Pareil mais avec numéro de port à la fin**
```bash
grep -E "^(ftp|http)://([[:alnum:]][\.]?[[:alnum:]]+)*(:[[:digit]]+)?$ url.txt
```

## SED

- **Capturer le domaine d'une adresse mail**
```bash
echo <mail> | sed 's/.*@\(.*\)/domaine=\1/'
echo "mathilde.wallut@gmail.com" | sed 's/\(.*\)\.\(.*\)@\(etu\.*\)/prenom = \1 \nnom = \2 \ndomaine = \3/'
```
- s = substitute
- expression entre \()\ est celle capturée qui va être substituée
- \n = nième groupe capturé
- \(expression à caturer)


## Administration système
```bash
whoami // info login courant
id Malena // info de l'user Malena
who // info users connectés sur le serveur
tty // console depuis laquelle on est connecté
```

