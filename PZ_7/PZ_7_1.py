def evaluate_expression(expression):
    total = 0
    current_number = 0
    operation = '+'
    for char in expression:
        if char.isdigit():
            current_number = int(char)
        elif char in '+-':
            if operation == '+':
                total += current_number
            elif operation == '-':
                total -= current_number
            operation = char
    if operation == '+':
        total += current_number
    elif operation == '-':
        total -= current_number
    return total
expression = "4+7-2-8"
result = evaluate_expression(expression)
print(result)
