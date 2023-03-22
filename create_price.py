import sys
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import PatternFill, Border, Side
from openpyxl.worksheet.worksheet import Worksheet
from PIL.PngImagePlugin import PngImageFile
from data_model import PriceItem, WarehouseItem, ShopItem, warehouse_title_line
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

def new_paint_cell(ws: Worksheet,
                   title_line: WarehouseItem,
                   row: int,
                   column: int) -> None:
    
    warehouse_column = title_line.index('01.Склад')
    shop1_column = title_line.index('02.ЦЧК')
    shop2_column = title_line.index('03.Дом Чая')
    shop3_column = title_line.index('04.Аллея')

    if column == warehouse_column:
        ws.cell(row=row, column=column).fill = PatternFill('solid',
                                                           start_color='C4D79B')
    elif column == shop1_column:
        ws.cell(row=row, column=column).fill = PatternFill('solid',
                                                           start_color='92CDDC')
    elif column == shop2_column:
        ws.cell(row=row, column=column).fill = PatternFill('solid',
                                                           start_color='FABF8F')
    elif column == shop3_column:
        ws.cell(row=row, column=column).fill = PatternFill('solid',
                                                           start_color='95B3D7')


def create_price(prepared_price: list[WarehouseItem]) -> None:
    wb = Workbook()
    ws = wb.active

    # warehouse_column = prepared_price[0].index('01.Склад')
    # shop1_column = prepared_price[0].index('02.ЦЧК')
    # shop2_column = prepared_price[0].index('03.Дом Чая')
    # shop3_column = prepared_price[0].index('04.Аллея')


    for item_number, item in enumerate(prepared_price, 1):
        for field_number, field in enumerate(item, 1):

            print_border(ws, row=item_number, column=field_number)
            new_paint_cell(ws=ws, title_line=prepared_price[0],
                           row=item_number, column=field_number)

            # if field_number == warehouse_column:
                # paint_cell(ws, row=item_number, column=field_number, color='C4D79B')
            # elif field_number == shop1_column:
                # paint_cell(ws, row=item_number, column=field_number, color='92CDDC')
            # elif field_number == shop2_column:
                # paint_cell(ws, row=item_number, column=field_number, color='FABF8F')
            # elif field_number == shop3_column:
                # paint_cell(ws, row=item_number, column=field_number, color='95B3D7')

            if isinstance(field, PngImageFile):
                ws.row_dimensions[item_number].height = 56 
                anchor = ws.cell(row=item_number, column=field_number).coordinate
                ws.add_image(Image(field), anchor=anchor)
            else:
                ws.cell(row=item_number, column=field_number).value = field

    ws.column_dimensions['A'].width = 90 #TODO: тут нужно сделать autofit для всех колонок
    wb.save('baza.xlsx')


def main() -> None:
    path = sys.argv[1]
    data = get_data_from_xlsx(path)
    prepared_price = prepare_price(data=data, mode='warehouse')
    create_price(prepared_price)


if __name__ == '__main__':
    main()
