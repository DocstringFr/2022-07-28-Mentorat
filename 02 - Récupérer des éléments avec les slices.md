# Exercices Docstring Mentorat

## [Récupérer des éléments avec les slices](https://www.docstring.fr/formations/exercices/921/?previous=difficulty%3D1&tab=enonce)

### Énoncé

> Dans cet exercice, vous devez récupérer différents morceaux d'une liste.
>
> La liste de départ est la suivante :
> 
> `liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]`
> 
>L'objectif de cet exercice est de récupérer les informations suivantes grâce aux slices :
>
> - Les **trois premiers employés** (`"Maxime"`, `"Martine"` et `"Christopher"`) dans une liste `trois_premiers`.
> - Les **trois derniers employés** (`"Carlos"`, `"Michael"` et `"Éric"`) dans une liste `trois_derniers`.
> - Tous les employés **sauf** le premier et le dernier dans une liste `milieu`.
> - Le **premier** et le **dernier** employé dans une liste `premier_dernier`.

#### Aide

> Pensez au fait que vous pouvez parcourir une liste en sens inverse avec des indices négatifs.

### Pédagogie

> revenir sur la notion de `slice` et comment elle fonctionne (et pourquoi on pourrait en avoir besoin)

### Analyse de l'énoncé

- l'énoncé est assez explicite avec des indications en gras, couleurs pour marquer les éléments important
- Tout cet excercise se base sur la compréhension et bonne utilisation de l'outil `slice` python sur les `list`


### Documentations

- [class slice(stop) - class slice(start, stop[, step])](https://docs.python.org/fr/3/library/functions.html#slice) (ps: cette partie de la documentation n'est pas traduite en 🇫🇷Français🇫🇷, ça pourrait être 💡un bon apport💡 dans la documentation/opensource de faire cette traduction et la proposer ^^)
- [itertools.islice(iterable, stop) - itertools.islice(iterable, start, stop[, step])](https://docs.python.org/fr/3/library/itertools.html#itertools.islice): Crée un **itérateur** qui renvoie les **élément sélectionnés de l'itérable**. (ps: il y a une ❌faute❌ d'orthographe dans cette traduction :p)
- [Glossaire - tranche](https://docs.python.org/fr/3/glossary.html#term-slice): (slice en anglais), un objet contenant habituellement une portion de séquence.
