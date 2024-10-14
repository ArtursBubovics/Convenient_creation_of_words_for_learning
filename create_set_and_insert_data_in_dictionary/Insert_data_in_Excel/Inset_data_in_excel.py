import xlwings as xw
from create_set_and_insert_data_in_dictionary.Insert_data_in_Excel.get_an_empty_field.get_an_empty_field import get_an_empty_field

def inset_data_in_excel(wb, ws, words, transcription, word_meaning, use_cases, russian_meaning):
    
    # Выводим отладочную информацию
    print("Looking for empty fields to fill in new fields")

    EMPTY_FIELD = get_an_empty_field(ws)


    row, col = EMPTY_FIELD
    # Заполняем значения в Excel
    ws.range((row, 1)).value = row - 2
    ws.range((row, 3)).value = 0
    ws.range((row, 4)).value = words
    ws.range((row, 5)).value = transcription
    ws.range((row, 6)).value = word_meaning
    ws.range((row, 7)).value = ' ; '.join(use_cases)
    ws.range((row, 8)).value = russian_meaning

    # Заполняем цвета ячеек
    ws.range((row, 3)).color = (255, 0, 0)
    ws.range((row, 2)).color = (0, 176, 80)

    ws.range((row, 1), (row, 8)).api.HorizontalAlignment = xw.constants.HAlign.xlHAlignCenter

    wb.save(r'C:\Users\papar\Desktop\Dictionary_English.xlsx')
    print('\nEverything saved correctly!')