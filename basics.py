# Task 1: Function to return letter grade from score
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print("Grade for score 95:", get_letter_grade(95))
print("Grade for score 82:", get_letter_grade(82))
print("Grade for score 45:", get_letter_grade(45))


# Task 2: FizzBuzz 1 to 100
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

print("\n--- FizzBuzz Output ---")
fizzbuzz()
