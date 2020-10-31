def b(n):               # on définit b(n) d'après la question C
    r = (2*n**3+n)/3
    return r

n = 0                   
while b(n)<= 2000:      # on calcule le nombre de briques utilisées pour chaque valeur de n 
    n+=1                # et verifie que ce nombre est bien inférieur à 2000, et on incrémente n de 1 si c'est le cas.

n-=1                    # on soustrait 1 de n car le while s'arrête quand b(n) est au dessus de la barre des 2000 briques.
print(n, b(n)) 