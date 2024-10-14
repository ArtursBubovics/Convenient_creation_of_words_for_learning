def get_an_empty_field(ws):
    last_row_excel = ws.range('A1').end('down').row

    has_empty_fields = False

    for excel_row in range(2, last_row_excel + 1):
        empty_fields = [
            ws.cells(excel_row, col).value is None or ws.cells(excel_row, col).value == ''
            for col in range(3, 9)
        ]

        if any(empty_fields):
            print('Found an empty field')
            has_empty_fields = True 
            print('excel_row:' + str(excel_row))
            return (excel_row, 4)

    if not has_empty_fields:
        print('No empty fields found. Returning next row after the last filled row.')
        print('last_row_excel:' + str(last_row_excel+1))
        return (last_row_excel + 1, 4)
    return None