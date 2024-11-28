# WAIT
- comment attendre qu'un process se termine ?

## main et child en même temps

```c
#include <unistd.h>

int main(int argc, char *argv[]){
    int id=fork();
    int n;

    if(id==0){ // child process
        n=1;
    } else { // main process
        n=6;
    }

    for(int i=n;i<n+5;i++){
        printf("%d",i);
        // attend d'avoir tous les input avant d'afficher donc il faut flush
        fflush(stdout);
    }
    return 0;
}
```
--> les nombres sont superposés : 1 6 2 7 3 8 4 9 5 10  
--> les deux process s'exécutent en même temps  
--> comportement unpredictable, l'ordre est choisi par l'ordi de façon aléatoire

## utilisation de wait
- inidique à l'ordi d'attendre qu'un child process (on ne précise pas lequel) s'exécute avant de s'exécuter à son tour  
- seulement dans le main process : si dans le child, va attendre indéfiniment car attend un child process qui n'existe pas
```c
#include <unistd.h>

int main(int argc, char *argv[]){
    int id=fork();
    int n;

    if(id==0){ // child process
        n=1;
    } else { // main process
        n=6;
    }
    if(id!=0){ // main process
        wait(); // attend le child process
    }
    for(int i=n;i<n+5;i++){
        printf("%d",i);
        // attend d'avoir tous les input avant d'afficher donc il faut flush
        fflush(stdout);
    }

    // retour à la ligne entre les deux et exécuté qu'une seule fois
    // si on met !=0 alors on tout sera sur la même ligne car main exécuté après
    if(id==0){
        printf("\n");
    }
    return 0;
}
```
--> dans ce cas-là on aura d'abord 12345\n puis 678910