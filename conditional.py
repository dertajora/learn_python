cek = 10
while cek > 1:
	
	if cek >= 8:
		pass
	elif cek > 5:
		print cek
	else:
		print "A\n"

	# decrease value 
	cek -= 1

cek += 10
# how to print string and int using modern string format
print "{} and {}".format("string anything", cek)