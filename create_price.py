import sys
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import PatternFill, Border, Side
from openpyxl.styles.colors import Color
from openpyxl.worksheet.worksheet import Worksheet
from PIL.PngImagePlugin import PngImageFile
from data_model import PriceItem, WarehouseItem, ShopItem, warehouse_title_line
from get_data_from_xlsx import get_data_from_xlsx


def prepare_price(data:list[PriceItem], mode: str) -> list[tuple]:
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


def paint_column(ws: Worksheet) -> None:
    for row in enumerate(ws.iter_rows(min_col=1, max_col=ws.max_column, max_row=ws.max_row)):
        for column_number, cell in enumerate(row, 1):
            # cell.border = Border(top=Side(border_style='thin', color='000000'),
            #                      left=Side(border_style='thin', color='000000'),
            #                      right=Side(border_style='thin', color='000000'),
            #                      bottom=Side(border_style='thin', color='000000')
            #                      )
            if column_number == 3:
                cell.fill = PatternFill("solid", start_color="C4D79B")
            elif column_number == 4:
                cell.fill = PatternFill("solid", start_color="92CDDC")
            elif column_number == 5:
                cell.fill = PatternFill("solid", start_color="FABF8F")
            elif column_number == 6:
                cell.fill = PatternFill("solid", start_color="95B3D7")



def print_border(ws: Worksheet, row:int, column: int) -> None:
    ws.cell(row=row, column=column).border = Border(top=Side(border_style='thin', color='000000'),
                                                                  left=Side(border_style='thin', color='000000'),
                                                                  right=Side(border_style='thin', color='000000'),
                                                                  bottom=Side(border_style='thin', color='000000')
                                                                  )

def create_price(prepared_price:list[tuple]) -> None:
    wb = Workbook()
    ws = wb.active
    for item_number, item in enumerate(prepared_price, 1):
        for field_number, field in enumerate(item, 1):
            print_border(ws, row=item_number, column=field_number )
            if isinstance(field, PngImageFile):
                ws.row_dimensions[item_number].height = 56 
                anchor = ws.cell(row=item_number, column=field_number).coordinate
                ws.add_image(Image(field), anchor=anchor)
            else:
                ws.cell(row=item_number, column=field_number).value = field
    ws.column_dimensions['A'].width = 90 #TODO: тут нужно сделать autofit для всех колонок
    paint_column(ws)
    wb.save('baza.xlsx')


def main() -> None:
    path = sys.argv[1]
    data = get_data_from_xlsx(path)
    prepared_price = prepare_price(data=data, mode='warehouse')
    create_price(prepared_price)


if __name__ == '__main__':
    main()
