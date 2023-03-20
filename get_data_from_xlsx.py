import sys
import openpyxl
from typing import Union
from openpyxl.cell.cell import Cell
from openpyxl_image_loader import SheetImageLoader
from PIL.PngImagePlugin import PngImageFile
from data_model import PriceItem


def _get_price(cell:int) -> Union[int, None]:
    if isinstance(cell, int):
        return cell
    return None


def _get_quantity(cell: int) -> float:
    if isinstance(cell, int):
        return float(cell)
    elif isinstance(cell, float):
        return cell
    return 0.0


def _get_image(image_loader: SheetImageLoader, cell: Cell) -> Union[PngImageFile, None]:
    if image_loader.image_in(cell.coordinate):
        return image_loader.get(cell.coordinate)
    

def get_data_from_xlsx(path: str) -> list[PriceItem]:
    workbook = openpyxl.load_workbook(path)
    image_loader = SheetImageLoader(workbook.active)
    worksheet = workbook.active
    row_list = []
    for row in worksheet:
        if row[4].value != None and row[4].value != 'Номенклатура, Характеристика, Упаковка':
            row_list.append(
                            PriceItem(
                                title = row[4].value,
                                purchase_price = _get_price(row[14].value),
                                large_wholesale_price = _get_price(row[15].value),
                                medium_wholesale_price = _get_price(row[16].value),
                                small_wholesale_price = _get_price(row[17].value),
                                warehouse_price = _get_price(row[18].value), 
                                shop_price =_get_price(row[19].value),
                                quantity_warehouse = _get_quantity(row[20].value),
                                quantity_shop1 = _get_quantity(row[22].value),
                                quantity_shop2 = _get_quantity(row[24].value),
                                quantity_shop3 = _get_quantity(row[26].value),
                                img = _get_image(image_loader, row[13]), 
                                secret_warehouse = _get_quantity(row[28].value)
                                )
                            )
    return row_list


def main():
    path = sys.argv[1]
    print(get_data_from_xlsx(path))


if __name__ == '__main__':
    main()
