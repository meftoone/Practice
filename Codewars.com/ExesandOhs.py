"""
Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive.
The string can contain any char.
Examples input/output:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""
#made by own
def xo(s):
    xcounts=0
    ocounts=0
    for i in range(len(s)):
        if s[i]=="x"or s[i]=="X":
            xcounts+=1
        elif s[i]=="o"or s[i]=="O":
            ocounts+=1
        else:
            pass
    if xcounts==ocounts:
        return True
    else:
        return False

print(xo('xo'), 'True expected')
print(xo('xo0'), 'True expected')
print(not xo('xxxooo'), 'False expected')

