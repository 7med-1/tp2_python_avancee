from lxml import etree

# Charger le fichier XML
tree = etree.parse("produits.xml")
root = tree.getroot()

#print les element de produits
produits = root.xpath("//produit[@categorie='électronique'][stock > 0]")

for p in produits:
    print(
        f"ID : {p.get('id')} | "
        f"Nom : {p.find('nom').text}"
    )
    
    
totaux = {}

# Parcourir tous les produits
for produit in root.xpath("//produit"):

    categorie = produit.get("categorie")

    prix = float(produit.find("prix").text)
    stock = int(produit.find("stock").text)

    valeur = prix * stock

    # Ajouter la valeur au total de la categorie
    if categorie not in totaux:
        totaux[categorie] = 0

    totaux[categorie] += valeur


print("\nValeur totale du stock par catégorie :")

for categorie, total in totaux.items():
    print(f"{categorie} : {total}")
    

#ajoute d'une nouveau produits
nouveau = etree.SubElement(
    root,
    "produit",
    id="P005",
    categorie="bureau"
)

# Sous-elements du produit
nom = etree.SubElement(nouveau, "nom")
nom.text = "Chaise"

prix = etree.SubElement(nouveau, "prix")
prix.text = "900"

stock = etree.SubElement(nouveau, "stock")
stock.text = "20"

#ecrire dans l'arbre xml
tree.write(
    "produits_modifie.xml",
    pretty_print=True,
    encoding="utf-8",
    xml_declaration=True
)

print("\nProduit P005 ajoute.")