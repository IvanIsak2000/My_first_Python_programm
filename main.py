print('программа: кодовый замок')
print("\nинструкция:\n  1)введите число-парооль\n 2)для выхода напишите:'выход'")
parol_ot_file = "1"

while True:  # цикл проверки введёного кода с кодом
    try:
        ввод = str(input("введите пароль "))
        if ввод == "выход":  # выход
            print("выход из программы:")
            print("ПРОГРАММА ЗАВЕРШЕННА")
            break
            parol_ot_file.close()
        elif ввод == parol_ot_file:  # правильынй пароль
            print("ПРАВИЛЬНЫЙ ПАРОЛЬ")
            print("ALL DONE")
            break
        elif ввод == "подсказка":
            print("длина пароля", len(parol_ot_file))
        elif ввод == "я сдаюсь":
            print("ПРАВИЛЬНЫЙ ПАРОЛЬ БЫЛ: ", parol_ot_file)
            print("ПРОГРАММА ЗАВЕРШЕННА")
            break
        else:  # неправильный пароль
            print("пароль ", ввод, " не правильный")
    except:
        print("ошибка ввода")
        parol_ot_file.close()
        print("ПРОГРАММА ЗАВЕРШЕННА")

