### Function ###

### Exo1 ###
def letter_by_letter(seq):
  # Function which writes 'seq' with space between every caracters.
  pos = 0
  print "letter_by_letter:"
  while pos<len(seq):
    # the ',' between the variables dell the '\n'.
    print seq[pos],
    pos+=1

def letter_by_line(seq):
  # Function which writes 'seq' with only one letter by line.
  pos = 0
  print "letter_by_line:"
  while pos<len(seq):
    print seq[pos]
    pos+=1

def one_line(seq):
  print "Your sequence is: " + seq

def exo1(seq):
  print "\n"
  one_line(seq)
  print ""
  letter_by_letter(seq)
  print "\n"
  letter_by_line(seq)
### End exo1 ###


### Exo2 ###
def nuc_and_pos(seq):
  pos = 0
  print "letter_by_letter:"
  while pos<len(seq):
    print seq[pos], pos
    pos+=1

def exo2(seq):
  print ""
  nuc_and_pos(seq)
### End exo2 ###


### Exo3 ###
def number_of_AA_soufre(seq):
  # Function which pritn the number of sulphur amino acid.
  pos, num_j= 0, 0
  while pos<len(seq):
    # or seq[i] in "mc"
    if ((seq[pos]=='C') | (seq[pos]=='M')):
      num_j+=1
    pos+=1

  return num_j

def exo3(seq):
  num_j=number_of_AA_soufre(seq)
  print "There is", num_j, "of AA soufre."
### End exo3 ###


### Exo4 ###
def AppaNucleotide(seq, nucleotide):
  pos=0
  freq=0
  while pos<len(seq):
    if seq[pos]==nucleotide:
      freq+=1
    pos+=1

  freq=float(freq)
  appar=freq/len(seq)

  return appar*100


def exo4(seq):
  print "Pourcentage de A =", round(AppaNucleotide(seq, 'A'), 3)
  print "Pourcentage de C =", round(AppaNucleotide(seq, 'C'), 3)
  print "Pourcentage de G =", round(AppaNucleotide(seq, 'G'), 3)
  print "Pourcentage de T =", round(AppaNucleotide(seq, 'T'), 3)
  Pourcentage_total = AppaNucleotide(seq, 'A')+AppaNucleotide(seq, 'C')+AppaNucleotide(seq, 'G')+AppaNucleotide(seq, 'T')
  print "Pourcentage total =", round(Pourcentage_total, 3)
  Pourcentage_other = 100-Pourcentage_total
  print "Pourcentage autre =", round(Pourcentage_other, 3)
### End exo4 ###


### Exo5 ###
def T_to_U(seq):
  # Function which switch 'T' for 'U'.
  pos=0
  new_seq = ""
  while pos<len(seq):
    # Add 'U' in 'new_seq' if the letter is an 'T'.
    if seq[pos]=='T':
      new_seq+='U'
    # Add the continuation of 'seq' if the lettre ins't 'T'
    else:
      new_seq+=seq[pos]
    pos+=1

  return new_seq

def nucA_to_nucB(seq, nucA, nucB):
  # Function switch 'nucA' for 'nucB'
  pos=0
  new_seq = ""
  while pos<len(seq):
    if seq[pos]==nucA:
      new_seq+=nucB
    else:
      new_seq+=seq[pos]
    pos+=1

  return new_seq

def exo5(seq):
  print "old seq =", seq.upper()
  print "new seq =", T_to_U(seq)
  print "new seq =", nucA_to_nucB(seq, 'T', 'U')
### End exo5 ###


### Exo6 ###
def exchange(nucA):
  # Function which exchange 'nucA' for the opposite.
  if nucA=='A':
    return 'T'
  elif nucA=='C':
    return 'G'
  elif nucA=='T':
    return 'A'
  else:
    return 'C'

def complementary_strand(seq):
  # Strand = brin
  # Function which found the complementary strand of 'seq'.
  pos=0
  seq_comp=""
  while pos<len(seq):
    # Add the opposite nucleotide.
    seq_comp+=exchange(seq[pos])
    pos+=1

  # With [::-1] we can inverse the str.
  seq_comp=seq_comp[::-1]
  return seq_comp

def exo6(seq):
  print "old seq =", seq.upper()
  print "complementary_strand =", complementary_strand(seq)
### End exo6 ###

### Exo7 ###
def found_adn(seq):
  # Function which found the errors in an adn seq.
  pos=0
  # Creat an empty table for save errors and their position.
  wrong=[]
  while pos<len(seq):
    # Save errors and their position.
    if not ((seq[pos]=='A') | (seq[pos]=='C') | (seq[pos]=='G') | (seq[pos]=='T')):
      wrong.append((seq[pos], pos+1))
    # Else save 0.
    else:
      wrong.append(0)
    pos+=1

  return wrong

def found_adn_2(seq):
  # Same that 'found_adn' but return 0 at the first erro else 1.
  pos=0
  while pos<len(seq):
    if not ((seq[pos]=='A') | (seq[pos]=='C') | (seq[pos]=='G') | (seq[pos]=='T')):
      return 0
    pos+=1

  return 1

def is_adn(liste):
  # Function which say if 'seq' is an adn seq.
  for i in range(len(liste)):
    # Test if haven't any error in the liste init with 'found_seq'.
    if(liste[i]!=0):
      return 0
  return 1

def exo7(seq):
  liste=found_adn(seq)
  print "is adn ?", is_adn(liste)
  print(liste)
  print "with found_adn_2, is adn ?", found_adn_2(seq)
### End Exo7 ##

### Exo8 ###
def is_palindrome(seq):
  new_seq=seq[::-1]
  # Inverse the 'seq'.
  if seq==new_seq:
    return 1

  return 0

def is_palindrome_biologique(seq):
  new_seq=complementary_strand(seq)
  if seq.upper()==new_seq:
    return 1

  return 0

def exo8(seq):
  print "is palindrome ?", is_palindrome(seq)
  print "is palindrome_biologique ?", is_palindrome_biologique(seq)
### End exo8 ###

### Menu ###
def choice(seq, num):
  seq=seq.upper()
  if num==1:
    print "Exercise 1:"
    exo1(seq)
  elif num==2:
    print "Exercise 2:"
    exo2(seq)
  elif num==3:
    print "Exercise 3:"
    exo3(seq)
  elif num==4:
    print "Exercise 4:"
    exo4(seq)
  elif num==5:
    print "Exercise 5:"
    exo5(seq)
  elif num==6:
    print "Exercise 6:"
    exo6(seq)
  elif num==7:
    print "Exercise 7:"
    exo7(seq)
  elif num==8:
    print "Exercise 8:"
    exo8(seq)
  else:
    print "number unknown."

def switcher_choice(seq, num):
  print "Exercise" + num
  seq=seq.upper()
  switcher = {
    1:exo1(seq),
    2:exo2(seq),
    3:exo3(seq),
    4:exo4(seq),
    5:exo5(seq),
    6:exo6(seq),
    7:exo7(seq),
    8:exo8(seq)
  }

  switcher.get(num, "Invalid exercise.")

def menu():
  seq=raw_input("Give me a sequence:\n")
  num=int(input("Give me the number of the execice:\n"))

  choice(seq, num)
## End menu ###

### Main ###
menu()
