# Initialize the sum variable
total_sum = 0

# Loop to get 10 numbers from the user
for i in range(10):
    # Get user input
    number = float(input(f"Enter number {i + 1}: "))
    # Add the number to the total sum
    total_sum += number

# Print the total sum
print("The sum of the 10 numbers is:", total_sum)
