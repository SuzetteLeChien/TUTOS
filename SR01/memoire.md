# Les différents types de mémoire

## L'allocation statique
#### Lorsque le programme s'initialise, il demande une quantité de données pour la mémoire, laquelle ne pourra pas changer par la suite. La quantité nécessaire est spécifiée dans le code source du programme.

- En principe seuls les langages compilés permettent l'usage de l'allocation statique.

- L'avantage est sur la performance : la mémoire est immédiatement utilisable par le programme sans demander l'attribution d'espace mémoire.

- Ce type de mémoire manque cependant de souplesse car son allocation doit être prévue lors de l'écriture du programme et cela ne peut être modifié à l'exécution. On s'en sert donc principalement pour des variables globales dont les valeurs sont déjà connues à la compilation.

## L'allocation sur la stack
#### Cette allocation se fait lors de l'exécution du programme et obéit au principe de fonctionnement de la stack. Convient bien pour les variables locales.

- Fonctionne comme une pile : last in first out. Elle est de taille fixe mais l'allocation à l'intérieur est dynamique.

- Le pointeur référence toujours le haut de la stack, son accès est donc séquentiel. Le pointeur ne peut pas aller au delà des limites de la stack, il s'agit sinon de stack overflow, une tentative d'écriture dans des zones de mémoire adjacente. --> aboutit à un crash du programme

- Comme les accès à la stack sont séquentiels et que les mêmes adresses mémoire tendent à être réutilisées, le processeur optimise l’accès à cet espace mémoire en le mettant dans son cache. Par conséquent, les lectures et écritures dans la stack sont très performantes

- En revanche, comme sa taille est déclarée lors de la création du thread, il n’est pas possible d’y stocker des quantités trop importantes de données. En outre, chaque thread possède une stack propre. Dans les langages permettant le multithreading, la stack ne peut servir à partager de l’informations entre différents threads.

La mémoire dans la stack se libère de façon automatique : à la fin d'une fonction, toutes les variables qu'elle a déclarées sont instantanément supprimées.

## L'allocation sur la heap : malloc
#### Cette allocation permet le stockage de volumes de données plus importants, leur accès aléatoire et le partage d'informations entre différentes fonctions et threads

- Il n'y a donc aucune contrainte de taille,lorsque le process nécessite plus de mémoire il en fait la demande à l'OS (système d'exploitation).

- La heap est plus flexible que la stack. Elle permet l'allocation de variables globales partagées entre plusieurs fonctions et permet le partage de valeurs entre threads d'un même process.

- On doit s'assurer de bien libérer la mémoire à la fin du programme (free()) au risque d'aboutir à une fuite de mémoire.

- on utilise le malloc() en c.


## RAPPEL
Un processus est une collection d’espace mémoire virtuel, de code, de données et de ressources système. Un thread est du code qui doit être exécuté en série dans un processus. Un processeur exécute des threads, et non des processus, de sorte que chaque application a au moins un processus, et un processus a toujours au moins un thread d’exécution, appelé thread principal. Un processus peut avoir plusieurs threads en plus du thread principal.

- Le multithreading permet au CPU (processeur) de gérer plusieurs tâches ou thread de façon pseudo-simultanée. Il s'agit d'un moyen intelligent et économique d’augmenter les performances des processeurs.
- Au lieu de maintenir un processus pendant une longue période, le système passe rapidement à la tâche suivante avec le multithreading, même s’il attend toujours des données. De cette façon, il n’y a pratiquement pas de temps d’attente.

