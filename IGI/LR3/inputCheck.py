def input_check(prompt, input_type, condition=lambda x: True):
    while True:
        try:
            user_input = input_type(input(prompt))
            if condition(user_input):
                return user_input
            else:
                print("Некорректный ввод, попробуйте еще раз: ")
        except ValueError:
            print(f"Пожалуйста, введите значение типа {input_type.__name__}.")