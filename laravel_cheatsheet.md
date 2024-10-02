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
- peut être une page html / css basique qui est appelé quand on saisit la route correspondante dans le fichier web.php


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









