#imports
import os
import sys

def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

#function to solve the prefix expression
def solve_expression(exp):

    #keep running while the list is not at length 1
    while len(exp) != 1:
        i = 0
        ops = 0 #how many times evaluation happened in each pass
        #iterate through the list
        while i < len(exp)-2:
            #check for +, -, *, /
            if exp[i] == '+' or exp[i] == '-' or exp[i] == '*' or exp[i] == '/':
                #strip next two elements of - sign to check to see if it's a digit
                x = isDigit(exp[i+1].lstrip('-+'))
                y = isDigit(exp[i+2].lstrip('-+'))
                # if both are numbers then process
                if x and y:
                    ops += 1
                    #add
                    if exp[i] == '+':
                        value = str(num(exp[i+1]) + num(exp[i+2]))
                        exp[i] = value
                        del exp[i+1]
                        del exp[i+1]
                    #subtract
                    elif exp[i] == '-':
                        value = str(num(exp[i+1]) - num(exp[i+2]))
                        exp[i] = value
                        del exp[i+1]
                        del exp[i+1]
                    #multiply
                    elif exp[i] == '*':
                        value = str(num(exp[i+1]) * num(exp[i+2]))
                        exp[i] = value
                        del exp[i+1]
                        del exp[i+1]
                    elif exp[i] == '/':
                        value = str(num(exp[i+1]) / num(exp[i+2]))
                        exp[i] = value
                        del exp[i+1]
                        del exp[i+1]
                else:
                    pass
            else:
                pass
            i += 1
        
        if ops == 0:
            return ("Input Error") # The expression is not valid, since it didn't evaluate anything is this pass!
    #return final value
    return exp[0]

def parse(instring):
    expr = instring.strip().split(" ")
    index = 0
    for x in expr:
        if expr[index] != '+' and expr[index] != '-' and expr[index] != '*' and expr[index] != '/' and isDigit(expr[index]) == False:
            return("Input Error")
        else:
            pass

        index += 1
    return expr

def calculate(str):
    xpn = parse(str)
    if xpn == "Input Error":
        return("Input Error")
    else:
        res = solve_expression(xpn)
        if isDigit(res) == False:
            return("Input Error")
        else:
            return(res)


# Main
if __name__ == "__main__":
    inputline = "* 4 5"
    # process the prefix expression
    res = calculate(inputline)
    print (res)
