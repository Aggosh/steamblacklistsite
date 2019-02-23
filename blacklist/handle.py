from .models import blacklist
from datetime import datetime

def handle_uploaded_file(f, user):
	with open('files/add_to_blacklist.ini', 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

	new_edit_black = blacklist.objects.create(user=user, pub_date=datetime.now(), )
	add_to_blacklist(new_edit_black)
	del_repeat(new_edit_black)


def add_to_blacklist(new_edit_black):
	with open('files/add_to_blacklist.ini', 'r') as f1:
		with open('files/blacklist.ini', 'a') as f2:
			for line in f1:
				if line[:7] == '7656119' and len(line) == 18:
					f2.write(line)

def del_repeat(new_edit_black):
	a = []
	with open('files/blacklist.ini', 'r') as f:
		for line in f:
			if line[:7] == '7656119' and len(line) == 18:
				a.append(line.replace('\n', ''))

	a = list(set(a))
	with open('files/blacklist.ini', 'w') as f:
		for x in a:
			f.write(str(x+'\n'))

	new_edit_black.blacklist_size = len(a)
	old_black = blacklist.objects.get(pk=(new_edit_black.pk-1))
	new_edit_black.edit = new_edit_black.blacklist_size - old_black.blacklist_size
	new_edit_black.save()
		