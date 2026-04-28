# Notes pour la présentation

Ces notes doivent contenir le discours que je porterais pendant le séminaire. Je dois partager les concepts abordés de la plus simple des manières.

## Objectifs de la présentation

Le grand public à tendance à penser qu'un modèle d'intelligence artificielle est capable de comprendre. Il est important de faire la distinction entre le cerveau humain et le moteur mathématique dont dispose les modèles qui ne sert qu'à prédire le prochain mot. En apprenant à le faire correctement ce moteur apprend aussi beaucoup de choses sur la langue et le monde.

## Intro

Modèle = **Intelligence** artificielle mais ils ne comprennent pas.

### Pour Intelligent

- Produir du contenu utile en prenant en compte le contexte donné.

- Traduire du texte donnée (principal objectif de l'ia au début)

- Raisonner (chain of thought)

### Contre Intelligent

- Expérience subjective

- Conscience

- Compréhension

En science: Intelligent, en philosophie: pas intelligents car compréhension à déterminer.

Pour pouvoir répondre à cette question il faut savoir comment ces modèles fonctionnent. Cette présentation a pour but de vous donner les bases de l'apprentissage machine.

## Word2Vec

Avant de parler ou d'associer les mots, l'IA doit apprendre la langue.

### Pre-training

Pour apprendre, l'IA doit repérer quels mots apparaissent dans des contextes similaires. On lui fait lire d'énormes quantités de documents. La source principale est internet avec des sites comme wikipédia. 

Après avoir lu assez d'articles, elle remarque que le mot chat est utilisé dans des contextes similaires avec chien ou lapin. Elle apprend que boire est souvent utilisé avec ces animaux. Elle voit que le mot lait, qui est une boisson est utilisé avec chat. Le modèle finit par apprendre à utiliser ces mots ensembles. Il reconnait les patterns. L'IA ne sait pas ce qu'est un chat mais elle sait très bien comment parler des chats.

Ce processus dure plusieurs mois, requiert des milliers d'ordinateurs surpuissant pour traiter les documents et consomme énormément d'énergie. 

### Embedding

Les ordinateurs ne peuvent pas comprendre les mots écrits avec des lettres. Il faut les traduire dans une langue mathématique. Mais comment donner du sens à un nombre ?

L'idée géniale derrière les Intelligences Artificielles, c'est **la méthode de placement spatial**. L'explication tient en une phrase : *"On reconnaît un mot à ses fréquentations"*.

Pour commencer, les mots sont traduis en nombre qui correspondent au mot entier ou à une partie du mot. Ces nombres n'ont pas de sens et ne servent que d'identificateur. Ils sont appelés tokens.

Au tout début de sa vie, l'IA ne connaît aucun mot. Elle prend tout le dictionnaire sous forme de token et les jette parfaitement au hasard dans un immense espace mathématique. Au début, le mot "chaussette" peut très bien se retrouver à côté de "galaxie".

L'IA commence à lire Wikipedia. À chaque fois qu'elle croise une phrase, comme *"Le chat boit du lait"*, elle regarde les mots qui composent cette phrase. Elle agit alors comme une sorte d'aimant ou de gravité. Elle **tire** mathématiquement les mots "chat", "boit" et "lait" pour les rapprocher légèrement les uns des autres sur sa carte. Et elle repousse les mots qui n'ont rien à voir.

Après avoir lu des milliards de phrases pendant des mois, la carte s'est organisée toute seule ! Tous les animaux ont été tellement tirés ensemble par les verbes d'action qu'ils finissent par former une ville sur la carte. 

L'IA n'a aucun dictionnaire interne avec des définitions. Pour elle, la seule définition du mot "chat", c'est la liste de ses coordonnées GPS sur cette immense carte. Un mot n'a de sens que grâce aux mots qui l'entourent. Elle se contente de calculer des distances entre les villes sur sa carte ! 

La représentation de ces mots nous permet de faire des calculs comme avec des nombres.
