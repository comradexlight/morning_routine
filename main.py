import sys
import openpyxl
from openpyxl_image_loader import SheetImageLoader
from datarow import DataRow


def get_list_of_sheets(path: str) -> list:
    workbook = openpyxl.load_workbook(path)
    image_loader = SheetImageLoader(workbook.active)
    # return workbook.sheetnames # получем список имен листов .xlsx файла
    column_img = workbook.active['N']
    for cell in column_img:
        if image_loader.image_in(cell):
            print("Got it!")


def main():
    path = sys.argv[1]
    print(get_list_of_sheets(path))


if __name__ == '__main__':
    main()