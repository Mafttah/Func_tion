def function_user_input(message):
    user_answer = input(f"{message}")
    while True:
        if user_answer == "":
            print("Don't pass")
            continue
        break
    return user_answer
    


def function_user_print(to_print):
    print("---------------")
    print(f"{to_print}")
    print("---------------")


user_name = function_user_input("What is your name?: ")

function_user_print(user_name)

is_married = function_user_input("Are you married?: ")
function_user_print(is_married)

user_city = function_user_input("What is your city?: ")
function_user_input(user_city)
