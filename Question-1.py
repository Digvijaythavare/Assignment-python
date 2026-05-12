# Create function to add tow numbers
def add_numbers(num1,num2):
    return num1 + num2
# Create function to subtract two numbers
def subtract_numbers(num1,num2):
    return num1 - num2
usre_input1 = float(input("Enter first number: "))
usre_input2 = float(input("Enter second number: "))
# Call the functions and print the results
print("The sum of the two numbers is: ", add_numbers(usre_input1,usre_input2))
print("The difference of the two numbers is: ", subtract_numbers(usre_input1,usre_input2))
