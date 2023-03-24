import sys
from datetime import datetime
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import PatternFill, Border, Side
from openpyxl.worksheet.worksheet import Worksheet
from PIL.PngImagePlugin import PngImageFile
from data_model import PriceItem, WarehouseItem, ShopItem, warehouse_title_line, shop_title_line
from get_data_from_xlsx import get_data_from_xlsx


def prepare_price(data:list[PriceItem], mode: str) -> list[WarehouseItem]:
    prepared_price = []
    match mode:
        case 'warehouse':
            prepared_price.append(warehouse_title_line)
            for item in data:   
                prepared_price.append(
                    WarehouseItem(
                    title=item.title,
                    warehouse_price=item.warehouse_price,
                    quantity_warehouse=item.quantity_warehouse,
                    quantity_shop1 = item.quantity_shop1,
                    quantity_shop2 = item.quantity_shop2,
                    quantity_shop3 = item.quantity_shop3,
                    img=item.img
                    )
                    )
        case 'shop':
            prepared_price.append(shop_title_line)
            for item in data:
                prepared_price.append(
                    ShopItem(
                    title=item.title,
                    shop_price=item.shop_price,
                    quantity_shop1 = item.quantity_shop1,
                    quantity_warehouse=item.quantity_warehouse,
                    quantity_shop2 = item.quantity_shop2,
                    quantity_shop3 = item.quantity_shop3,
                    img=item.img
                    )
                    )
        case 'small':
            for item in data:
                prepared_price.append(
                    ShopItem(
                    title=item.title,
                    shop_price=item.warehouse_price,
                    quantity_shop1 = item.quantity_shop1,
                    quantity_warehouse=item.quantity_warehouse,
                    quantity_shop2 = item.quantity_shop2,
                    quantity_shop3 = item.quantity_shop3,
                    img=item.img
                    )
                    )
    return prepared_price


def paint_cell(ws: Worksheet, row: int, column: int, color: str) -> None:
    ws.cell(row=row, column=column).fill = PatternFill('solid', start_color=color)


def print_border(ws: Worksheet, row: int, column: int) -> None:
    ws.cell(row=row, column=column).border = Border(top=Side(border_style='thin', color='000000'),
                                                    left=Side(border_style='thin', color='000000'),
                                                    right=Side(border_style='thin', color='000000'),
                                                    bottom=Side(border_style='thin', color='000000')
                                                    )


def create_price(prepared_price: list[tuple], name) -> None:
    wb = Workbook()
    ws = wb.active

    warehouse_column = prepared_price[0].index('01.Склад') + 1
    shop1_column = prepared_price[0].index('02.ЦЧК') + 1
    shop2_column = prepared_price[0].index('03.Дом Чая') + 1
    shop3_column = prepared_price[0].index('04.Аллея') + 1


    for item_number, item in enumerate(prepared_price, 1):
        for field_number, field in enumerate(item, 1):

            print_border(ws, row=item_number, column=field_number)

            if field_number == warehouse_column:
                paint_cell(ws, row=item_number, column=field_number, color='C4D79B')
            elif field_number == shop1_column:
                paint_cell(ws, row=item_number, column=field_number, color='92CDDC')
            elif field_number == shop2_column:
                paint_cell(ws, row=item_number, column=field_number, color='FABF8F')
            elif field_number == shop3_column:
                paint_cell(ws, row=item_number, column=field_number, color='95B3D7')

            if isinstance(field, PngImageFile):
                ws.row_dimensions[item_number].height = 56 
                anchor = ws.cell(row=item_number, column=field_number).coordinate
                ws.add_image(Image(field), anchor=anchor)
            else:
                ws.cell(row=item_number, column=field_number).value = field

    ws.column_dimensions['A'].width = 90 #TODO: тут нужно сделать autofit для всех колонок
    wb.save(name)


def main() -> None:
    date = datetime.now().strftime('%Y_%m_%d')
    path = sys.argv[1]
    data = get_data_from_xlsx(path)
    mode = sys.argv[2]
    prepared_price = prepare_price(data=data, mode=mode)
    name = f'{mode}_{date}.xlsx'
    create_price(prepared_price, name)


if __name__ == '__main__':
    main()
