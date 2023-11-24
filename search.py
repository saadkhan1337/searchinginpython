a=(9,8,7,6,5,4,3,2,1)
b=int(input("enter the number you want to search"))
flag=0
for i in a:
    if i==b:
        print("Found")
        flag=1
        break
if flag==0:
    print("not found")


##a=(9,8,7,6,5,4,3,2,1)
##b=int(input("enter the number you want to search"))
##if(b in a):
##    print("Found")
##else:
##    print("not found")
##
##    
