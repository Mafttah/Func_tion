# parametre alan, işlenen sonucu return ile gönderen function
def user_input_with_message(message):
    user_message = input(f"{message}")
    return user_message

# parametre alan, işlem yapan, return ile değer göndermeyen function
def user_print_with_method(to_print):
    print("----------------------")
    print(f"{to_print}")

def generate_info(_info1, _info2):
    _info1 = _info1.strip()
    _info2 = _info2.strip()
    info = _info1 + " " + _info2
    return info
    

name = user_input_with_message("Adınızı giriniz: ")
surname = user_input_with_message("Soyadınızı giriniz: ")
city = user_input_with_message("Yaşadınız şehir: ")
town = user_input_with_message("Bulunduğunuz ilçe: ")
occupation = user_input_with_message("Mesleğiniz: ")
print("")

generated_full_name = generate_info(name, surname)
user_print_with_method(generated_full_name)
generated_city = generate_info(town, city)
user_print_with_method(occupation)
user_print_with_method(generated_city)




