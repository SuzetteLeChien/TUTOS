# Executing commands in c

```c
#include <sys/types.h>
int execlp(nom_fichier_a_ex,argv[0],argv[1],...,argv[n]);

// exemple : exécution de ls -la
// chercher les commandes bash dans usr/bin
execlp("/usr/bin/ls","ls","-la",NULL);

// autre exemple : wc -l
execlp("/usr/bin/wc","wc","-l",NULL);
```
