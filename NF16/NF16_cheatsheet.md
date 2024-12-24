# CHEATSHEET NF16

## TD

### switch case
```c
switch(variable){
    case 1:
        // instructions
        break;
    case 2:
        // instructions
        break;
    default :
        printf("erreur");
}
```

### min to maj
```c
chaine[i]=chaine[i]+('a'-'A');
// table ASCII de 0 à 127
```

### vider le buffer après un getchar
```c
c = getchar () ;
while ( getchar () != ’\ n ’) ; // Vide le buffer
```

### scanf avec tableau de caractère
```c
scanf("%s", chaine) // chaine est déjà un pointeur
```

### pointeur sur tableau
```c
chaine[i] == *(chaine+i)
```

### SCANF
- scanf attend un pointeur vers l'emplacement mémoire où la valeur lue doit être stockée. --> attend l'adresse de l'emplacement

### Fonction qui interagit avec le terminal
```c
/* argc = nb d'arguments (compte le calcul) */
/* argv = liste des arguments */
/* argv[0] = calcul */
/* argv[1] = "-a" */
/* argv[2] = 10.0 */
int main(int argc, char * argv[]){}
```

### effacer le terminal
```c
system("clear");
```

### initialiser un pointeur
```c
int a, *p;

*p=a: // NON : impossible car p pas encore initialisé
p=&a; // OUI
```

### COMPLEXITE

#### Definition
- cout(d)=complexité en temps sur la donnée d
- meilleur cas : Min(n)=min{cout(d),d€Dn}
- pire cas : Max(n)=max{cout(d),d€Dn}

> n^x --> complexité polynomiale

> 2^n, 3^n, n! --> complexité exponentielle

si pas de division successive alors pas log


#### fonction de complexité
- O(f(n))={T(n):il existe des constantes >0 c et n0 tq 0<=T(n)<=cf(n) pour tout n>=n0}
- règle du maximum : O(f(n)+g(n)) = O(max(f(n),g(n)))
> SEULEMENT DANS R+  
> NOMBRE DE PARAM INDEPENDANT DE N  
> car f(n)+g(n)<=2*max(f(n),g(n))
> car max(f(n),g(n))<=f(n)+g(n)

- O(f(n)) réflexive, transitive et non symétrique
> f(n)<=cf(n)
> f € O(g) et g € O(h) --> f € O(h)
> f € O(g) mais g !€ O(f)

### INVARIANT DE BOUCLE
- Il s'agit d'une propriété vraie avant la première itération et qui reste vraie après chaque
itération.
- un invariant de boucle est souvent de la forme "telle variable admet telle quantité pour valeur"

> par exemple pour la recherche dichotomique :
il existe j appartenant à [gauche,droite] tel que t[j]=clé

> par exemple tri par sélection :
le sous tableau T[k+1,..,n] est trié

> par exemple FIBONACCI : fk=f(k+1) 0<=k<=n-1 à la kième itération

L'ensemble vide vérifie n'importe quelle propriété

### EXEMPLES DE COMPLEXITE
> VOYAGEUR DE COMMERCE : énumératif --> O(n*n!)


### TROIS ALGO A CONNAITRE

#### TOUR DE HANOI
O=origine, I=intermédiaire, D=destination
```
Procedure Hanoi(n:entier,O,D,I:entier)  
    si n>0 alors  
        Hanoi(n-1,O,I,D)  
        afficher('déplacer de',O,'vers',D)  
        Hanoi(n-1,I,D,O)
```
> complexité exponentielle : T(n)=2^n - 1

> NOTER DEMONSTRATION COMPLEXITE

#### N FACTORIELLE
```
f(n)=n*f(n-1)
f(0)=1

T(n)=t(n-1)+1
T(0)=0

--> suite arithmétique donc T(n)=T(0)+n --> O(n)
--> complexité LINEAIRE
```
#### SUITE DE FIBONACCI
```
Fibo(n:entier)  
    si (n==0) ou (n==1) retourner N  
    sinon retourner (Fibo(n-1)+Fibo(n-2))
```
> Le nombre de noeuds d'un arbre binaire est exponentiel en fonction de N

> donc complexité exponentielle sauf si on stocke les résultats avec un tableau --> complexité linéaire


### Dérécursification
```
Rec(N)  
    Action a1  
    Si p(N) alors // cas triviaux  
    sinon  
        action a2  
        R:= //fonction de N  
        Rec(R)

Iter(N)
    Action a1
    Tant que not p(N) faire
        action a2
        N:= //fonction de n
        action a1
    actions correspondant aux cas triviaux
```

