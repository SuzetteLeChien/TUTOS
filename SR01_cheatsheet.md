# TRUCS A RETENIR POUR SR01

Code C
-
### Boucle For
```c
for(int i=0; i<MAX; i++){/* instructions */}
```

### Structure
```c
typedef struct name{
 // instructions
} NewName;

// ou après avoir défini la structure
typedef struct name NewName;
```

### Exemple de structure et pointeur sur structure
```C
// STRUCTURE ELEMENT
struct Element {
    int col;
    int val;
    struct Element *suivant;
} ;
typedef struct Element element;


// TYPE LISTE_LIGNE
typedef element *liste_ligne;


// STRUCTURE MATRICE CREUSE
struct MatriceCreuse {
    int Nlignes;
    int Ncolonnes;
    liste_ligne *tab_lignes;
} ;
typedef struct MatriceCreuse matrice_creuse;
```

### Exemple de malloc
```C
// on alloue de l'espace pour un tableau de pointeurs de taille l
int **tab=(int **)malloc(l * sizeof(int *));

// on alloue de l'espace pour chaque ligne
for (int i = 0; i < l; i++)
{
    tab[i]=(int *)malloc(c *sizeof(int));
}

// 3D
int ***tab(int ***)malloc(d1*sizeof(int **));
for(int i=0;i<d1;i++){
	tab[i]=(int **)malloc(d2*sizeof(int *));

	for(int j=0;j<d2;j++){
		tab[i][j]=(int *)malloc(d3*sizeof(int));
	}
}

```

### do while
```c
do{
    // instructions
}
while();
```

### switch type
```c
switch(variable){
    case 1:
        // instructions
        break;
    
    case 2:
        // instructions
        break;
}
```


### Initialiser un tableau
```c
int tab[MAX]={1,2,3}
```

### Modulo

```c
entier%2
```

### Affichage %

```c
%s // chaîne de caractère
%c // caractère
%lu // taille --> par ex sizeof(int)

/* DECIMAL */
%ld // entier de type long int
%u // entier unsigned int
%ul // entier unsigned long int
%+d // affiche le signe puis l'entier
%.4d // 4 chiffres, 0 à gauche pour compléter
%4d // 4 caractères, espace à gauche pour compléter
%-4d // 4 caractères, espace à droite pour compléter
%6.4d // largeur min de 6 pour l'affichage + précision de 4 chiffres

/* OCTAL */
%o // octal d'un unsigned int
%lo // octal d'un unsigned long int
%#o // pareil aevc préfixe 0


/* HEXA */
%X // hexa d'un unsigned int en MAJ
%x // pareil mais en min
%lX // hexa d'un unsigned long int
%#x // hexa avec le préfixe 0x
%#6.4X // le 6 s'applique avant d'avoir mis le préfixe

/* FLOTTANT */
%.2f // 2 chiffres après la virgule
%#.0f // on affiche le point décimal même si aucune décimale

/* NOTATION SCIENTIFIQUE */
%E //  1.23456e123 devient 1.234560E+123 tjrs 6 chiffres après virgule
%.0E // 1E+123
%#.0E // point décimale 1.E+123

/* PAS COMPRIS */
%G // Affiche le nombre en notation scientifique si l'exposant est >= à 4 ou <= à -4, sinon utilise la notation décimale. Il supprime les zéros inutiles à la fin du nombre.
```


### Priorité des opérateurs
```c
x = x && y || z; 
/*opérateur logique voit 0 comme faux et tout le reste comme vrai (= 1)*/

int x = 2, y = 1, z = 0;
z += -x++ + ++y; 
/*pré incrémentation prioritaire*/
/*post incrémentation se fait après le -*/
/*on prend la valeur de x avant qu'elle soit post incrémentée*/
/*x est quand même modifié*/
// donc z=-2 + 2=0
// x = 2+1=3 et y=2
/* ++ ou -- modifie la valeur*/

int x = 3, z = 0;        
z = x / ++x;
/*z=3/4*/
/*toujours 1 quand division entière*/
/*x=4  z=1*/ 


int x = 03, y = 02, z = 01;
int a, b;
a = x | y & ~z;           
b = x ^ y & ~z; 
/*opérateur bit à bit donc il faut convertir en bit*/
/*représenté en octale*/
/*en décimal donne 3,2 et 1*/
/*en binaire donne 0011, 0010 et 0001*/

/*~z=1110*/
/*y & ~z donne 0010 en comparant bit à bit avec et*/
/* | = ou donc renvoie 0011*/
/*donc a=3*/

/* ^ = ou exclusif*/
/*donc b=0001=1*/


int x = 01, y = -01;
int a;
a = ~x | x;                
y <<= 3;
/*comme décalage on met sur 8 bits*/
/*je l'ai pas fait mais ça donne le même résultat*/

/*x=0001*/
/*~x donne 1110*/
/*1110 | 0001 = 1111*/
/*a=1111 = -1*/

/*pour le passer du - au + on inverse les bits puis +1*/
/*y=1111*/
/*<<= 3 : décalage à gauche de 3 on ajoute des 0 à droite*/
/*y=1000 donne 0111+1=1000=-8*/
/*toujours un bit de signe*/

int x = 3, y = 2;
int a;
a = x < y ? x++ : y++;
/* x > y donc on n'entre pas et on incrémente y*/
/*y avec incrémentation post fixée*/
/*a prend donc la valeur de y et y est incrémenté après*/
/*a=2, x=3 et y=3*/

int x = -1, y = -1, z = -1;
int a;
a = ++x && ++y || ++z;    
/*x y et z deviennent 0*/
/* le && lit un 0 avec x donc ne rentre même pas dans y*/
/*du coup y n'est pas incrémenté*/
/*donc on trouve y=-1*/
/*a = 0*/    
```

