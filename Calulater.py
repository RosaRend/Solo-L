While True:
  print("Welcome to Asimca( A SIMply CAlulater),\nAsimca is here to satisfy all your\nbasic calulation needs. I don't want to keep you\ntoo long so heres how to get started your options are to.....")
  print("Enter 'add' to add two numbers.")
  print("Enter 'subtract' to subtract two numbers.")
  print("Enter 'multiply' to multiply two numbers.")
  print("Enter 'divison' to divide two numbers.")
  print("Enter 'quit' to end the program.")
  if user_input == "quit":
    break
  elif user_input == "add":
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    result = str(num1 + num2)
    print("Your outcome is " + result)
  elif user_input == "subtract":
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    result = str(num1 - num2)
    print("Your outcome is " + result)
  elif user_input == "multiply":
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    result = str(num1 * num2)
    print("Your outcome is " + result)
  elif user_input == "divide":  
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    result = str(num1 / num2)
    print("Your outcome is " + result)
  else:
    print("Unknown input")
