"""
You have to write a function printer_error which given a
string will return the error rate of the printer as a string
representing a rational whose numerator is the number of errors
and the denominator the length of the control string. Don't reduce
this fraction to a simpler expression.
The string has a length greater or equal to one and contains only letters from a to z.

Examples:
s="aaabbbbhaijjjm"
error_printer(s) => "0/14"
s="aaaxbbbbyyhwawiwjjjwwm"
error_printer(s) => "8/22"
"""
def printer_error(s):
    lenght=len(s)
    errors=0
    for i in range(lenght):
        if ord(s[i]) > 109 :
            errors+=1

    return ("{}/{}".format(errors,lenght))



s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
print(printer_error(s))
