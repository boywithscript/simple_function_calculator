# Function Calculator

def cal(a, b, operation):
    match operation:
        case "+": return a + b
        case "-": return a - b
        case "*": return a * b
        case "**": return a ** b
        case "/": return a / b if b != 0 else  "Error: Can't divide by zero"
        case _: return("Error : Operation invalid")
       
print (cal(2, 6, "+"))
print (cal(6, 2, "/"))
print (cal(2, 0, "/"))
print (cal(3, 4, "%"))
