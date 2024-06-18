BLUE_COLOR = (0, 112, 192)  # RGB для синего цвета

def get_an_empty_field(ws, df):

    # Проход по каждой строке в DataFrame
    for index, row in df.iterrows():
        excel_row = index + 2  # +2 для учета заголовков и начальной строки

        # Ищем ячейку, указывающую на то, что места для ввода больше нет
        is_in_cards_column = 2  # Индекс столбца 'Is in cards'

        is_in_cards_cell = ws.cells(excel_row, is_in_cards_column)

        if cell_color_determination(is_in_cards_cell, BLUE_COLOR):
            print("There are no further fields to enter")
            return None
        else:
            # Проверяем, есть ли заполнение у текущей ячейки
            if cell_has_no_fill(is_in_cards_cell):
                if (ws.cells(excel_row, 3).value is None or ws.cells(excel_row, 3).value == '' or
                    ws.cells(excel_row, 4).value is None or ws.cells(excel_row, 4).value == '' or
                    ws.cells(excel_row, 5).value is None or ws.cells(excel_row, 5).value == '' or
                    ws.cells(excel_row, 6).value is None or ws.cells(excel_row, 6).value == '' or
                    ws.cells(excel_row, 7).value is None or ws.cells(excel_row, 7).value == '' or
                    ws.cells(excel_row, 8).value is None or ws.cells(excel_row, 8).value == ''):
                    
                    print('Found an empty field')
                    return (excel_row, 4)
                else:
                    continue
            else:
                continue
    return None

def cell_color_determination(cell, color):
    # Проверяем цвет ячейки
    fill_color = cell.color
    return fill_color == color

def cell_has_no_fill(cell):
    # Проверяем, пустая ли ячейка
    return cell.color is None