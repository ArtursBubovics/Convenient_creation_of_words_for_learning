import xlwings as xw
from create_set_and_insert_data_in_dictionary.Insert_data_in_Excel.get_an_empty_field.get_an_empty_field import get_an_empty_field
from openpyxl.styles import Border, Side
from datetime import datetime
def inset_data_in_excel(wb, ws, usageRate, partOfSpeech, words, transcription, word_meaning, use_cases, russian_meaning):
    
    # Выводим отладочную информацию
    print("Looking for empty fields to fill in new fields")

    EMPTY_FIELD = get_an_empty_field(ws)

    lastUsedDate = datetime.today().strftime("%d.%m.%Y")

    row, col = EMPTY_FIELD
    # Заполняем значения в Excel
    ws.range((row, 1)).value = row - 1
    ws.range((row, 2)).value = usageRate
    ws.range((row, 3)).value = 0
    ws.range((row, 4)).value = lastUsedDate
    ws.range((row, 5)).value = partOfSpeech
    ws.range((row, 6)).value = words
    ws.range((row, 7)).value = transcription
    ws.range((row, 8)).value = word_meaning
    ws.range((row, 9)).value = ' ; '.join(use_cases)
    ws.range((row, 10)).value = russian_meaning

    # Заполняем цвета ячеек
    ws.range((row, 3)).color = (255, 0, 0)
    ws.range((row, 2)).color = (0, 176, 80)

    ws.range((row, 1), (row, 10)).api.HorizontalAlignment = xw.constants.HAlign.xlHAlignCenter


    range_to_border = ws.range((row, 1), (row, 10))

    for border in [
        xw.constants.BordersIndex.xlEdgeBottom,
        xw.constants.BordersIndex.xlEdgeTop,
        xw.constants.BordersIndex.xlEdgeLeft,
        xw.constants.BordersIndex.xlEdgeRight,
        xw.constants.BordersIndex.xlInsideVertical,
        xw.constants.BordersIndex.xlInsideHorizontal,
    ]:
        range_to_border.api.Borders(border).LineStyle = 4
        range_to_border.api.Borders(border).Weight = 1 



    wb.save(r'C:\Users\papar\Desktop\Dictionary_English.xlsx')
    print('\nEverything saved correctly!')