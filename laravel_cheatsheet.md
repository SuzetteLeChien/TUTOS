# Bases de Laravel

## Qu'est ce que Laravel ?
Laravel est un framework PHP open-source qui facilite le dévelopement d'applications web en fournissant une architecture MVC (Modèle-Vue-Contrôleur) et une série d'outils et de fonctionnalités.

## Quels sont ses avantages ?
1) **Architecture MVC**

Laravel suit le modèle MVC, ce qui permet une séparation claire des responsabilités entre les modèles, les vues et les contrôleurs, facilitant ainsi la gestion et la maintenance du code.

2) **Outils de Développement Puissants**

Laravel est livré avec des outils comme Artisan (un outil en ligne de commande) et Tinker (un REPL pour PHP), qui simplifient de nombreuses tâches de développement.

3) **Système de routage avancé**

Laravel offre un système de routage puissant et flexible, permettant de définir des routes de manière simple et efficace.

4) **Système de Templates Blade**

Blade est le moteur de templates de Laravel, qui permet de créer des vues dynamiques et réutilisables avec une syntaxe simple et intuitive.

5) **Sécurité intégrée**

Laravel inclut des fonctionnalités de sécurité intégrées, comme la protection contre les injections SQL, les attaques XSS (Cross-Site Scripting) et les attaques CSRF (Cross-Site Request Forgery).

6) **Extensibilité**

Laravel est hautement extensible grâce à son système de packages et de composants, permettant d'ajouter facilement de nouvelles fonctionnalités à votre application.


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
--path=/home #filtre les routes par chemin : ici /home
--name=login #filtre les routes par un nom spécifique
--method=GET #filtre les routes par méthode HTTP : ici GET
--reverse #inverse l'ordre des routes
```





