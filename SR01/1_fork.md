# FORK
## librairie linux nécessaire
```c
#include <unistd.h>
```
## utilisation de fork
```c
#include <unistd.h>

int main(int argc, char *argv[]){
    fork();
    printf("salut");
    return 0;
}
```
Ce programme va afficher deux fois salut  
--> un process fils est né avec fork et exécute également les lignes d'après  
--> tout ce qui est avant le fork n'est exécuté qu'une fois

## id du fork

```c
#include <unistd.h>

int main(int argc, char *argv[]){
    int id=fork();
    printf("salut id=%d",id);
    return 0;
}
```
--> deux id différents  
--> 0 pour le child process  
--> != 0 pour le père

## comportements différents grâce à l'id

```c
#include <unistd.h>

int main(int argc, char *argv[]){
    int id=fork();

    if(id==0){ // child process
        printf("hello from the child process\n");
    } else { // main process
        printf("hello from the main process\n");
    }
    return 0;
}
```

## double fork
```c
#include <unistd.h>

int main(int argc, char *argv[]){
    fork();
    fork();
    printf("salut");
    return 0;
}
```
--> "salut" va s'afficher 4 fois  
--> le premier fork crée un child process  
--> le deuxième fork crée un child process du main un un child process du child process : donc quatre process en même temps

## créer deux child process
```c
#include <unistd.h>

int main(int argc, char *argv[]){
    int id=fork();

    if(id!=0){ // main process
        fork();
    }
    printf("salut\n");
    return 0;
}
```
--> cette fois-ci on a bien trois "salut"
