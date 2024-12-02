# PRACTICAL USE CASE FOR FORK AND PIPE IN C

### Calcul de différentes sommes en fonction du process
```c
#include<stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <errno.h>


int main(int argc, char *argv[]){
    int arr[]={1,2,3,4,1,2};
    int arrsize=sizeof(arr)/sizeof(int);
    int start, end;
    int fd[2];

    // init pipe + gestion erreur
    if(pipe(fd)==-1){
        return 1;
    }

    int id=fork();
    if(id==-1){
        return 2;
    }

    if(id==0){ // child process
        start=0;
        end = arrsize / 2;
    } else { // parent process
        start = arrsize / 2;
        end = arrsize;
    }

    int sum = 0;
    int i;
    for(i=start;i<end;i++){
        sum += arr[i];
    }
    printf("calculated partial sum : %d\n",sum);
    return 0;
}
```
- child process : sum = 6
- parent process : sum = 7

### Utilisation du pipe pour communiquer le résultat
```c
int main(int argc, char *argv[]){
    int arr[]={1,2,3,4,1,2};
    int arrsize=sizeof(arr)/sizeof(int);
    int start, end;
    int fd[2];

    // init pipe + gestion erreur
    if(pipe(fd)==-1){
        return 1;
    }

    int id=fork();
    if(id==-1){
        return 2;
    }

    if(id==0){ // child process
        start=0;
        end = arrsize / 2;
    } else { // parent process
        start = arrsize / 2;
        end = arrsize;
    }

    int sum = 0;
    int i;
    for(i=start;i<end;i++){
        sum += arr[i];
    }
    printf("calculated partial sum : %d\n",sum);

    if(id==0){ // child process
        close(fd[0]); // close reading
        write(fd[1],&sum,sizeof(sum));
        close(fd[1]); // close writing
    } else { // parent process
        int sumFromChild;
        close(fd[1]); // close writing
        read(fd[0],&sumFromChild,sizeof(sumFromChild));
        close(fd[0]); // close reading

        int totalSum = sum + sumFromChild;
        printf("total sum : %d\n",totalSum);
        wait(NULL); // attend le child process before ending
    }
    return 0;
}
```
- Total sum = 13

### Gestion des erreurs pendant un read / write
```c
if(write(fd[1],&sum,sizeof(sum))==-1){
    return 3;
}

if(read(fd[0],&sumFromChild,sizeof(sumFromChild))==-1){
    return 4;
}
```