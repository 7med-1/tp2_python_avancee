import time
import threading

fichiers = [
    ("rapport.pdf", 2),
    ("image.png", 1),
    ("video.mp4", 4),
    ("archive.zip", 3),
    ("data.csv", 1.5),
]

#fonction tetecharger qui prendre une duree et un nom
def telecharger(nom, duree):
    print(f"Début du téléchargement : {nom}")
    time.sleep(duree)
    print(f"Fin du téléchargement : {nom}")

#debut de tem de l'execution pour le calculer a la fin
debut_seq = time.time()

#une loop pour faire le travail sequenciel
for nom, duree in fichiers:
    telecharger(nom, duree)
#fin du temps
fin_seq = time.time()

#resultat de l'execution
print(f"Temps total séquentiel : {fin_seq - debut_seq:.2f} secondes")

threads = []

#temps thread
debut_threads = time.time()

#creation des threads 
for nom, duree in fichiers:
    t = threading.Thread(target=telecharger, args=(nom, duree))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

fin_threads = time.time()

#calcule de resultat et affichage
print(f"Temps total avec threads : {fin_threads - debut_threads:.2f} secondes")
