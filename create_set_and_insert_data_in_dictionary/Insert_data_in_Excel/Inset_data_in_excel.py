from create_set_and_insert_data_in_dictionary.Insert_data_in_Excel.get_an_empty_field.get_an_empty_field import get_an_empty_field
from openpyxl.styles import PatternFill

def inset_data_in_excel(excel_file, df, workbook, worksheet, words, transcription, word_meaning, use_cases, russian_meaning):
    print('go2')
    EMPTY_FIELD = get_an_empty_field(excel_file, df, workbook, worksheet)

    
    # Заполняем значения в Excel
    worksheet.cell(row=EMPTY_FIELD.row, column=3).value = 0
    worksheet.cell(row=EMPTY_FIELD.row, column=4).value = words
    worksheet.cell(row=EMPTY_FIELD.row, column=5).value = transcription
    worksheet.cell(row=EMPTY_FIELD.row, column=6).value = word_meaning
    worksheet.cell(row=EMPTY_FIELD.row, column=7).value = ' ; '.join(use_cases)
    worksheet.cell(row=EMPTY_FIELD.row, column=8).value = russian_meaning

    red_fill = PatternFill(start_color='FF0000', end_color='FF0000', fill_type='solid')
    worksheet.cell(row=EMPTY_FIELD.row, column=3).fill = red_fill

    green_fill = PatternFill(start_color='00B050', end_color='00B050', fill_type='solid')
    worksheet.cell(row=EMPTY_FIELD.row, column=2).fill = green_fill
    print('\nEverything saved correctly!')
    # Сохраняем изменения
    workbook.save(excel_file)
