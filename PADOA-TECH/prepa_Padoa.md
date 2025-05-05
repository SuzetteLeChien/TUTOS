# Trucs a connaitre:
## JavaScript:
A programming language that runs in web browsers. It allows websites to be interactive rather than just static pages. JavaScript is what makes things happen when you click buttons, fill out forms, or see content update without refreshing the page.

[Javascript en 100 secondes](https://www.youtube.com/watch?v=DHjqpvDnNGE)

Pour plus pousser: [W3School](https://www.w3schools.com/js/)
## TypeScript
JavaScript with added type checking. It's like JavaScript that checks your work before you run it, helping catch errors early. TypeScript code gets converted to JavaScript before running.

[Typescript en 100 secondes](https://www.youtube.com/watch?v=zQnBQ4tB3ZA)

Pour plus pousser: [W3School](https://www.w3schools.com/typescript/index.php)

## Node JS
A way to run JavaScript outside of web browsers. Before Node.js, JavaScript could only run in browsers, but Node.js lets developers use JavaScript to build backend servers, command-line tools, and other applications that run on computers rather than in browsers.

[Tuto NodeJS en 15 minutes](https://www.youtube.com/watch?v=ENrzD9HAZK4&t=2s)

Pour plus pousser: [W3School](https://www.w3schools.com/nodejs/default.asp)

NodeJS est ce que l'on appel un runtime:

**Runtime:** An environment that provides the necessary components to execute code in a specific programming language. A runtime includes:

The interpreter or virtual machine that executes the code
Core libraries and functions available to the language
Memory management systems
Input/output operations handling

Think of a runtime as the "engine" that powers your code. For example, Node.js provides a JavaScript runtime outside browsers by incorporating the V8 JavaScript engine (originally built for Chrome) along with additional modules for file system access, networking, and other server-side capabilities.

**Problème:** Je sais pas quelle framework ils utilisent pour le backend

## Angular

Angular is a comprehensive front-end framework maintained by Google that uses TypeScript to build single-page applications. Here's what makes it distinctive:
Core Angular Features
- Component-Based Architecture: Everything in Angular is built as components—reusable, self-contained pieces of UI with their own logic and styling.
- Two-Way Data Binding: Angular allows data to flow both ways between components and the UI, automatically keeping them in sync.
Dependency Injection: Angular has a built-in system that makes it easier to provide components with the services and resources they need.
- TypeScript Integration: Angular is built with TypeScript, providing strong typing and better tooling support.
- Complete Solution: Angular includes routing, forms handling, HTTP client, testing utilities, and animation support out of the box.

How Angular Differs from Other Frameworks when compared to other popular frameworks like React or Vue:

- Opinionated vs. Flexible: Angular is more opinionated and prescriptive about how applications should be structured. React and Vue are more flexible libraries that let developers make more architectural decisions.
Size and Learning Curve: Angular is larger and has a steeper learning curve, but provides more built-in functionality. React is smaller and more focused on UI rendering.
- Language Approach: Angular strongly favors TypeScript, while React and Vue work with either plain JavaScript or TypeScript as an option.
Template System: Angular uses HTML templates with special directives, while React uses JSX (JavaScript XML) and Vue offers a template syntax that's closer to standard HTML.
- State Management: Angular includes services and RxJS for state management, while React often requires external libraries like Redux.
Corporate Backing: Angular has strong Google support and follows a more regular, predictable release schedule with clear upgrade paths.

Angular excels in large enterprise applications where its comprehensive structure, TypeScript integration, and robust tooling provide significant advantages for maintaining complex codebases with multiple developers.

[Angular en 100 secondes](https://www.youtube.com/watch?v=Ata9cSC2WpM)

Pour plus pousser: [W3School](https://www.w3schools.com/angular/default.asp)

## PostgreSQL
A powerful, open-source relational database system. It stores data in tables that can relate to each other and is known for reliability, feature richness, and standards compliance. PostgreSQL is often used for applications that need complex queries, data integrity, and scalability.

[PostgreSQL en 100 secondes](https://www.youtube.com/watch?v=n2Fluyr3lbc)

Pour plus pousser: [W3School](https://www.w3schools.com/postgresql/index.php)

## Autres concepts a connaitres
- Un CLI (Command Line Interface) est une interface utilisateur en ligne de commande qui permet à l'utilisateur d'interagir avec un programme en utilisant des commandes textuelles. Les commandes sont exécutées immédiatement. Les CLIs sont souvent utilisés pour effectuer des tâches de gestion de système, de développement de logiciels et de traitement de données. Dans angular par exemple elle permet de créer des nouveaux composants
- [Testing en 100 secondes](https://www.youtube.com/watch?v=u6QfIXgjwGQ&t=93s). A savoir que a Padoa on utilise les actions github et un outil appeler CircleCI pour run les test E2E et d'intégration
- [Redis en 100 secondes](https://www.youtube.com/watch?v=G1rOthIU-uo). Utiliser pour la gestions des taches a réaliser. Faut voire ca comme une BDD qui est utiliser pour stocker et accéder rapidement des données simple (key=>value)
- [Docker en 100 secondes](https://www.youtube.com/watch?v=Gjnup-PuquQ). Ca vas être nécessaire car ce que tu fait ca vas être builde vers une image docker qui seras deployer par kubernetes
- [Kubernetes en 100 secondes](https://www.youtube.com/watch?v=PziYflu8cB8). Juste bon a comprendre ca prends moins de 2 minutes