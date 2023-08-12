for i in range(1, 11):  # Outer loop for rows
    num = i
    for j in range(1, 11):  # Inner loop for columns
        print(num, end='   ')  # Format the number with 3 spaces
        num += i
    print()  # Move to the next line after each row
