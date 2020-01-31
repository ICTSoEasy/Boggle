INFILE = './words.txt'
OUTFILE = './newwords.txt'
infile = open(INFILE,'r')
outfile = open(OUTFILE,'w')
lines = infile.readlines()
for word in lines:
    outfile.write(word.upper())
infile.close()
outfile.close()