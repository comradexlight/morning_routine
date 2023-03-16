import sys
import openpyxl
# from openpyxl_image_loader import SheetImageLoader
from datarow import DataRow


def get_data_from_xlsx(path: str) -> list[DataRow]:
    workbook = openpyxl.load_workbook(path)
    # image_loader = SheetImageLoader(workbook.active)
    # return workbook.sheetnames # получем список имён листов .xlsx файла
    # column_img = workbook.active['N']
    worksheet = workbook.active
    for row in worksheet:
        print('title:', row[4].value)
        print('warehouse_price:', row[18].value)
        print('store_price:', row[19].value)
        print('quantity_warehouse:', row[20].value)
        print('quantity_store1:', row[22].value)
        print('quantity_store2:', row[24].value)
        print('quantity_store3:', row[26].value)
        print('quantity_secret:', row[26].value) 


def main():
    path = sys.argv[1]
    print(get_data_from_xlsx(path))


if __name__ == '__main__':
    main()
