import matplotlib.pyplot as plt
import statistics

#donnees d'entrer
A = [120, 135, 98, 150, 160, 175]
B = [80, 90, 110, 105, 130, 145]
C = [200, 185, 170, 190, 160, 210]

mois = [1, 2, 3, 4, 5, 6]

#plot des trois courbes de ventes
plt.plot(mois, A, "b-o", linewidth=2, label="Produit A")
plt.plot(mois, B, "g--s", linewidth=2.5, label="Produit B")
plt.plot(mois, C, "r-^", linewidth=3, label="Produit C")

#limiter x entre 0 et 7 , y entre 50 et 250 
plt.xlim(0, 7)
plt.ylim(50, 250)

#titre est lable de chaque axe et du graphe
plt.title("Ventes mensuelles des produits")
plt.xlabel("Mois")
plt.ylabel("Ventes")
plt.legend(loc='upper left')

plt.grid(True)
plt.show()

#clalcule de l'ecart-type (standerd diveiation)
ecart_A = statistics.stdev(A)
ecart_B = statistics.stdev(B)
ecart_C = statistics.stdev(C)

#presentation des resultat
print("Écart-type du produit A :", round(ecart_A, 2))
print("Écart-type du produit B :", round(ecart_B, 2))
print("Écart-type du produit C :", round(ecart_C, 2))

#interpretation
print("\nLe produit le plus stable est le produit C.")
print("Justification : il possede l'ecart-type le plus faible,")
print("donc ses ventes varient moins d'un mois a l'autre.")



# | Critère                       | cx_Freeze                                                                                | PyInstaller                                                                                    |
# | ----------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
# | Facilité d'utilisation        | Moins simple, nécessite souvent un fichier de configuration `setup.py`                   | Très simple, une seule commande suffit                                                         |
# | Taille de l'exécutable        | Peut générer un dossier contenant plusieurs fichiers                                     | Le fichier `.exe` peut être assez lourd, surtout avec Matplotlib                               |
# | Option fichier unique         | Non, il génère généralement un dossier                                                   | Oui, avec l’option `--onefile`                                                                 |
# | Compatibilité multiplateforme | Compatible Windows, Linux et macOS, mais il faut générer l’exécutable sur chaque système | Compatible Windows, Linux et macOS, mais il faut aussi générer l’exécutable sur chaque système |
# | Votre recommandation          | Utile pour des projets plus structurés                                                   | Recommandé pour cet exercice car il est simple et rapide                                       |


