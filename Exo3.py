###########################################################################
# Exercice 3 raw_input et revisions sur les chaines de caracteres         #
# Ecrire un programme permettant a un utilisateur de saisir une sequence  #
# nucleotidique et d afficher :                                           #
# - le pourcentage en A, en T, en G et en C,                              #
# - ainsi que le pourcentage de caracteres qui ne font pas partie de      #
# l alphabet nucleotidique                                                #
# (qui correspondent soit a des erreurs de saisie, soit a des             #
# indeterminations apres sequencage).                                     #
# On fera en sorte que le programme fonctionne quelque-soit la casse      #
# utilisee pour saisir a, t, g, ou c                                      #
# (la casse correspond a la facon dont les mots sont ecrits :             #
# majuscule ou minuscule).                                                #
###########################################################################

def ApparitionNucleotide(sequence, nucleotide):
  frequence = float(sequence.count(nucleotide))
  apparition = frequence/len(sequence)
  return apparition*100

seq = raw_input("Donnez moi une sequence nucleotidique: ")
print "Voici la premiere chaine", seq, "et voici ca longueur", len(seq)

# On met tout en majuscule
seq = seq.upper()

# On arrondi avec la fonction round(, chiffre apres la virgule)
pourcentageA = round(ApparitionNucleotide(seq, 'A'), 3)
pourcentageT = round(ApparitionNucleotide(seq, 'T'), 3)
pourcentageG = round(ApparitionNucleotide(seq, 'G'), 3)
pourcentageC = round(ApparitionNucleotide(seq, 'C'), 3)

print "PourcentageA = ", pourcentageA, "%"
print "PourcentageT = ", pourcentageT, "%"
print "PourcentageG = ", pourcentageG, "%"
print "PourcentageC = ", pourcentageT, "%"

sumPourcentage = pourcentageA + pourcentageT + pourcentageG + pourcentageC
pourcentageAutre = 100 - sumPourcentage
print "En tout = ", sumPourcentage, "%"
print "Pourcentage autre = ", pourcentageAutre, "%"
