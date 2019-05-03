#!/usr/bin/env python
import os
import sys

def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def isOps(x):
    if (x == '+' or x == '-' or x == '*' or x == '/'):
        return True
    else:
        return False

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def oper (x, expr):
    if x == '+':
        x = plus(expr)
    elif x == '-':
        x = minus(expr)
    elif x == '*':
        x = mult(expr)
    elif x == '/':
        x = div(expr)
    return x

def binop(xpn):
    e = False
    if len(xpn) > 0: 
        l = xpn.pop()
    else:
        return 0, 0, True 
    l = oper(l,xpn)

    if len(xpn) > 0: 
        r = xpn.pop()
    else:
        return 0, 0, True
    r = oper(r,xpn)
    return l, r, e

def plus (xpn):
    l, r, e = binop(xpn)
    if (e == False):
        return (l + r)
    else:
        return ("Input Error")

def minus (xpn):
    l, r, e = binop(xpn)
    if (e == False):
        return (l - r)
    else:
        return ("Input Error")

def mult (xpn):
    l, r, e = binop(xpn)
    if (e == False):
        return (l * r)
    else:
        return ("Input Error")

def div (xpn):
    l, r, e = binop(xpn)
    if (e == False):
        return (l / r)
    else:
        return ("Input Error")

def parse(instring):
    expr = instring.strip().split(" ")
    index = 0
    for x in expr:# check for illigal elements in the prefix expresssion
        if (expr[index] != '+' and expr[index] != '-' and expr[index] != '*' 
                    and expr[index] != '/' and isDigit(expr[index]) == False):
            return("Input Error")
        else:
            if isDigit(expr[index]): # convert into number from string
                expr[index] = num(expr[index])

        index += 1
    return expr

def calculate(str):
    xpn = parse(str) # split the prefix expression into operators and numbers  
    if xpn == "Input Error":
        return("Input Error")

    xpn.reverse() # reverse the list such that I can use list.pop() operation

    if (len(xpn) > 0):
        x = xpn.pop() # get the first element in the prefix expression
    if isOps(x) == True:
        res = oper(x, xpn) # Calls the actual function to evaluate the operator
        if isDigit(res) and len(xpn) > 0:
            return("Input Error")
        else:
            return (res)
    elif len(xpn) == 0:
        return (x)
    else:
        return("Input Error")

#+ * 3 4 / 8 2
if __name__== '__main__':
    inputline = input("Please input Prefix Expression\n")
    #inputline = ['+', '*', 3, 4, '/', 8, 2,]
    print (calculate(inputline))
