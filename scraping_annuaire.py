from bs4 import BeautifulSoup

html_doc = """
<html><head><title>Annuaire Etudiants</title></head><body>
 <h1>Promotion 2025-2026</h1>
 <table id="etudiants">
 <thead><tr><th>Nom</th><th>Filiere</th><th>Note</th></tr></thead>
 <tbody>
 <tr class="etudiant"><td>Amina
Benali</td><td>Informatique</td><td>16.5</td></tr>
 <tr class="etudiant"><td>Youssef El
Idrissi</td><td>Mathematiques</td><td>14.0</td></tr>
 <tr class="etudiant"><td>Sara
Moussaoui</td><td>Informatique</td><td>18.2</td></tr>
 <tr class="etudiant"><td>Karim
Tazi</td><td>Physique</td><td>12.5</td></tr>
 <tr class="etudiant"><td>Nadia
Ouahbi</td><td>Informatique</td><td>15.8</td></tr>
 </tbody>
 </table>
 <div class="annonces">
 <p class="urgent">Examen de rattrapage : 15 juin</p>
 <p>Remise des notes : 30 juin</p>
 <p class="urgent">Réunion pédagogique : 10 juin</p>
 </div>
</body></html>"""


#html parser
soup = BeautifulSoup(html_doc, "html.parser")

# Afficher le titre
print("Titre :", soup.title.text)

# Afficher le texte du h1
print("H1 :", soup.h1.text)


#extraction des donnees des etudiants avec find all
etudiants = soup.find_all(class_="etudiant")

print("\nListe des etudiants :")

for e in etudiants:

    nom = e.find(class_="nom").text
    filiere = e.find(class_="filiere").text
    note = float(e.find(class_="note").text)

    print(f"Nom : {nom} | Filière : {filiere} | Note : {note}")



#la recherche de toute les etudiants de l'informatique avrc une note sup a 15 pour calculer leur moy 
notes_info = []

print("\nEtudiants Informatique avec note > 15 :")

for e in etudiants:

    nom = e.find(class_="nom").text
    filiere = e.find(class_="filiere").text
    note = float(e.find(class_="note").text)

    if filiere == "Informatique" and note > 15:
        print(f"{nom} : {note}")
        notes_info.append(note)

# Calcul de la moyenne
moyenne = sum(notes_info) / len(notes_info)

print("Moyenne :", moyenne)

#selection de css
urgents = soup.select("p.urgent")

print("\nMessages urgents :")

for p in urgents:
    print(p.text)


#remoplacemnt des balise
for p in urgents:

    # Créer une nouvelle balise <strong>
    nouveau = soup.new_tag("strong")

    # Copier le texte
    nouveau.string = p.text

    # Remplacer <p> par <strong>
    p.replace_with(nouveau)

#le code html/css est modifer avec success
print("\nHTML modifie :")
print(soup.prettify())