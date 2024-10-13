file=open("text.txt","r")
print(file.read())
#method 2
for y in file:
    print(y)
#writng to a file
file=open("text.txt","w")
file.write("yes hello")
file.write("yes bye")
file.close()
file=open("text.txt","a")
file.write("yes hi")
file.write("yes byebye")
file.close()