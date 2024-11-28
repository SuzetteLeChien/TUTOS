# VISUALIZATION OF A FORK CALL

- on reprend l'exemple de wait.md
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
        fflush(stdout);
    }

    if(id==0){
        printf("\n");
    }
    return 0;
}
```

## comparaison between main process memory and child process memory

| variable      | PP memory      | CP memory    |
| ------------- |:--------------:| ------------:|
| argc          | 1              | 1            |
| argv          | "main.exe"     | "main.exe"   |
| id            | 4300           | 0            |
| n             | 6              | 1            |
| n             | 6              | 2            |
| n             | 6              | 3            |
| n             | 6              | 4            |
| n             | 6              | 5            |
| n             | 7              | 5            |
| n             | 8              | 5            |
| n             | 9              | 5            |
| n             | 10             | 5            |

- the memory is getting copied from one process to another  
- when you execute it, each process has actually their own space in memory
- once fork is called, the execution line is split and depending on the process you get different things even though thery're executing the same code


