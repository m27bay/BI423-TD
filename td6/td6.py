##############################################################
######################### outil(s) ###########################
##############################################################

def max_3(start, a, b, c):
  if a < b and a < c and a > start+3:
    return a
  elif b < a and b < c and b > start+3:
    return b
  else:
    return c

def read_in_file():
  name_file = raw_input("Name file (with .txt)?\n")

  open_mode = "r";
  file = open(name_file, open_mode);

  # skip the first line on the file
  file.readline()

  # return the rest of the file
  sequence = (file.readline()).lower()
  file.close()
  return sequence

##############################################################
######################## function(s) #########################
##############################################################

def found_cds():
  sequence = read_in_file();
  codon_start = "atg"
  pos_start = 0

  # list of codon stop
  codon_stop = ["taa", "tga", "tag"]
  pos_end = 0

  pos_start = sequence.find(codon_start)

  pos1 = sequence.find(codon_stop[0])
  pos2 = sequence.find(codon_stop[1])
  pos3 = sequence.find(codon_stop[2])

  pos_end = max_3(pos_start, pos1, pos2, pos3)

  lenght = len(sequence[pos_start: pos_end+3])
  print "start at", pos_start, "end at:", pos_end, "lenght:", lenght

  return sequence[pos_start: pos_end+3]

##############################################################
###########################  main  ###########################
##############################################################

def main():
  print found_cds()

##############################################################

main()


# mini = input("taille mini")
# stop = "TGA/TAA/TAG"
# i = 0
# start = -1
# while i < len(seq)-2:
#   if start < 0 and seq[i:i+3] = "ATG"
#     start = i
#   elif start >= 0 and seq[i:i+3] in stop
#     if i+3 - start >= mini
#       file.write("+...")
#       start = -1
#   i = i + 3
