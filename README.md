# Function Calculator

A simple Python function-based calculator that performs basic arithmetic operations using the `match-case` statement.

## Features

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Exponentiation (`**`)
- Division (`/`) — includes zero division check
- Handles invalid operations gracefully

## Code Example

```python
def cal(a, b, operation):
    match operation:
        case "+": return a + b
        case "-": return a - b
        case "*": return a * b
        case "**": return a ** b
        case "/": return a / b if b != 0 else  "Error: Can't divide by zero"
        case _: return("Error : Operation invalid")

Sample Output:

print(cal(2, 6, "+"))   # Output: 8
print(cal(6, 2, "/"))   # Output: 3.0
print(cal(2, 0, "/"))   # Output: Error: Can't divide by zero
print(cal(3, 4, "%"))   # Output: Error : Operation invalid

Requirements

Python 3.10 or later (due to use of match-case)


How to Run

python cal.py

License

MIT License (or any other license you prefer)


