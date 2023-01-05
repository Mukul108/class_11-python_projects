# python code to Check if element exists in list or not
 
lst=[ 1, 6, 3, 5, 3, 4, 5, 6, 7, 8, 9 ]
#checking if element 7 is present
# in the given list or not
i = int(input("write digit here:"))
# if element present then return
# exist otherwise not exist
if i in lst:
    print("exist")
else:
    print("not exist")