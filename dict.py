

def missing():
	d = {1:"one",2:"two"}
	if 1 in d :
		print("1 exists")

	if not 3 in d:
		print("3 does not exists")


if __name__== '__main__':
	missing()