# Rect

Dans ce problème, nous avons une surface de N * M cases. Les '.' désignent des espaces vides et les '*' désignent des espaces occupés. On vous demande de calculer la longueur du plan grand carré inscrit dans la surface. Un carré est correct lorque sa surface ne prend que des espaces libres.

Input:
    N M : 2 entiers désignant le nombres de lignes et le nombres de charactères dans une ligne
    N lignes suivantes une chaîne de charactères composés de '.' et de '*'
Ouput:
    La longueur du plus grand carré

Exemples:

```
$> cat sample1.txt
3 3
*.*
...
*..
$> cat sample1.txt | ./rect
2
$> cat sample2.txt
6 5
*....*
.....*
....**
..*...
.....*
$> cat sample2.txt | ./rect
3
```
