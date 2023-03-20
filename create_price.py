import sys
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from PIL.PngImagePlugin import PngImageFile
from data_model import PriceItem, WarehouseItem, ShopItem
from get_data_from_xlsx import get_data_from_xlsx


def prepare_price(data:list[PriceItem], mode: str) -> list[tuple]:
    prepared_price = []
    match mode:
        case 'warehouse':
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
    return prepared_price


def create_warehouse_price(data:list[PriceItem]) -> None:
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
    print(prepare_price(data=data, mode='shop'))
    # create_warehouse_price(data)


if __name__ == '__main__':
    main()
