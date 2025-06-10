#!/usr/bin/python
'''
    File name: genuss.py
    Author: wizardofzos
    Version: 1.1
    Date created: Jul 2, 2018
    Date last modified: Aug 20, 2018
    Python Version: 2.7

    Description:
    
    This program takes an 'ASCII-art' from file 'screen.txt'
    and generates the correct assembly statments so it can be
    used inside the source code for an USSTAB.

    There are some 'color-codes' that can be used to set various 
    colors. The general syntax is "=!x" where x is a letter
    Y = Yellow, B = Blue, R = Red, ...
    See source for all present codes.
    (only SFE/PROTECTED/NORMAL)

'''




with open('screen-aws.txt') as screen:
    screen_data = screen.read()
screen.close

with open('ebcdic-table') as ebcdic_stream:
	ebcdic = ebcdic_stream.read()
ebcdic_stream.close


hexval = {}
char   = {}

for line in ebcdic.split('\n'):
	vals = line.split('\t')
	if len(vals) < 3:
		continue	
	hexval[vals[2]] = vals[1]
        
fulldc = ""

# Some static colors (all SFE/PROTECTED/NORMAL)
# Use =!Y etc...
yellow    = "         DC    X'290242F6C0E0'"      # =!Y
blue      = "         DC    X'290242F1C0E0'"      # =!B
red       = "         DC    X'290242F2C0E0'"      # =!R
pink      = "         DC    X'290242F3C0E0'"      # =!P
green     = "         DC    X'290242F4C0E0'"      # =!G
truquoise = "         DC    X'290242F5C0E0'"      # =!T
black     = "         DC    X'290242F8C0E0'"      # =!C
dblue     = "         DC    X'290242F9C0E0'"      # =!D
orange    = "         DC    X'290242FAC0E0'"      # =!O
purple    = "         DC    X'290242FBC0E0'"      # =!U
pgreen    = "         DC    X'290242FCC0E0'"      # =!L
white     = "         DC    X'290242FFC0E0'"      # =!W









row=1
for line in screen_data.split('\n'):
    pos = 0
    if len(line) < 79:
        a  = 79 - len(line)
        line = line + (a*" ")
    # Print a positioning control to go to next row...
    print("         DC    X'11',AL2(((%d-1)*80)+(01-1))" % row)
    # Change the full line into EBCDIC X-codes...
    c = 0
    while c < len(line):
        
        # check for color-codes (=!R, =!B, =!Y for Red Blue Yellow)
        if line[c:c+3] == "=!Y":
            print(yellow)
            c = c + 3
        if line[c:c+3] == "=!B":
            print(blue)
            c = c + 3
        if line[c:c+3] == "=!G":
            print(green)
            c = c + 3
        if line[c:c+3] == "=!C":
            print(black)
            c = c + 3
        if line[c:c+3] == "=!R":
            print(red)
            c = c + 3
        if line[c:c+3] == "=!W":
            print(white)
            c = c + 3
        if line[c:c+3] == "=!C":
            print(black)
            c = c + 3
        if line[c:c+3] == "=!Y":
            print(yellow)
            c = c + 3
        if line[c:c+3] == "=!P":
            print(pink)
            c = c + 3
        char = line[c:c+1]
        try:
    	    print("         DC    X'%s'" % hexval[char])
        except KeyError:
            print("Error -> Key >%s< not found (row %s)" % (c, row))
            print(c.encode('hex'))
        c += 1
    row += 1







