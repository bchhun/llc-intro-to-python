# -*- coding: utf-8 -*-

# Rappelez-vous, nous avons besoin d'une chaîne de caractère pour la fonction
# raw_input, mais vous devez le convertir en integer pour la comparaison mathématique
weather = int(input("Quelle est la température en ce moment-même ? (saisissez un chiffre svp): "))

# si la température est plus grande ou égale à 25 degrés
if weather >= 25:
    print("Allons à la plage !")
# la température est plus petite que 25 degrés MAIS plus grande que 15 degrés
elif weather < 25 and weather > 15:
    print("Allons prendre une bonne crème glacée !")
else:
    print("Portez votre gilet chaud préféré et révez à la plage")
