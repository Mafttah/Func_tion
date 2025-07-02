def user_input_with_message(message):
    user_message = input(f"{message}")
    return user_message

def user_print_with_method(to_print):
    print("----------------------")
    print(f"{to_print}")

def generate_info(_info1, _info2):
    _info1 = _info1.strip()
    _info2 = _info2.strip()
    info = _info1 + " " + _info2
    return info
    

university = user_input_with_message("Üniversite adı: ")
course = user_input_with_message("Kurdun adı: ")
hobby = user_input_with_message("Bir hobi söyle: ")
city = user_input_with_message("Gezerken hoşlandığın bir şehir: ")
wish = user_input_with_message("İlerde yapmak ya da öğrenmek istediğin bir şey: ")
print("")

generated_degree = generate_info(university, course)
user_print_with_method(generated_degree)
user_print_with_method(hobby)
user_print_with_method(city)
user_print_with_method(wish)

