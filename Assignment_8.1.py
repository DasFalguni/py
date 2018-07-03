# Input the file name
fname = raw_input("Enter file name: ")
# Open the file handler
fh = open(fname)
# List to store the lines and split the values
list_line = []
# List the entire content in the file
list_file = []
for line in fh:
    list_line = line.rstrip().split()
    #list1 = line.split()
    #print list1
    list_file.extend(list_line)
# Sort the list
list_file.sort()
# The expected list without the duplicate values
list_expected = []
for i in range(len(list_file)):
    value = list_file[i]
    if list_file[i] not in list_expected:
        list_expected.append(list_file[i])
    else:
        continue
print list_expected
