#########################################################################
# Exercice 1 - input                                                    #
# Faire un programme permettant de calculer l aire d'un rectangle etant #
# donnees sa largeur et sa longueur,                                    #
# ces deux dernieres valeurs etant entrees par l utilisateur sur la     #
# ligne de commande en utilisant ici l instruction input.               #
#########################################################################

def AirRectangle(longueur, largeur):
  aire=longueur*largeur
  return aire

### Main ####
longueur=int(input("Donnez moi la longueur de votre rectangle: "))
largeur=int(input("Donnez moi la largeur de votre rectangle: "))

aire=AirRectangle(longueur, largeur)

print "Voici l aire de votre rectangle", aire
