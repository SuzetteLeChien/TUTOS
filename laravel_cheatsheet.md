# Bases de Laravel

## Dossier routes
### api.php
### channels.php
### console.php
### web.php
- On y enregistre les routes web de notre application
#### exemple :
> cette route nous renvoie la vue 'welcome'
```php
Route::get('/', function () {
    return view('welcome');
});
```

## Dossier resources/views
- on y retrouve les différentes vues de notre application
- peut être une page html / css basique qui est appelée quand on saisit la route correspondante dans le fichier web.php


## Pour créer une nouvelle page
1) Se placer dans le fichier web.php et créer une nouvelle route
- par exemple
```php
Route::get('/nouvelleroute', function () {
    return view('nouvelle-vue');
});
```

2) Créer la nouvelle vue dans resources/views
- On crée un fichier nouvelle-vue.blade.php
- Créer le contenue que l'on souhaite dans le nouveau fichier

> La nouvelle route affichera la page nouvelle-vue.blade.php

## Architecture MVC
### 


## Commandes utiles
> Obtenir la liste des routes définies
```bash
php artisan route:list
```
 Cette commande affiche une table avec les informations suivantes pour chaque route :
- **Method** : les méthodes HTTP(GET, POST, PUT, DELETE...) associées à la route
- **URl** : l'URl de la route
- **Name** : le nom de la route, si elle en a un
- **Action** : l'action associée à la route généralement le contrôleur et la méthode

On peut également utiliser des options pour filtrer ou formater la sortie de la commande
> exemple
```bash
--path=/home #filtre les routes par chemin
--name=login #filtre les routes par un nom spécifique
--method=GET #filtre les routes par méthode HTTP
--reverse #inverse l'ordre des routes
```





