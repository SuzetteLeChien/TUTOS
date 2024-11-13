# EXPO CHEATSHEET

## lancer l'appli
```bash
npm install // installer les dépendances
npx expo start
```
Ensuite scanner le QrCode avec l'appli expo go sur téléphone (sinon simulateur sur ordi mais plus compliqué).

##
Beaucoup de package existent déjà, par exemple notifications push, caméra...


## Fichiers de l'appli SKIUT

## Répertoire components>navigation
## TabBarButton.jsx
Gère une barre de navigation personnalisée. 
- affiche un onglet interactif dans une barre de navigation avec des icônes et des textes stylisés
- applique des effets visuels pour signaler à l'utilisateur quel onglet est actif
- crée une interface cohérente et stylisée en utilisant des polices et des couleurs spécifiques

### ANALYSE DETAILLEE
1) Importation des dépendances
- Text, Pressable, Stylesheet : composants et fonctions de base de React Native
- useEffect : Hook React pour déclancher des effets secondaires (ici pour animer un changement de style)
- TabBarIcon : composant personnalisé pour afficher une icône --> ficher TabBarIcon.tsx
- useSharedValue, withSpring : react-native-reanimated, utilisé pour créer des animations fluides et réactives
- Fonts, loadFonts : constants pour les polices personnalisées définies dans le projet --> Font.Title.Bold utilisé pour styliser le texte

2) Déclaration et animation de scale avec useSharedValue
- scale est une valeur partagée initialisée à 0
- Lorsque l'onglet est focalisé (isFocused), scale passe de 0 à 1 ou inversement avec une animation de ressort (withSpring)

3) Rendu du composant
- Le composant retourne une structure avec Pressable, un bouton réactif qui détecte les pressions de l'utilisateur
- A l'intérieur de Pressable il affoche :
    - TabBarIcon : icône correspondant à l'onglet, avec la couleur (color) et l'icône (icon) en propriétés
    - Text : affoche le label de l'onglet avec un style de couleur, une taille de police fixe de 13, et une police en gras définie par Fonts.Title.Bold

4) Style du conteneur
- container : dispose les éléments au centre avec flex 1, justifyContent : 'center' et alignItems: 'center'. gap: 4 ajoute un espacement de 4 unités entre les éléments enfants.

## TabBar.jsx
Définit et personnalise la barre de navigation.
- affiche la barre 
- gère la navigation entre différents écrans
- affiche des styles spécifiques / animations pour chaque onglet

### ANALYSE DETAILLEE

1) Propriétés et Structure
- Ce composant utilise trois propriétés clés :
    - state : état de navigation, inclut les routes et l'index de l'onglet actuellement actif
    - descriptors : continent des info et options de chaqeu route, y compris icônes et labels
    - navigation : permet de déclencher des actions de navigation (aller vers un autre écran, gérer les évènements des onglets...)

2) Rendu des onglets
- La barre est rendue à l'intérieur d'une view avec le style styles.tabbar
- Chaque onglet est généré en utilisant state.routes.map pour itérer sur toutes les routes définies

3) Options et configurations des onglets
- Pour chaqeu route, le composant récupère l'icône (icon) et le label (tabBarLabel ou title) à partir de options
- Le composant utilise la propriété isFocused pour identifier l'onglet actuellement sélectionné

4) Interaction avec les onglets
- onPress : gère les clics sur les onglets --> si l'onglet est déjà sélectionné (isFocused) il reste inchangé, sinon il navigue vers la nouvelle route
- onLongPress : permet de déclencher des actions supplémentaires en cas de pression longue, émettant un évènement tabLongpress

5) Condition d'affichage de l'icône
- si options.noIcon est défini --> N'AFFICHE PAS D'ICONE

6) Composant TabBarButton
- chaque onglet est rendu avec le composant TabBarButton, qui reçoit des informationns comme l'icône, le label, la couleur et les évènements onPress et onLongPress. Ce composant est responsable de l'affichage visuel de chaque onglet et de ses animations.

