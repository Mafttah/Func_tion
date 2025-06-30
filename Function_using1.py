# # klasik function kullanımı
# def first_function():
#     isim = input("İsminizi girin: ")
#     print(f"Merhaba {isim}")
# # parametresiz bir fonksiyonun çağırılması
# first_function()    

# parametreli kullanım
def second_function(mesaj):
    user_answer = input(f"{mesaj}")
    print(f"Mesajınız: {user_answer}")

second_function("What is your birthday?: ")
second_function("Are you married?: ")