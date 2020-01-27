#Je vais essayer de faire d'abord une liste de tous les numéros d'identification, sans l'url devant

# url = list(range(20000,30151))
# print(url)

# Réussi ! 
# Je metrai tous mes essais en commentaire 

# url = list(range("https://montrealcampus.ca?p=20000","https://montrealcampus.ca?p=30151"))
# print(url)

# Nope, ça ne marche pas. Deuxième essai 

# url = "https://montrealcampus.ca?p=" + list(range(20000,30151))
# print(url)

# Non plus, voilà ce que ça me dit : "TypeError: can only concatenate str (not "list") to str". 
# J'en déduis que je ne peux pas mélanger du texte et des chiffres dans une étendue de nombre. Troisième essai : 

# url1 = "https://montrealcampus.ca?p="
# url2 = list(range(20000,30151))
# url3 = url1 + url2
# print(url3)

# Cela me dit la même chôse. Quatrième essai : 

# url = list(range(20000,30151))
# print("https://montrealcampus.ca?p=",url)

# Cela fait quelque chose d'intéressant, mais l'url n'apparait qu'une fois au début pas devant chaque nombre, donc cela ne va pas. 

# url = list(range(20000,30151))
# print("https://montrealcampus.ca?p=" + url)

# Cela ne marche pas, même type d'erreur que plus haut. Même en enlevant les espaces entre le + dans le doute. 

# url = list(range(20000,30151))
# print(url)
# print(len(url))

# Au moins, j'ai le bon nombre de chiffres dans mon étendue de nombre. Mais je dois encore trouver comment 
# ajouter l'url devant les chiffres. Je vais essayer de créer une boucle. Je n'avais pas réussi, mais après 
# être venue vous voir pour que vous m'expliquiez, voici le résulat : 

nombres = list(range(20000,30151))
url = "https://montrealcampus.ca?p="

liste = []

for nombre in nombres:
    print(url+str(nombre))
    liste.append(url+str(nombre))
    
print(liste)
print(len(liste))
