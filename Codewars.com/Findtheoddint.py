#Find the odd int in codewars.com
#made by own

def find_it(seq):
    count=0
    for i in range(len(seq)):
        for j in range(len(seq)):
            if seq[i]==seq[j]:
                count+=1
        if count%2!=0 :
            return(seq[i])
            break
        count=0


print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
print(find_it([10]))
print(find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]))
print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))
print(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]))





