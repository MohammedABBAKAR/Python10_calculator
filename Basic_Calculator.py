# Create a function that takes two numbers and 
# a mathematical operator + - / * and will perform a 
# calculation with the given numbers.

# Examples

# calculator(2, "+", 2) ➞ 4

# calculator(2, "*", 2) ➞ 4

# calculator(4, "/", 2) ➞ 2

def calculator(num1, operator, num2):
    if operator == "+" :
       return num1 + num2
    elif operator == "*":
       return num1 * num2
    elif operator == "/":
       return num1 /num2
print(calculator(2,"+",3))


def calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

# Examples
print(calculator(2, "+", 2))  # ➞ 4
print(calculator(2, "*", 2))  # ➞ 4
print(calculator(4, "/", 2))  # ➞ 2
print(calculator(4, "/", 0))  # ➞ Error: Division by zero
print(calculator(4, "%", 2))  # ➞ Error: Invalid operator
