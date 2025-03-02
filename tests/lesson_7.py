"""Work with open file"""

print("-----Work with open file ->-->--->--- --------- -----")

"""
'r'       open for reading (default)
'w'       open for writing, truncating the file first
'x'       create a new file and open it for writing
'a'       open for writing, appending to the end of the file if it exists
'b'       binary mode
't'       text mode (default)
'+'       open a disk file for updating (reading and writing)
"""
# pen('hello', 'w').write('Hello World')  # Так делать не ок
with open('../file_for_tests/hello') as file:
    print(file.read())
    print("------------- --------- -----")


"""Work with path"""
print("-----Work with path ->-->--->--- --------- -----")

import os

# abspath = os.path.abspath('hello')
# dirname = os.path.dirname(abspath)
# print(dirname)
# print("------------- --------- -----")
# print(os.path.abspath(__file__))

TEKUSH_FILE_PATH = os.path.abspath(__file__)
print(TEKUSH_FILE_PATH)
PROJECT_FILE_PATH = os.path.dirname(TEKUSH_FILE_PATH)
print(PROJECT_FILE_PATH)
OTHER_FILE_PATH = os.path.dirname(PROJECT_FILE_PATH)
print(OTHER_FILE_PATH)
with open('../file_for_tests/hello') as file:
    print(file.read())
print("-----join_path  ->-->--->--- --------- -----")

joinpath = os.path.join(OTHER_FILE_PATH, 'file_for_tests', 'hello')
print(joinpath)


"""Work with exists"""
print("-----Work with exists  ->-->--->--- --------- -----")

for_tests_path = os.path.join(OTHER_FILE_PATH, 'file_for_tests')
is_path_exists = os.path.exists(for_tests_path)
print(is_path_exists)

print("-----Create new folder ->-->--->--- --------- -----")

dir_for_tests_path = os.path.join(for_tests_path, 'new_dir_lesson6')
print(dir_for_tests_path)
is_path_exists = os.path.exists(dir_for_tests_path)
print(is_path_exists)
if not is_path_exists:
    os.mkdir('../file_for_tests/new_dir_lesson6')
    print('Created folder')


"""Work with csv"""
print("-----Work with csv ->-->--->--- --------- -----")

import csv

with open('../file_for_tests/2.5kb.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)

print("-----Created new csv ->-->--->--- --------- -----")
with open('../file_for_tests/new.csv', 'w') as csv_file:
    csvwriter = csv.writer(csv_file, delimiter=';')
    csvwriter.writerow(['test', 'test2', 'test3'])
    csvwriter.writerows(
        [
            ['name', 'phoneNumber', 'email'],
            ['Antom', '+79160000000', 'anton@mail.ru'],
            ['Alina', '+79030000000', 'alina@mail.ru'],
        ]
    )
with open('../file_for_tests/new.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)

"""Work with xls"""
print("-----Work with xls ->-->--->--- --------- -----")

import xlrd

book = xlrd.open_workbook('../file_for_tests/komunal.xls')

print(f'Кол-во листов: {book.nsheets}')
print(f'Имена листов: {book.sheet_names()}')
sheet = book.sheet_by_index(0)
print(f'Вывожу кол-во колонок: {sheet.ncols}')
print(f'Вывожу кол-во строк: {sheet.nrows}')
print(f'Пересечение строки и столбца {sheet.cell_value(rowx=0, colx=2)}')

# for rx in range(sheet.nrows):
#     print(sheet.row(rx))

"""Потом он рассказывал про xlsx но отличий там немного"""


"""Work with pdf"""
print("-----Work with pdf ->-->--->--- --------- -----")

import pypdf

reader = pypdf.PdfReader('../file_for_tests/test_pdf.pdf')
number_of_pages = len(reader.pages)
first_page = reader.pages[0]
text = first_page.extract_text()

# print(number_of_pages, '\n', first_page)
print(text)


"""Work with zip"""
print("-----Work with zip ->-->--->--- --------- -----")

import zipfile

zip_file = zipfile.ZipFile('../file_for_tests/test_files.zip')
print(zip_file.namelist())
text = zip_file.read('test.pdf')
print(text)
zip_file.close()

with zipfile.ZipFile('../file_for_tests/test_files.zip') as testzip:
    testzip.extract('test.pdf')

"""
1. Взять из материалов лекции только модули начинающиеся с test_,
 решить в них все TODO.
2. Создать новые тесты, которые заархивируют имеющиеся в resources
 различные типы файлов в один архив в tmp и проверят тестом в архиве 
 каждый из файлов, что он является тем самым, который был заархивирован,
 не распаковывая архив.
"""
