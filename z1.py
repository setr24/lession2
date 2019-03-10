#Задание 1 - Возраст

def age_list (age, max_age=99):
    if age <= 7:
     return "Иди в детский сад!"
    if age <= 18:
        return "Пора в школу!" 
    if age <= 23:
        return "Пары ждут"
    if age >= max_age:
        return "Столько не живут"
    else:
        return "А че не на работе?"

age = int(input("Какой Ваш возраст:")) 
print(age_list(age))