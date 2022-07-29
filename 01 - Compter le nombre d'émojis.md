# Exercices Docstring Mentorat

## [Compter le nombre d'émojis](https://www.docstring.fr/formations/exercices/1979/?tab=enonce)

### Énoncé

> Dans cet exercice, l'objectif est de récupérer le nombre d'émojis pour chaque émoji dans la chaîne de caractères `emojis`.
> 
> Vous devez récupérer ces informations dans le dictionnaire `emojis_count`.
> 
> Dans l'exemple de l'exercice, `emojis_count` doit donc être égal à :
> 
> {'🥳': 4, '🚀': 1, '😎': 1, '😍': 2}

#### Aide

> Pour compter le nombre d'éléments dans un **itérable**, on peut utiliser la méthode **`count`**.
> Pensez également à utiliser les **`sets`** 😉

### Pédagogie

> intéressant de détailler la réflexion -> "Je dois compter le nombre d'emojis : 
> - par quoi je commence
> - avec quoi je travaille
> - quelles notions vont m'aider ?
> 
> => Faire l'algorithme en français avant de passer au code.

### Analyse de l'énoncé

- récupérer le **nombre** (d'émojis) pour chaque (émoji) dans la **chaîne de caractères** (emojis).
- (Vous devez) récupérer (ces informations) dans **le dictionnaire** (emojis_count).
- Dans l'**exemple** de l'exercice, (emojis_count) doit (donc) être égal à : **{'🥳': 4, '🚀': 1, '😎': 1, '😍': 2}**


### Documentations

- [list.count(x)](https://docs.python.org/fr/3/tutorial/datastructures.html)
- [5.4. Ensembles (sets)](https://docs.python.org/fr/3/tutorial/datastructures.html#sets)
- [class collections.Counter([iterable-or-mapping])](https://docs.python.org/fr/3/library/collections.html#collections.Counter): La classe Counter est une **sous-classe de dict** qui permet le **dénombrement** d'**objets hachables**.
- [Objets defaultdict](https://docs.python.org/fr/3/library/collections.html#defaultdict-objects): Renvoie un nouvel objet qui se comporte comme un **dictionnaire**.
