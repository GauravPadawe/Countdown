def countdown(a):
	while True:
		if a:
			print a
			a = a - 1
			if a == 0:
				print "Blastoff"
				break
				
print countdown(7)