### Fonctions utiles
```c
// 1) pour lire une chaîne rentrée par l'utilisateur 
char chaine[10];
fgets(chaine,sizeof(chaine),stdin);

// 2) comparer des chaines
// si pareil strcmp renvoie 0
if (strcmp(argv[1],"-a")==0)

// 3) convertir char en float
atof(argv[i]); // renvoie un double

// trouver taille d'un tableau
#define TAILLE(tableau) (sizeof(tableau) / sizeof((tableau)[0]))
```

### Fonction avec matrice en paramètres
- ces paramètres sont équivalents :
```c
void matrice_info(int tab[N][M])
void matrice_info(int tab[][M])
void matrice_info(int (*tab)[M])

// pour la matrice (int tab[N][M]), l'élément tab[i][j] se trouve à l'adresse tab + (i*M+j)*sizeof(int)
```

### Fonction qui interagit avec le terminal
```c
/* argc = nb d'arguments (compte le calcul) */
/* argv = liste des arguments */
/* argv[0] = calcul */
/* argv[1] = "-a" */
/* argv[2] = 10.0 */
int main(int argc, char * argv[]){}
```


La compilation
-
C'est un processus complexe :
1) pré-traitement
2) compilation
3) assemblage
4) édition de lien

--> tout est compris dans le gcc -o

### 1. Pré-traitement
- traite les commandes #
- supprime les commentaires

**source.c.h --> source pré-traitée.i**

### 2. Compilation
- génère un fichier source en langage assembleur

**source pré-traitée.i --> source assembleur.s**

### 3. Assemblage
- génère un fichier en code machine

**source assembleur.s --> objet.o**

### 4. Edition de liens
- génère un exécutable

**objet.o --> exécutable.exe**


### Bibliothèque
- STATIQUE = fait une copie de toutes les fonctions des bibliothèques utilisées
- DYNAMIQUE = copie juste le nom de la bibliothèque et compile au moment de l'exécution (-lm)

## Exemple d'annales
```C
// triangle de Pascal --> affichage pyramide
for(i=0;i<nbL;i++){
	for(j=0;j<t[i]->nl;j++){
		printf("%3d",t[i]->tab[min(j,i-j)]);}}

// min to maj
chaine[i]=chaine[i]+('a'-'A');

// Retourne le nombre de caractères sans le '\0'.
strlen(chaine)

// tableau
t[i][j]=1 ;
*(t[i]+j)=1;
*(*(t+i)+j)=1;

// pointeurs
int arr[] = {1, 2, 3, 4, 5};
int *ptr = arr;
int *pt = arr;
int a = *ptr++;
int b = ++*pt;
- Sachant que l’adresse du tableau arr est ox10 et un entier est codé sur 4 octets
donnez les valeur de a, ptr, *ptr, b, pt, arr
• a = 1
• ptr = Adresse du deuxième élément du tableau arr (0x10 + 4 = 0x14)
• *ptr = 2
• b = 2
• pt = Adresse du premier élément du tableau arr (0x10)
• arr = Adresse du début du tableau arr (0x10) 
```

- ATTENTION --> possible de définir une fonction après le main si déclarée avant
- %s avec pointeur sur chaîne de caractère imprime la chaîne de caractère en entier (sans *)
- %s avec autre chose qu'un pointeur vers caractère renvoie une erreur
- d'abord accès aux champs d'une structure puis opération


