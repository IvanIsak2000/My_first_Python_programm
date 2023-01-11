print('CHECK PASSWORD')
print("""Instruction:
1) You must enter the correct password!
2) Functions: print'exit' for exit, 'hint' for hint, 'surrender' for programm exit """)
parol_ot_file = "1"

while True:  # цикл проверки введёного кода с кодом
    try:
        user_input = str(input("введите пароль/write password: "))
        if user_input == "exit":  # выход
            print("exit!")
            z = input("PRESS FOR EXIT")
            break
            parol_ot_file.close()
        elif user_input == parol_ot_file:  # правильынй пароль
            print("ALL DONE")
            z = input("PRESS FOR EXIT")
            break
        elif user_input == "hint":
            print("Password lenght", len(parol_ot_file))
        elif user_input == "surrender":
            print("Right password was ", parol_ot_file)
            z = input("PRESS FOR EXIT")
            break
        else:  # неправильный пароль
            print("Password ", user_input, " not right")
    except:
        print("WRITE ERROR!")
