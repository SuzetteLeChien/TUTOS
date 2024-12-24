# NF16 : FINAUX

## TD
On peut créer un objet d'une structure dans une fonction sans utiliser de malloc si la structure est bien définie et qu'elle n'a pas besoin d'allocation dynamique

### structure FILE
```c
typedef struct file {
int tab [ MAXF ];
int tete ; // Premier element a defiler
int queue ; // Premier emplacement libre
} file ;
```
- La file est vide si tete==queue
- La file est pleine si la queue se trouve juste en dessous de la tête
> pleine si Tete[F]=(Queue[F]+1)%Longueur[F]

### structure PILE
```c
typedef struct pile {
int sommet ; // Indice de l ’ element au sommet de la pile
int tab [ MAXP ];
} pile ;
```

### Arbre k-aire
```c
typedef struct Cellule{
	int cle;
	struct Cellule *père;
	struct Cellule *filsG;
	struct Cellule *filsD;
}Cellule;
```
### Arbre binaire de recherche
#### Parcours d'un arbre binaire
1) Parcours préfixe
- racine > guche > droite

2) Parcours postfixe
- gauche > droite > racine

3) Parcours infixe
- gauche > racine > droite

#### Supprimer un noeud
- si aucun fils on supprime en modifiant le père
- si un fils on supprime et on rattache le fils au père
- si deux fils on remplace le noeud par le successeur (ou le prédecesseur ?)
> si x possède un sous-arbre droit non vide, le successeur est le plus petit élément de cet arbre
> si x possède un sous-arbre gauche non vide, le prédecesseur est le plus grand élément de cet arbre

#### Complexité des opérations de base
| Fonction   | Liste quelconque | Liste triée | ABR   |
| ---------- |:----------------:| :----------:| -----:|
| Ajouter    | O(1)             | O(n)        | O(h)  |
| Supprimer  | O(n)             | O(n)        | O(h)  |
| Rechercher | O(n)             | O(n)        | O(h)  |
| Intersecte | O(n)             | O(n)        | O(h)  |

Dans le cas général, on peut avoir un ABR de hauteur n (si on insère par ordre croissant).
Dans le cas d'un arbre complet on a h=log2(n).

#### Rotation droite
> Complexité O(1)
```
Rotd(x:Racine)
    Si gauche[x]!=NIL:
        y:=gauche[x]
        C:=droit[y]
        pere[y]:=pere[x]
        Si pere[x]!=NIL:
            Si gauche[pere[x]]=x:
                gauche[pere[x]]=y;
            Sinon:
                droit[pere[x]]=y;
        droit[y]:=x
        pere[x]:=y
        gauche[x]:=c
        Si C!=NIL:
            pere[C]:=x
        retourner y
```

#### Variation hauteur d'un noeud après Rotation
h'(v)=h(v)+DELTA si h(g)>h(d) ou (h(g)=h(d) et DELTA=1)  
      0 sinon

h=1+max(1+h(B),1+h(C),h(D))  
h'=1+max(h(B),1+h(C),1+h(D))

#### Algorithme récursif d'enracinage de x
> Complexité O(hauteur)
```
enraciner(r:Racine; e:entier)
    Si(cle[r]=e)
        retourner r
    Sinon si(cle[r]>e)
        enraciner(gauche[r],e) // remonte e au fils gauche
        retourner rotd(r) // enracine fils gauche
    Sinon si(cle[r]<e)
        enraciner(droit[r],e) // remonte e au fils droit
        retourner rotg(r) // enracine fils droit
```

#### Equilibre d'un noeud
h(gauche[x])-h(droit[x])

eqx=1 + max(h(B),h(C)) - h(D)

#### Rotation gauche droite
- CNS : X a un fils gauche Y et Y a un fils droit Z
1) Rotation gauche sur y
2) Rotation droite sur x

```
Rotgd ( x : Noeud ; Delta : entier )
    Si gauche [ x ] != NIL et droit [ gauche [ x ]] != NIL
        eqx := eq [ x ]
        gauche [ x ] := rotg ( gauche [ x ] , D1 ) // Rot gauche sur y
        eq [ x ] := eq [ x ]+ D1 // equilibre parent quand fils gauche varie de D1
        Si ( eqx > 0 ou ( eqx = 0 et D1 = 1) ) // variation pere quand fils varie
            Delta := D1
        Sinon
            Delta := 0
        z := rotd (x , D2 ) // totation droite sur x
        Delta := Delta + D2 // Delta total
        retourner z // z est la racine
```


### Passer de string à integer
```c 
while(expression[k]>='0' && expression[k]<='0'){
    nb=nb*10;
    nb=nb+(exp[k]-'0');
    k++;
}
```

