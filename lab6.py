#develop a porgram to sort contents of a file and write the sorted contents to another file
import os.path
import sys
fname=input("Enter the name of the file to be sorted: ")

if not os.path.isfile(fname):
    print("File does not exist.")
    sys.exit(0)

infile = open(fname, "r")
mylist = infile.readlines()
linelist = []
for line in mylist:
    linelist.append(line.strip())
linelist.sort()

outfile=open("sorted.txt", "w")
for line in linelist:
    outfile.write(line + "\n")
outfile.close()
infile.close()

if os.path.isfile("sorted.txt"):
    print("File sorted.txt created successfully.") 
    print("sorted.txt",len(linelist), "lines")
    print("Contents of sorted.txt:")
    print("==========================")
    rdfile= open("sorted.txt", "r")
    for line in rdfile:
        print(line, end="")