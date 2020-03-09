#########################################################################
# Exercice 2 raw_input                                                  #
# Faire un programme permettant a un utilisateur de saisir deux chaines #
# de caracteres utilisant maintenant l instruction raw_input et         #
# affichant a l ecran :                                                 #
# - la premiere chaine et sa longueur,                                  #
# - la seconde chaine et sa longueur,                                   #
# - le nombre de fois ou la seconde chaine apparait dans la premiere.   #
#########################################################################

str1 = raw_input("Donnez moi une chaine de caracteres: ")
str2 = raw_input("Donnez moi une deuxieme de caracteres: ")

print "Voici la premiere chaine", str1, "et voici ca longueur", len(str1)
print "Voici la deuxieme chaine", str2, "et voici ca longueur", len(str2)

# str1.count(str2) permet de connaitre le nombre d'apparition de
# str1 dans str2
print "Nombre d apparation de", str2, "dans", str1, "est", str1.count(str2)
