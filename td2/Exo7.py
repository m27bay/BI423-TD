###########################################################################
# Exercice 7 - Extraction d une partie d une chaine                       #
#                                                                         #
# 7.1. Ecrire un programme permettant a un utilisateur de saisir une      #
# chaine ainsi que d extraire de cette chaine les n premiers caracteres   #
# (encore une fois la valeur de n doit etre saisie par l utilisateur),    #
#                                                                         #
# 7.2. Ecrire un programme permettant a un utilisateur de saisir une      #
# chaine ainsi que d extraire de cette chaine les n derniers caracteres   #
# de la chaine saisie (via la saisie de n par l utilisateur)              #
#                                                                         #
# 7.3. En utilisant les exercices precedents ecrire un programme donnant  #
# le choix a l utilisateur de traiter un des deux cas precedents.         #
# On utilisera dans ce cas une instruction du type "if: ... elif: ...else:#
###########################################################################

def SousChaineDeb(string, lenght):
  return string[:lenght]


def SousChaineFin(string, lenght):
  sizeStr = len(string)
  deb = sizeStr - lenght
  return string[deb: sizeStr]


def SousChaineChoix(string, lenght):
  print "SousChaineDeb = choice 1---SousChaineFin = choie 2"
  choice = int(input("Donnez votre choix ? "))

  if(choice==1):
    return SousChaineDeb(string, lenght)

  elif(choice==2):
    return SousChaineFin(string, lenght)

  else:
    return


### Main ###
Str = raw_input("Donnez moi une chaine de caracteres: ")
data=int(input("Donnez moi un nombre entier: "))

print "\ncdSousChaineDeb = ", SousChaineDeb(Str, data)
print "SousChaineFin = ", SousChaineFin(Str, data)

print "\nSousChaineChoix:", SousChaineChoix(Str, data)
