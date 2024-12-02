# Calling fork multiple times

- Comment savoir quel process est quel process ?
```c
#include <unistd.h>

int main(int argc, char *argv[]){
    int id1=fork();
    int id2=fork();
    return 0;
}
```
### schéma des relations entre process

- main process 

| actual id  | a     |
| ---------- |:-----:|
| id1        | x     |
| id2        | z     |

- first child  

| actual id  | x     |
| ---------- |:-----:|
| id1        | 0     |
| id2        | y     |

- second child of main process

| actual id  | z     |
| ---------- |:-----:|
| id1        | x     |
| id2        | 0     |

- child of the child process

| actual id  | y     |
| ---------- |:-----:|
| id1        | 0     |
| id2        | 0     |

--> le main process n'a accès qu'à ses enfants et pas au quatrième process

--> si le dernier id est à 0 alors pas de child

### Distinction entre les différents process
```c
#include <unistd.h>

int main(int argc, char *argv[]){
    int id1=fork();
    int id2=fork();
    if(id1==0){ // child of the parent process
        if(id2==0){ //  child of the child process
            printf("I'm the last child");
        }
        else{ // child with child
            printf("I'm the first child");
        }
    }
    else{ 
        if(id2==0){ // child of main with no child
            printf("I'm the second child");
        }
        else{ // main process
            printf("I'm the main process");
        }

    }
    return 0;
}
```
- wait() n'attend qu'un seul enfant (le premier qui se termine) donc on ne peut pas l'utiliser tel quel car le main a deux child processes


### Utilisation de wait avec plusieurs enfants
```c
#include <unistd.h>
#include<errno.h>

int main(int argc, char *argv[]){
    int id1=fork();
    int id2=fork();
    if(id1==0){
        if(id2==0){
            printf("I'm the last child");
        }
        else{
            printf("I'm the first child");
        }
    }
    else{ 
        if(id2==0){
            printf("I'm the second child");
        }
        else{
            printf("I'm the main process");
        }
    }
    while(wait(NULL)!=-1 || eerno!=ECHILD){
        printf("waited for a child to finish");
        // va s'afficher trois fois après exécution
    }
    return 0;
}
```
