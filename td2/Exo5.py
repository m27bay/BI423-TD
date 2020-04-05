#######################################################################
# Exercice 5 - if: ... else:                                          #
# Ecrire un programme permettant de savoir si un nombre entier saisi  #
# par l utilisateur est pair ou impair.                               #
#######################################################################

###########################################################################
# Exercice 6 - if: ... elif: ... else:                                    #
# Ecrire un programme permettant a un utilisateur de saisir un nombre et  #
# indiquant si ce nombre est positif, negatif ou egal a zero.             #
###########################################################################

def EstPair(data):
  LaVerite = 0
  if(data%2==0):
    LaVerite = 1

  return bool(LaVerite)


def Positif(data):
  LaVerite = 0
  if(data>0):
    LaVerite = 1

  return bool(LaVerite)

def Negatif(data):
  LaVerite = 0
  if(data<0):
    LaVerite = 1

  return bool(LaVerite)

def EgaleAZero(data):
  LaVerite = 0
  if(data==0):
    LaVerite = 1

  return bool(LaVerite)

### Main ###
data=int(input("Donnez moi un nombre entier: "))
print data, "est pair ?", EstPair(data)
print data, "est:\n\tPositif ?", Positif(data), "\n\tNegatif ?", Negatif(data), "\n\tEgale a zero ?", EgaleAZero(data)
