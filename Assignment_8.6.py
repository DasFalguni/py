# Enter the file name
name = raw_input("Enter file:")
# Assign the default file name
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
time = list()
hour_list = list()
tot_hour_list = list()
lst = list()
counts = dict()
for line in handle:
    if line.startswith ('From:'):
        continue
    elif line.startswith ('From'):
    	hour_list = line.rstrip().split()
    	# storing the time part in a list
    	time = hour_list[5].split(':')
    	# storing the hour in a string
    	hour = time[0]
    	# form the list with all the hours
    	tot_hour_list.append(hour)
    else:
        continue

# Prepare the dictionary with hour and no. of times
for hour in tot_hour_list:
    counts[hour] = counts.get(hour,0) + 1

# Prepare the tuple and sort it by key values.
for key, val in counts.items():
    lst.append((key, val))
lst.sort()

# print the tuple
for key, val in lst[0:]:
    print key, val
    
