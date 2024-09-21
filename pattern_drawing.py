# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to draw the pattern
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after finishing one row
    row += 1  # Increment the row counter
