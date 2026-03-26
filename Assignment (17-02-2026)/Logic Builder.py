# Logic Builder Assignment

def fizz_buzz():
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0

    for number in range(1, 51):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
            fizzbuzz_count += 1
        elif number % 3 == 0:
            print("Fizz")
            fizz_count += 1
        elif number % 5 == 0:
            print("Buzz")
            buzz_count += 1
        else:
            print(number)

    print("\nTotal Fizz:", fizz_count)
    print("Total Buzz:", buzz_count)
    print("Total FizzBuzz:", fizzbuzz_count)

# Calling the function
fizz_buzz()