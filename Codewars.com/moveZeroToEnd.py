"""

move zeros to end

"""
def move_zeros(array):
    new = []
    zeros = []
    for i in range(len(array)):
        if array[i] == 0 or array[i] == 0.0:
            if type(array[i]) == int or type(array[i]) == float:
                zeros.append(array[i])
            else: new.append(array[i])
        else:
            new.append(array[i])
    return new + zeros


move_zeros([1,2,0,1,0,1,0,3,0,1])
move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9])
move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9])
move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9])
move_zeros([0,1,None,2,False,1,0])
move_zeros(["a","b"])
move_zeros(["a"])
move_zeros([0,0])
move_zeros([0])
move_zeros([False])
move_zeros([])


