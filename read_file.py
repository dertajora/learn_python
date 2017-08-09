

with open("product.ini", "r") as file:
    
    # print file.readline(1)
    print file.readlines()

file = open("derta.txt", "r") 
for line in file: 
	print line 

print("Read file sukses !")