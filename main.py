import sys
import openpyxl

def get_list_of_sheets(path: str) -> list:
    workbook = openpyxl.load_workbook(path)
    return workbook.sheetnames # получем список имен листов .xlsx файла

def main():
    path = sys.argv[1]
    print(get_list_of_sheets(path))


if __name__ == '__main__':
    main()