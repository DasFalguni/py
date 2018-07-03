fname = raw_input('Enter the file name:')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith ('Subject:'):
        count = count + 1
print 'There are', count, 'subject lines in', fname


# Enter the file name
name = raw_input("Enter file:")
# Assign the default file name
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
sender = list()
sender_list = list()
counts = dict()
for line in handle:
    if line.startswith ('From:'):
    	sender = line.rstrip().split()
    	#print sender
    	the_sender = sender[1]
    	#print the_sender
    	sender_list.append(the_sender)
        
    else:
        continue


for name in sender_list:
    counts[name] = counts.get(name,0) + 1

#print counts
most_committer = None
most_number = None

for committer, number in counts.items():
    if most_committer is None or number > most_number:
        most_committer = committer
        most_number = number
