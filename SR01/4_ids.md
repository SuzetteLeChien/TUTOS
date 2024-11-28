# PROCESS IDS

- every single process has their own id

## librairie pour obtenir les id
```c
#include <sys/wait.h>
```

## getpid
```c
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[]){
    int id=fork();
    printf("id=%d\n",getpid());
    return 0;
}
```
- on obtient deux id 3727 (chil porcess) et 3722 (main process)

## getppid
```c
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[]){
    int id=fork();
    printf("id=%d parent=%d\n",getpid(),getppid());
    return 0;
}
```
- on obtient l'id du process et l'id du père :
```
id=3784 parent=3778
id=3778 parent=3772
```

## child ends after main : zombie process
```c
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[]){
    int id=fork();
    if(id==0){ // chil process
        sleep(1); // wait for 1 sec
    }
    printf("id=%d parent=%d\n",getpid(),getppid());
    return 0;
}
```
- l'id du pere du child process ne correspond plus à l'id du main process
- un nouveau père a été assigné au chil process car le parent est mort avant l'exécution du fils
- la commande kill ne va plus pouvoir supprimer la mémoire du chil process qui est un zombie process

## forcer l'attente du père
```c
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[]){
    int id=fork();
    if(id==0){ // chil process
        sleep(1); // wait for 1 sec
    }
    printf("id=%d parent=%d\n",getpid(),getppid());

    if(id!=0){ // main process
        wait(NULL); 
        // paramètre = pointeur vers process
    }
    return 0;
}
```
- le main process s'affiche en premier mais attend quand même le chil process avant de die

## wait fonctionne sans vérifier l'id
```c
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[]){
    int id=fork();
    if(id==0){ // chil process
        sleep(1); // wait for 1 sec
    }
    printf("id=%d parent=%d\n",getpid(),getppid());

    if(wait(NULL)==-1){
        printf("no children to wait for\n");
    }
    return 0;
}
```
- le main s'affiche en premier
- on a ensuite le chil puis la ligne "no children to wait for"
- wait renvoie -1 en cas d'erreur

## return du wait
```c
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[]){
    int id=fork();
    if(id==0){ // chil process
        sleep(1); // wait for 1 sec
    }
    printf("id=%d parent=%d\n",getpid(),getppid());

    int res=wait(NULL);
    if(res==-1){
        printf("no children to wait for\n");
    } else {
        printf("%d finished execution",res);
    }
    return 0;
}
```
- d'abord main process
- ensuite chil process
- ensuite "no children to wait for"
- ensuite "{id du child} finished execution"

Wait renvoie donc l'id du process qu'on est a attendu  
--> usefull when you deal with multiple child processes