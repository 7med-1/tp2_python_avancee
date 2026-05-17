import threading
import time

#class TacheAnalyse
class TacheAnalyse(threading.Thread):

    #constructeur
    def __init__(self, nom_fichier, nb_lignes):
        super().__init__()
        self.nom_fichier = nom_fichier
        self.nb_lignes = nb_lignes
        self.duree_reelle = 0

    #Methode executee automatiquement lors du demarrage du thread
    #Elle simule l’analyse d’un fichier par blocs de 1000 lignes 
    def run(self):

        debut = time.time()

        lignes_traitees = 0
        bloc = 1000

        print(f"Debut analyse : {self.nom_fichier}")

        while lignes_traitees < self.nb_lignes:

            time.sleep(0.5)

            lignes_traitees += bloc

            if lignes_traitees > self.nb_lignes:
                lignes_traitees = self.nb_lignes

            print(
                f"{self.nom_fichier} : "
                f"{lignes_traitees}/{self.nb_lignes} lignes traitees"
            )

        self.duree_reelle = time.time() - debut

        print(f"Fin analyse : {self.nom_fichier}")


#creation des 3 instances 
t1 = TacheAnalyse("fichier_A", 5000)
t2 = TacheAnalyse("fichier_B", 3000)
t3 = TacheAnalyse("fichier_C", 8000)

threads = [t1, t2, t3]

for t in threads:
    t.start()

for t in threads:
    t.join()

#affichage des resultat des threads
for t in threads:
    print(
        f"{t.nom_fichier} : "
        f"{t.duree_reelle:.2f} secondes"
    )