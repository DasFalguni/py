# Enter the file name
name = raw_input("Enter file:")
# Assign the default file name
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
time = list()
hour_list = list()
tot_hour_list = list()

counts = dict()
for line in handle:
    if line.startswith ('From:'):
    	hour_list = line.rstrip().split()
    	#print sender
    	time = hour_list[2].split(':')
    	print time
    	hour = time[0]
    	print hour
    	#print the_sender
    	tot_hour_list.append(hour)
    else:
        continue

for hours in tot_hour_list:
            counts[hours] = counts.get(hours, 0) + 1
        
print counts
