# CHEATSHEET JAVASCRIPT

## Changer un texte html en cliquant sur un bouton
```html
<p id="demo">Mathilde</p>

<button type="button" onclick='document.getElementById("demo").innerHTML = "Wallut"'>Click Me!</button>
```
En cliquant sur le bouton "Click Me!", le texte "Mathilde" va se changer en "Wallut"



## Changer la source d'une image en cliquant sur un bouton
```html
<p>In this case JavaScript changes the value of the src (source) attribute of an image.</p>

<button onclick="document.getElementById('IMAGE').src='pic_bulbon.gif'">Allumer</button>

<img id="IMAGE" src="pic_bulboff.gif" style="width:100px">

<button onclick="document.getElementById('IMAGE').src='pic_bulboff.gif'">Eteindre</button>
```
En cliquant sur "Allumer", la source de l'image va être modifiée et l'ampoule va s'allumer et inversement pour le bouton "Eteindre"

## Changer le style d'un élément html (CSS)
```html
<p id="demo">élément à modifier</p>

<button type="button" onclick="document.getElementById('demo').style.fontSize='35px'">Bouton</button>
```
En cliquant sur le bouton, l'élément à modifier va changer de style CSS

## Cacher un élément html
```html
<p id="demo">élément à cacher</p>

<button type="button" onclick="document.getElementById('demo').style.display='none'">Bouton</button>
```
En cliquant sur le bouton, l'élément à cacher va disparaître de la page

## Faire apparaître un élément html
```html
<p id="demo" style="display:none">élément caché</p>

<button type="button" onclick="document.getElementById('demo').style.display='block'">Bouton</button>
```
En cliquant sur le bouton, l'élément caché va apparaître

## Créer des fonctions JavaScript
```html
<p id="demo">a paragraph</p>

<button type="button" onclick="myFunction()">Bouton</button>

<script>
function myFunction() {
  document.getElementById("demo").innerHTML = "Paragraph changed.";
}
</script>
```
- En cliquant sur le bouton on utilise la fonction définie en java script
- on peut définir une fonction dans le head ou le body
- un code java script inséré dans du html doit être placé entre des balises script

## JavaScript externe
```html
<script src="myScript1.js"></script>
<script src="myScript2.js"></script>
```
- on crée des fichiers .js dans lesquels on décrit des fonctions
- pour utiliser plusieurs fichiers dans le html on utilise plusieurs balises script
- permet une meilleure lisibilité