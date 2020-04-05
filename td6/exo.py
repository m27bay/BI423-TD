from old_td import T_to_U, complementary_strand

### Exercise 1 ###
def exo1():
  recuperate_first_line()

def recuperate_first_line():
  file_name=raw_input("Give me the name of the file (with .txt):\n")

  file=open(file_name, "r")

  # readline s'arrete au \n
  print "This is the line: ", file.readline()
  file.close()

def exo1_bis():
  recuperate_first_line_bis()

def recuperate_first_line_bis():
  file_name=raw_input("Give me the name of the file (with .txt):\n")

  file=open(file_name, "r")

  read=file.readline()
  buf=""
  while(read!=""):
    buf+=read[:len(read)-1]
    read=file.readline()

  print "This is the line: ", buf
  file.close()
### End exercise 1 ###


### Exercise 3 ###
def exo3():
  char=raw_input("Give me a char (in majuscule):\n")
  char=char.upper()
  pourc=pourc_de_char(char)


def nbr_char_in_file():
  file_name=raw_input("Give me the name of the file (with .txt):\n")
  file=open(file_name, "r")

  read=file.readline()
  buf=""
  som=0
  while(read!=""):
    buf+=read[:len(read)-1]
    som+=len(read)-1
    read=file.readline()

  print "There is", som, "char in", file_name
  file.close()
  return som

def save(string, length, pourc, char):
  file_name=raw_input("Name file save ?\n")
  file_name+=".txt"
  file=open(file_name, "w")

  file.write("The string is: " + str(string) + "\n")
  file.write("Her size is: " + str(length) + "\n")
  file.write("She haves " + str(pourc) + " of char: " + str(char) + "\n")

def pourc_de_char(char):
  file_name=raw_input("Give me the name of the file (with .txt):\n")
  file=open(file_name, "r")

  read=file.readline()
  buf=""
  freq=0
  while(read!=""):
    buf+=read[:len(read)-1]
    read=file.readline()

  file.close()
  buf=buf.upper()

  freq=buf.count(char)
  freq=float(freq)
  size=len(buf)
  pourc=freq/size

  save(buf, size, pourc*100, char)

  return pourc*100
### End exercise 3 ###

### Execise 4 ###
def exo4():
  while 1:
    choice=int(input("\n\nWhat to you want to do ?\nchoice 0: quit\nchoice 1: sequence transcrit\nchoice 2: sequence complementary strand:\n"))
    if(choice==0):
      break
    seq=raw_input("Give me a sequence:\n")
    seq=seq.upper()
    if choice==1:
      save(T_to_U(seq), 0, 0, '')
    elif choice==2:
      save(complementary_strand(seq), 0, 0, '')
### End exercise 4 ###

### Exercise 5 ###
def exo5():
  file_name=raw_input("Give me the name of the file (without .txt):\n")
  file_name+=".txt"

  file=open(file_name, "r")
  print with_find(file)
  file.close()

def with_find(file):
  read=file.readline()
  motif=raw_input("Give me a motif:\n")

  pos, count = 0, 0
  pos+=read.find(motif, pos)
  count+=1

  return count, pos

# def without_find(file_name):

### End exercise 5

### Menu ###
def choice(num_exo):
  if num_exo==1:
    print "Exercise 1:"
    exo1()
  elif num_exo==2:
    print "Exercise 1 bis:"
    exo1_bis()
  elif num_exo==3:
    print "Exercise 3"
    exo3()
  elif num_exo==4:
    print "Exercise 4"
    exo4()
  elif num_exo==5:
    print "Exercise 5"
    exo5()
  else:
    print "number unknown."

def menu():
  num_exo=(int(input("Give me the number of the exercise:\n")))
  choice(num_exo)

### End menu ###

### Main ###
menu()
