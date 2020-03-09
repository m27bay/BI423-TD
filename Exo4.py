###########################################################################
# Exercice 4 if:                                                          #
# Ecrire un programme permettant a un utilisateur de saisir deux chaines  #
# caracteres et de savoir si la seconde est contenue dans la premiere.    #
# On fera deux versions de ce programme :                                 #
# l une avec count, l autre avec in.                                      #
###########################################################################

def PremiereVersion(chaine1, chaine2):
  LaVerite = 0
  if(chaine1.count(chaine2)<=1):
    LaVerite = 1

  return bool(LaVerite)


def DeuxiemeVersion(chaine1, chaine2):
  LaVerite = chaine2 in chaine1

  return LaVerite


### Main ###
str1 = raw_input("Donnez moi une chaine de caracteres: ")
str2 = raw_input("Donnez moi une deuxieme de caracteres: ")

print "Voici la premiere chaine", str1
print "Voici la deuxieme chaine", str2

print "PremiereVersion:", PremiereVersion(str1, str2)
print "DeuxiemeVersion:", DeuxiemeVersion(str1, str2)
