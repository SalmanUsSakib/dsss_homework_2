import random

def rndm_integer(mn_value, mx_value):
    """
    Random Integer generated which is mn_value(int) and mx_value(int).

    """
    return random.randint(mn_value, mx_value)


def rndm_operator():
    """
    Random operator of Arithmatic

    """
    return random.choice(['+', '-', '*'])


def new_problem(number1, number2, op):
    """
    Two numbers and an operator been created by new math problem.
        
    """
    prb_stat = f"{number1} {op} {number2}"
    if op == '+':
        right_answer = number1 + number2
    elif op == '-':
        right_answer = number1 - number2
    else:
        right_answer = number1 * number2
    return prb_stat, right_answer


def math_quiz():
    """
    A simple math quiz game that presents the user with math problems and checks their answers.
    """
    score = 0
    tot_num_questions = 3 #have to use interger instead of floating number 

    print("Welcome to a nice Math Quiz Problem")
    print("Here there will be some math problems as well as their answers.")

    for _ in range(tot_num_questions):
        number1 = rndm_integer(1, 10)
        number2 = rndm_integer(1, 5) # using random.randint(mn_value, mx_value) as a interger type.  
        op = rndm_operator()

        prb_stat, right_answer = new_problem(number1, number2, op)
        
        print(f"\nQuestion: {prb_stat}") # Showing problem
        try:
            user_right_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid number. Kindly enter an valid integer.")
            continue  # Skip the upcoming question
        
        if user_right_answer == right_answer: #if ans correct
            print("You have a point.")
            score += 1
        else:
            print(f"Wrong answer. The Right answer is {right_answer}.")

    # Display the final output
    print(f"\nGame is over! Your final score is: {score}/{tot_num_questions}")

if __name__ == "__main__":
    math_quiz()
