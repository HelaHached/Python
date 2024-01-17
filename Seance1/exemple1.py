# variable de type str 
nom= "ali"
# variable de type float 
Salaire= 1200.756
# variable de type int 
Age = 35
# variable etat sociale : boolean
celibataire=True

# On appele fonction print
print(nom)

print(Salaire)

print(Age)


# Appel des informations avec une seule fonction

print("l'employé est :", nom, "son age :", Age,"ayant le salaire :", Salaire)


# Appel des informations avec une seule fonction et modification du separateur et de l'element final
#print("l'employé est :", nom, "son age :", Age,"ayant le sallaire :", Salaire,
#      sep='*', end=';')

print("l'employé est :", nom, "son age :", Age,"ayant le salaire :", Salaire,
      sep='*')

# lire à partir du clavier

nom= input("entrez votre nom:")
age= input("entrez votre age:")
salaire= input("entrez votre salaire:")
print("l'employé est :", nom, "son age :", age,"ayant le salaire :", salaire)
