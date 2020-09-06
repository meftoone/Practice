"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
Write a method that takes the array as an argument and returns this "outlier" N.
Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)
[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""
def find_outlier(integers):
    for i in range(0,len(integers)):
        if(integers[i]%2==0 and integers[i+1]%2==0 and integers[i+2]%2==1):##ÇÇT
                return integers[i+2]
        elif(integers[i]%2==1 and integers[i+1]%2==1 and integers[i+2]%2==0):##TTÇ
                return integers[i+2]
        elif(integers[i]%2==0 and integers[i+1]%2==1 and integers[i+2]%2==1):#ÇTT
                return integers[i]
        elif(integers[i]%2==1 and integers[i+1]%2==0 and integers[i+2]%2==0):#TÇÇ
                return integers[i]
        elif(integers[i]%2==0 and integers[i+1]%2==1 and integers[i+2]%2==0):#ÇTÇ
                return integers[i+1]
        elif(integers[i]%2==1 and integers[i+1]%2==0 and integers[i+2]%2==1):#TÇT
                return integers[i+1]

print("PRINT MUST BE 1->",find_outlier([0, 1, 2]))
print("PRINT MUST BE 11->",find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print("PRINT MUST BE 160->",find_outlier([160, 3, 1719, 19, 11, 13, -21]))