

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
	email_sender_list.append(word_list[1])
word_dict = dict()
for item in email_sender_list:
	word_dict[item] = word_dict.get(item, 0) + 1

print(word_dict)
max_sender = max(word_dict, key=word_dict.get)
max_num = max(word_dict.values())
print(max_num)