# Course

Tobi se promène tranquillement dans la forêt, quand, tout à coup, il trébuche et tombe à travers une faille.

Il se retrouve alors enfermé dans une grotte... Tobi, marchant à l'énergie solaire (école comme son créateur) doit alors sortir le plus vite possible de la grotte. Il doit alors trouver un chemin vers la sortie..

Input:
    N M les dimensions de la carte.
    N lignes avec la carte
Output:
    La longueur du chemin minimal de Tobi vers la sortie

Exemple:

```
$> cat sample1.txt
5 3
.T.
...
XX.
...
S.X
```

T représente Tobi.
S représente la sortie.
X représente les obstacles.

Tobi cherche alors le chemin le plus court vers la sortie.

```
$> cat sample1.txt | ./course
7
```

Dans cette carte, tobi passe par 7 positions différentes, les voici:
0 2
1 2
2 2
3 2
3 1
4 1
4 0