import sys
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from PIL.PngImagePlugin import PngImageFile
from data_model import DataRow
from get_data_from_xlsx import get_data_from_xlsx

def create_warehouse_price(data:list[DataRow]) -> None:
    wb = Workbook()
    ws = wb.active
    for row_number, row in enumerate(data, 1):
        ws.column_dimensions['A'].width = 90 #TODO: тут нужно сдеать autofit для всех колонок
        if row.img is None:
            ws.append(row)
        else:
            for column_number, cell in enumerate(row, 1):
                ws.row_dimensions[row_number].height = 56 
                if isinstance(cell, PngImageFile):
                    ws.add_image(Image(cell), anchor='H'+str(row_number))
                else:
                    ws.cell(row=row_number, column=column_number).value = cell
    
    wb.save('baza.xlsx')


def main() -> None:
    path = sys.argv[1]
    data = get_data_from_xlsx(path)
    create_warehouse_price(data)


if __name__ == '__main__':
    main()
