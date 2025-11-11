import sys
print (sys.argv[0]) #this is the first element of the arguments.
#If you need to add a path, put the path in quotes and concatenate
sys.argv[0]
file= open(sys.argv[1]) #sys.argv[1] contains the 2nd argument
for i in file:
    print (i.rstrip)
print ("goodbye")