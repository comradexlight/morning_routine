import shutil
import os
from zipfile import ZipFile


def fix_1c_error(path: str) -> None:
# Создаем временную папку
    tmp_folder = '/tmp/convert_wrong_excel/'
    os.makedirs(tmp_folder, exist_ok=True)

    # Распаковываем excel как zip в нашу временную папку
    with ZipFile(path) as excel_container:
        excel_container.extractall(tmp_folder)

    # Переименовываем файл с неверным названием
    wrong_file_path = os.path.join(tmp_folder, 'xl', 'SharedStrings.xml')
    correct_file_path = os.path.join(tmp_folder, 'xl', 'sharedStrings.xml')
    os.rename(wrong_file_path, correct_file_path) 

    # Запаковываем excel обратно в zip и переименовываем в исходный файл
    shutil.make_archive(path, 'zip', tmp_folder)
    os.replace(f'{path}.zip', f'{path}')