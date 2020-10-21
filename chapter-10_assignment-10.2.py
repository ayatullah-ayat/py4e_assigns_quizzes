# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

email_sender_list = list()
for line in handle:
	word_list = line.split()

	if len(word_list) < 2:
		continue
	if not word_list:
		continue
	if not line.startswith('From '):
		continue
	email_sender_list.append(word_list[5])

item_dict = dict()
for item in email_sender_list:
	item = item.split(':')
	it = item[0]
	item_dict[it] = item_dict.get(it, 0) + 1
for key, value in sorted(item_dict.items()):
	print(key, value)
