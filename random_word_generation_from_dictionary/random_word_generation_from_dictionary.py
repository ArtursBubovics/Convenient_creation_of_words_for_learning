import random
import pyttsx3

def random_word_generation_from_dictionary(wb, ws):
        generate_word = True
        last_row_excel = ws.range('A2').end('down').row

        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

        engine.setProperty('voice', voices[1].id)

        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 50) 

        while generate_word:
            if last_row_excel < 2:
                print("Нет доступных слов для генерации")
                break

            row_value = random.randint(2, last_row_excel)
            generated_word = ws.range((row_value, 4)).value
            generated_transcription = ws.range((row_value, 5)).value
            
            print('\n---------------------------------------------\n')
            print(f"\n\nВот сгенерированое слово: \033[92m{generated_word}\033[0m")
            print(f"\n\nВот транскрипция: \033[92m{generated_transcription}\033[0m")
            engine.say(generated_word)
            engine.runAndWait()

            word_processing = input('\n\n1)Хотите прослушать еще?\nДа это + ; Нет это - ;  Выберите действие: ')

            if(word_processing == '+'):
                 while True:
                    engine.say(generated_word)
                    engine.runAndWait()
                    repeat_word_processing = input('\n\nХотите прослушать еще?\nДа это + ; Нет это - ;  Выберите действие: ')
                    if(repeat_word_processing == '+'):
                        continue
                    else:
                        break

            show_addinal_fields = input('\n\n2)Хотите посмотреть дополнение к этому слову?\nДа это + ; Нет это - ;  Выберите действие: ')

            if(show_addinal_fields == '+'):
                print("\nВот дополнение: ")
                for col in range(6, 9):
                     print("\n* " + ws.range((row_value, col)).value)
                     

            user_response = input('\n3)Дальше генерировать?\nДа это + ; Нет это - ;  Выберите действие: ')

            if(user_response == '-'):
                if(input('\nХотите сохранить изменения?\nДа это + ; Нет это - ; Выберите действие: ') == '+'):
                    current_value = ws.range((row_value, 3)).value
                    ws.range((row_value, 3)).value = (current_value or 0) + 1
                    wb.save(r'C:\Users\papar\Desktop\Dictionary_English.xlsx')
                    break
                else:
                    break
            else:
                current_value = ws.range((row_value, 3)).value
                ws.range((row_value, 3)).value = (current_value or 0) + 1
                wb.save(r'C:\Users\papar\Desktop\Dictionary_English.xlsx')