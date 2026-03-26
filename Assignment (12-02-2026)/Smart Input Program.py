# Smart Input Program

# Taking input from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

# Categorizing age using conditional statements
if age < 13:
    category = "a child"
elif age < 20:
    category = "a teenager"
elif age < 60:
    category = "an adult"
else:
    category = "a senior citizen"

# Displaying personalized message
print("\nHello", name + "!")
print("You are", category, "and it is great that you enjoy", hobby + ".")