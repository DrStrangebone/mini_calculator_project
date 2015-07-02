'''
SIMPLE CALCULATOR. 

BY DR STRANGEBONE

'''

num1 = int(raw_input("First number: "))
operator = raw_input("Which operator (*, +, -, /): ")
num2 = int(raw_input("Second number: "))

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












