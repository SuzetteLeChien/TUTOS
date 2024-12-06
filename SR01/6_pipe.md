# Communicating between processes using pipes

### cas pratique : communiquer un int entre le fils et le père
```c
int main(int argc, char *argv[]){
    int fd[2]; // keys to write or read
    // fd[0] = read | fd[1] = write
    if(pipe(fd) == -1){ // creates the pipe
        printf("an error ocurred\n");
        return 1;
    }
    int id=fork();

    if(id==0){ // child process
        close(fd[0]); // close read
        int x;
        printf("input a number\n");
        scanf("%d",&x);
        // to send it to the parent process
        write(fd[1],&x,sizeof(int));
        close(fd[1]); // close write
    } else { // main process
        close(fd[1]); // close write
        int y;
        read(fd[0],&y,sizeof(int));
        close(fd[0]); // close read
        printf("got from child process %d",y);
    }
    
    return 0;
}
```
- write(pipe_write, adresse variable à lire, sizeof(variable))
- read(pipe_read, adresse où stocker la lecture, sizeof(variable))

### Réflexe à prendre : gestion des erreurs
```c
#include <unistd.h>

if(write(fd[1],&x,sizeof(int))==-1){
    printf("an error ocurred with writing\n");
    return 2;
}
if(read(fd[0],&x,sizeof(int))==-1){
    printf("an error ocurred with reading\n");
    return 3;
}

// pareil pour le fork
int id=fork();
if(id==-1){
    printf("an error ocurred with fork\n");
    return 1;
}
```

- on utilise des pipe entre des process de même hiérarchie

## Attention
### two way communication between processes
Si on read et write dans chaque process, un des deux peut aller plus vite que l'autre et l'autre ne recevra jamais l'information du pipe.

Pour régler ce problème on peut créer deux pipes :
```c
int p1[2]; // child to parent
int p2[2]; // parent to child
```
- p1 : child only writes, parent only reads
- p2 : child only reads, parent only writes

--> permet d'éviter les conflits