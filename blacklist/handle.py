
def handle_uploaded_file(f):
	with open('files/add_to_blacklist.ini', 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

	add_to_blacklist()
	del_repeat()


def add_to_blacklist():
	with open('files/add_to_blacklist.ini', 'r') as f1:
		with open('files/blacklist.ini', 'a') as f2:
			for line in f1:
				if line[:7] == '7656119' and len(line) == 18:
					f2.write(line)

def del_repeat():
	a = []

	with open('files/blacklist.ini', 'r') as f:
		for line in f:
			if line[:7] == '7656119' and len(line) == 18:
				a.append(line.replace('\n', ''))

	a = list(set(a))

	with open('files/blacklist.ini', 'w') as f:
		for x in a:
			f.write(str(x+'\n'))
		