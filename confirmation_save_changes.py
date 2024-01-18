def confirmation_save_changes_func(exit_flag):        
    if exit_flag:
        # сделать чтобы определяло есть ли в буфере что-то
        while True:
            save_changes = input("Хотите ли сохранить изменения, если нажмете (+) ДА, (-) НЕТ: ") 
            if(save_changes == '+'):
                return True
            elif(save_changes == '-'):
                return False
            else:
                print("Нету такой команды! Нажмите + или -")

            # break Выход из внешнего цикла при установленном флаге
    else:
        return False
