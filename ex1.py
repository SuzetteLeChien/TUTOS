# Exercice 1
from math import pi
with open("poème.txt","r",encoding="utf-8") as f:
    contenu=f.read()
    ponctuation=["'","!",",","?",".",]
    for caractere in contenu:
        if caractere in ponctuation:
            contenu=contenu.replace(caractere,"")

    liste_mots=contenu.split()
    pi_calcule=0
    for i in range (len(liste_mots)):
        pi_calcule+=(len(liste_mots[i])*(10**(-i)))
    print(pi_calcule)
    pi_theorique=str(pi[:17])
    print(pi_theorique)
    print(pi_calcule==float(pi_theorique))
    f.close()

with open("pi.txt","w",encoding="utf-8") as f:
    f.write(str(pi_calcule))
    f.close()
