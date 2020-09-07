"""
Take 2 strings s1 and s2 including only letters from ato z.
Return a new sorted string, the longest possible, containing distinct letters,
each taken only once - coming from s1 or s2.
Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"
a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""

#i did this cause i didnt know the set function :( it can do add two str this way
#    def longest(a1, a2):
#       return "".join(sorted(set(a1 + a2)))
# this is the short way


def longest(s1, s2):
    s1+=s2
    s1=sorted(s1)
    s1=deletesame(s1)
    return s1
def deletesame(string:str):
    removed=list(string)
    for i in range(len(string)-1):
        if removed[i]==removed[i+1]:
            removed[i]=""
    string="".join(removed) #almost spend 1 hours to find that "".join() usage with some music ofc :)
    return string



print(longest("sedat","hakan"))