### STRUCTURE DE DONNEES
#### TABLEAU NON TRIE
- Recherche : O(n)
- Suppression : O(n) si décale chaque case, O(1) si remplace par le dernier
- Min / Max : O(n)
- Successeur : on prend tous les éléments plus grands puis le plus petit parmis eux --> O(n)
- Prédécesseur : pareil

#### LISTES CHAINEES
- Recherche : O(n)
- Insertion : si au début O(1), sinon O(n)
- Prédécesseur : O(n)
- Suppression : O(1)

> Principe de sentinelle : on remplace NIL pour lier la dernière cellule avec la première cellule : une liset chaînée double avec sentinelle devient une liste circulaire  
> La première cellule avec NIL(L) ne fait généralement pas partie des données --> cellule factice

// recopier les schémas si besoin

> donc ne pas oublier de déclarer la cellule factice si on doit déclarer la sructure nous-même
```
succ[nil[L]]=tete[L]
pred[nil[L]]=queue[L]
succ[queue[L]]=nil[L]
pred[tete[L]]=nil[L]
```

- si on veut rajouter un élément new --> faire un malloc en copiant les attributs du nouvel élément et ajouter la copie

#### TABLEAU TRIE

- Recherche :


| Algo                  | itérations |
| --------------------- |:----------:|
| séquentiel            | n          |
| dichotomique itératif | log2(n)    |
| dichotomique récursif | log2(n)    |

- invariants de la recherche dichotomique :
> 1 <= g <= d <= N  
> T[i] <= x <= T[j]

#### PILE
- structure
```c
typedef struct Pile{
    int sommet; // indice de l'élément au sommet
    int tab[MAX];
} Pile;

/* SI LISTE CHAINEE */
typedef struct Noeud{
    int val;
    struct Noeud *suiv;
    struct Noeud *pred;
} Noeud;

typedef struct Pile{
    Noeud *sommet;
    int n; // taille de la pile
} Pile;

// CREER PILE
Pile* creer_pile(){
	Pile *p;
	p=(Pile*)malloc(sizeof(Pile));
	p->sommet=NULL;
	p->n=0;
	return p;
}

// EMPILER
int empiler(Pile *p, int x){
	if(p->n==MAX){
		printf("Pile pleine");
		return 1;
	}
	else{
		Nœud *new = (Noeud*)malloc(sizeof(Nœud));
		if(new==NULL){
			printf("erreur d'allocation mémoire");
			return 1;
		}
		new->val=x;
		new->suiv=NULL;

		p->sommet->suiv=new;
		p->sommet=new;
		p->n+=1;
		return 0;
	}
}
```
- Pile_vide(P)
```
Si sommet[P]=0
    alors retourner (vrai)
    sinon retourner (faux)
```
- Pile_pleine(P)
```
Si sommet[P]=Longueur[P]
    alors retourner(vrai)
    sinon retourner(faux)
```
- Empiler(P,x)
```
si (Pile_pleune(P)=vrai)
    alors Erreur('débordement')
    sinon somme[P]:=sommet[P]+1
        P[sommet[P]]:=x
```
- Dépiler(P)
```
Si Pile_vide(P)
    alors Erreur('débordement par défaut')
    sinon sommet[P] := sommet[P] - 1
        Retourner( P[sommet[P] + 1] )
```

- Insérer(P,x)
```
Si Pile_vide(P) ou x < P[sommet[P]]
alors Empiler(P, x)
sinon y := Dépiler(P)
    Insérer(P, x)
    Empiler(P, y)
```

#### FILE 
- structure
```c
typedef struct File{
    int tete; // indice de l'élément au sommet
    int queue;
    int tab[MAX];
} File;

/* SI LISTE CHAINEE */
typedef struct Noeud{
    int val;
    struct Noeud *suiv;
} Noeud;

typedef struct File{
    Noeud *tete;
    Noeud *queue;
    int n; // taille du tableau
} File;
```

### algo fusion de liste
```c
int fusion(Intervalle *I, Intervalle *J){
	if(!I || !J){
		return -1;
	}
	if(I->inf<=J->sup && I->sup>=J->inf){
		if(I->inf>J->inf){
			I->inf=J->inf;
		}
		if(I->sup<J(>sup)){
			I->sup=J->sup;
		}
		I->suiv=J->suiv;
		free(J);
		return 1;
	}
	return 0;
}
```

#### APRES UN MALLOC 
```c
Atome *New=(Atome*)malloc(sizeof(Atome));
if(New)==NULL return NULL;
```
#### COMPARER STR
```c
strcmp(s1,s2);
// 0 si identiques, 1 si différentes
```