7) Styles de la barre
- styles.tabbar applique les styles de la barre :
    - posistionnée en bas (bottom : 25) et occupe une largeur de 90% avec des marges (marginHorizontal: 20)
    - justifyContent: 'space-between' --> espave les onglets de manière uniforme
    - le style de fond blanc avec coins arrondis (borderRadius: 25) donne l'apparence de barre flottante
    - ombrage pour effet visuel


## Répertoire app

### _layout.tsx
Sert de plan général pour organiser la navigation et la disposition des onglets dans l'application en définissant comment chaque écran doit être affiché et en configurant l'apparence et le comportement des éléments de navigation.

### ANALYSE DETAILLEE

1) Importations principales
- Tabs : composant fourni pas expo-router pour créer une navigation par onglets
- TabBar : composant personnalisé pour la barre de navigation défini dans TabBar --> remplace la barre d'onglet par défaut

2) Structure du Layout
- Le composant RootLayout retourne un composant Tabs qui définit la navigation par onglets
- La prop tabBar={props => <TabBar {....props}/>} remplace la barre d'onglets par défaut par le composant personnalisé TabBar
- La prop screenOptions={{ headerShown: false }} désactive les headers de navigation en haut de chaque écran --> plus de place pour le contenu

3) Définition des écrans (onglets)
- Tabs.Screen définit chaque écran ou onglet
    - chaque écran a une propriété name qui correspond à la route et au composant qui sera chargé pour cet onglet
    - La prop options contient des propriétés supplémentaires pour l'affchage et la personnalisation :
        - title : label de l'onglet
        - icon
        - noIcon --> PAS D'ICONE POUR PROFIL

### Fonctionnement de chaque onglet
1) Home : route index avec l'icône home
2) Planning: route planning avec l'icône calendar
3) Potins : route potins avec l'icône chatbox
4) Défis : route défis avec l'icône trophy
5) Profil : route profil SANS ICÔNE

## defis.tsx
Crée un écran de base pour l'onglet défis --> message centré pour indiquer qu'il s'agit d'une page en attente de contenu. COnstitue un point de départ pour ajouter les fonctionnalités et l'interface utilisateur propre à la section "défis" de l'application.

### ANALYSE DETAILLEE
1) Structure et rendu de l'écran
- Le composant Index est une fonction qui retourne du JSX, la syntaxe utilisée dans React pour structurer le contenu de l'interface utilisateur
- Ce composant utilise un View qui prend tout l’espace disponible de l’écran (flex: 1) pour afficher son contenu au centre, à la fois verticalement et horizontalement.

2) Affichage du texte 
- Un composant Text affiche le message : "Edit app/defis.tsx to edit this screen."
- Le texte est probablement un message temporaire qui guide les développeurs, leur rappelant qu’ils peuvent personnaliser cet écran en modifiant le fichier defis.tsx.

3) Explication des styles appliqués
- flex: 1 : Indique que View doit occuper tout l'espace vertical disponible.
- justifyContent: "center" : Centre le contenu verticalement.
- alignItems: "center" : Centre le contenu horizontalement.

## profil.tsx
Crée un écran de base pour l'onglet profil --> message centré pour indiquer qu'il s'agit d'une page en attente de contenu. COnstitue un point de départ pour ajouter les fonctionnalités et l'interface utilisateur propre à la section "profil" de l'application.

### ANALYSE DETAILLEE
1) Structure du composant
- Le composant Index est une fonction React qui retourne une structure en JSX. Cette structure est utilisée pour définir la mise en page de l'écran.
- Le composant principal est un View (conteneur) qui prend toute la surface disponible de l’écran

2) Styles appliqués
- Le style flex: 1 est appliqué pour que le View occupe tout l'espace disponible verticalement, faisant de lui le conteneur principal.
- Alignement centré : justifyContent: "center" centre le contenu verticalement, tandis que alignItems: "center" centre le contenu horizontalement. Cela place tout contenu enfant (ici, le Text) au centre de l'écran

3) Texte affiché
- Un composant Text affiche le message : "Edit app/profil.tsx to edit this screen."
- Ce texte est un message de rappel pour les développeurs : il indique que ce fichier peut être modifié pour personnaliser l'affichage de la page "Profil".