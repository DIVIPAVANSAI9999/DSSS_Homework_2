import random

#This function generates a random integer between the given range by the user.
def function_A(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)

#This function returns a random choice from the given list.
def function_B():
    return random.choice(['+', '-', '*'])

#This function takes two numbers (n1 and n2) and an operator (o) as input.
def function_C(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    s = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = function_A(1, 10); n2 = function_A(1, 5.5); o = function_B()

        PROBLEM, ANSWER = function_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
         # Convert useranswer to float to handle cases where the result is not an integer
        useranswer = float(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

<<<<<<< HEAD
    print(f"\nYou scored {s} out of {int(t_q)} points.")

# Call the math_quiz function to start the quiz.
    math_quiz()
=======
   print(f"\nYou scored {s} out of {int(t_q)} points.")

# Call the math_quiz function to start the quiz.
    math_quiz()
>>>>>>> 5ef7d37dc458eccf14760db2ffcf01f5f679c485
