#Input the file name
fname = raw_input("Enter file name: ")
# Check in case the user does not enter the right file name, set default
if len(fname) < 1 : fname = "mbox-short.txt"
# Open the file handler
fhand = open(fname)
count = 0
list_email = []
# Do the calculation and manipulation
for line in fhand:
    if line.startswith ('From:'):
        count = count + 1
        list_email = line.rstrip().split()
        email = list_email[1]
        print email
    else:
        continue

print "There were", count, "lines in the file with From as the first word"
