def countdown(a):                                    # Defining a procedure "Countdown" that takes single input
	while True:                                  # Intialize While loop
		if a:                                # If Statement
			print a                      # Printing "a" will print value of "a" as is
			a = a - 1                    # As we want to define countdown we must minus the initial value by 1
			if a == 0:                   # when a's value becomes 0, then print "BlastOff!!"
				print "Blastoff"
				break                # breaking the loop
				
print countdown(7)

# CODED BY - GAURAV PADAWE
