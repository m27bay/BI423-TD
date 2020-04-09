import matplotlib.pyplot as plt

#######################################################################
############### Read and init the sequences with files ################
#######################################################################

def read_seq( name_file ):

  ## Open, option read
  file_fasta = open( name_file, "r" )

  ## Read the first line with data sequence
  line = file_fasta.readline()

  ## Cut sequence num id
  deb = line.find('|', 0, len(line)-1)
  end = line.find('|', deb+1, len(line)-1)
  descriptor = line[deb+1:end]

  ## Read all line and make the sequence
  buf = file_fasta.readlines()
  seq = "";
  for str in buf:
    seq += str[:len(str)-2]

  ## return
    ## [0] -> desciptor
    ## [1] -> sequence
  return descriptor, seq




def read_2_file():

  ## Init the directory and the extension for concatenate with the file name
  directory, extension = "fasta/", ".fasta"
  name_file1 = raw_input("Name file sequence1 (without extension)? \n")
  name_file2 = raw_input("Name file sequence2 (without extension)? \n")

  ## Test1
  # name_file1 = "DotSeq1"
  # name_file2 = "DotSeq2"

  ## Test2
  # name_file1 = "POAA25"
  # name_file2 = "P14949"

  ## Concatenate
  file_seq1 = directory + name_file1 + extension
  file_seq2 = directory + name_file2 + extension

  ## return
      ## [0][0] -> desciptor first sequence
      ## [0][1] -> first sequence
      ## [1][0] -> desciptor second sequence
      ## [1][1] -> second sequence
  return read_seq( file_seq1 ), read_seq( file_seq2 )

#######################################################################
########################## matrix functions ###########################
#######################################################################

def max( a, b ):
  if a > b:
    return a
  return b





def init_matrice( seq1, seq2 ):

  ## Found the max
  sizex = max( len(seq1), len(seq2) )
  if sizex == len(seq1):
    seq_max, seq_min, sizey = seq1, seq2, len(seq2)
  else:
    seq_max, seq_min, sizey = seq2, seq1, len(seq1)

  ## Init the matrix
    ## matrice( char, char, isequals )
  matrice = [ [(0, 0, 0)] * sizex for _ in range(sizey)]
  isdraw = 0

  ## Fill the matrix
  for y in range(sizey):
    for x in range(sizex):

      ## Check equality
      if seq_min[y] == seq_max[x]:
        isequals = 1
      else:
        isequals = 0

      ## Fill
      matrice[y][x] = (seq_min[y], seq_max[x], isequals)

  ## return
    ## [0] -> matrice( char, char, isequals )
    ## [1] -> sizex
    ## [2] -> sizey
  return matrice, sizex, sizey




def check_aligne( matrice, sizex, sizey, size_align ):

  ## To_draw: tab which respect the good align
  to_draw = [ [0] * sizex for _ in range(sizey)]

  ## Run into the matrix
  for y in range(sizey):
    for x in range(sizex):
      count_align = 0

      ## Check is equality between two sequences char
      if matrice[y][x][2] == 1:

        for i in range(size_align):
          ## Count align
          if y+i < sizey and x+i < sizex:
            count_align += matrice[y+i][x+i][2]

        ## If count_align is more than size_align, fill the to_draw matrix
        if count_align != 0 and count_align >= size_align:
          for i in range(size_align):
            to_draw[y+i][x+i] = 1

  ## return
    ## [0] -> to_draw matrix
    ## [1] -> sizex
    ## [2] -> sizey
  return to_draw, sizex, sizey




def print_matrice( matrice, sizex, sizey ):
  for y in range(sizey):
    for x in range(sizex):
      print matrice[y][x],
    print "\n"




def print_table( matrice, sizex, sizey, pos ):
  flags = 1
  for x in range(sizex):
    if flags == 1:
      print "   " + matrice[0][x][1],
      flags = 0
    else:
      print matrice[0][x][1],

  print "\n"
  for y in range(sizey):
    flags = 1
    for x in range(sizex):
      if flags == 1:
        print matrice[y][x][0] + " ",
        flags = 0
        print matrice[y][x][pos],
      else:
        print matrice[y][x][pos],
    print "\n"

#######################################################################

def init_graph( pourc, num_nuc ):

  ##
  seq = read_2_file()
  matrice = init_matrice( seq[0][1], seq[1][1] )

  ##
  #max = (20,12)
  plt.figure(figsize=(20,12), dpi=80)

  ##
  maxi = max( len( seq[0][1] ), len( seq[1][1] ) )

  if maxi < 350:
    size_pourc = 10
  else:
    size_pourc = 20

  ##
  posx = len( seq[0][1] ) / 2
  posy = int( ( size_pourc / 100.0 ) * len( seq[1][1] ) )
  posy = -posy

  ##
  plt.text(posx, posy, "Title: Dotplot", horizontalalignment = 'center', fontsize = 20)

  ##
  axes = plt.gca()

  ##
  plt.xlabel( seq[0][0] )
  plt.ylabel( seq[1][0] )

  ##
  plt.xlim( 0, maxi )
  plt.ylim( maxi, 0 )

  ##
  axes.xaxis.set_label_position('top')
  axes.xaxis.set_ticks_position('top')

  ##
  pourc = int( ( pourc / 100.0 ) * num_nuc )
  if pourc < 1:
    pourc = 1

  ##
  tab   = check_aligne( matrice[0], matrice[1], matrice[2], pourc )
  sizex = tab[1]
  sizey = tab[2]

  ##
  for y in range(sizey):
    for x in range(sizex):
      if tab[0][y][x] == 1:
        plt.scatter(x+1, y+1, c = "black", s=10)

  ##
  out_file = raw_input("File name ? \n")
  directory = "out/"

  ## Tets
  # out_file = "output"

  directory += out_file

  plt.savefig(directory + ".png", bbox_inches = "tight")

  ##
  plt.show()


def main():
  pourc = int(input("Seuil identite ( in pourcent )? \n"))
  num_nuc = int(input("fenetre ? \n"))

  ## test
  # pourc = 5
  # num_nuc = 50

  init_graph( pourc, num_nuc )

#######################################################################

main()
