'''
SIMPLE CALCULATOR. 

BY DR STRANGEBONE

'''

print "Shittiest calculator ever made. Enjoy!"


num1 = int(raw_input("First number: "))
operator = raw_input("Which operator (*, +, -, /): ")
num2 = int(raw_input("Second number: "))

redo = num1, operator, num2

if operator == '*':
    result = num1 * num2
    print result
elif operator == '+':
    result = num1 + num2
    print result
elif operator == '-':
    result = num1 - num2
    print result
elif operator == '/':
    result = num1 / num2
else:
    print "OPERATOR ERROR"
    
    

reuse = raw_input("Do you need to use it again? Y/N: \n")

yNo = 'Y'
if yNo == 'Y':
    print redo
else:
    print "ERROR - CLOSING."
#This needs fixing. Will fix later.











