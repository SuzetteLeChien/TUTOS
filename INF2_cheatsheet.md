# CHEATSHEET INF2 : FINAUX

## Fichiers
- fichiers binaires ou fichiers texte
- Cycle de vie : Creation > Ouverture > Manipulation > Fermeture

### ouvrir un fichier
```python
with open("file","w",encoding="utf-8") as f:
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