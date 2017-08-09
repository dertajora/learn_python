numbers = [1,2,3,4,5,6,7]
for number in numbers:
	if number % 2 == 0:
		print(number)
	

# x = 0 - 4
for x in range(5):
	print(x)

# x = 3 - 5
for x in range(3,6):
	print(x)

# x = 3,5,7 karena intervalnya = 2 , batas awal = 3, batas akhir = 8
for x in range(3,8,2):
	print(x)

#while 
count = 0 
while count < 5:
	print(count)
	count += 1

#use continue when condition meet, skip 1 loop saja
for x in range(1,10):
	if x % 2 == 0:
		continue
	print(x)


#use break when condition meet, stop the loop
for x in range(1,10):
	if x >= 5:
		break
	print(x)


# else condition in loop
count = 0 
while(count<5):
	print(count)
	count += 1
else:
	print("Value count reached 5")

# credit : https://www.learnpython.org/en/Loops