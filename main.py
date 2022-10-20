from os.path import exists
from CSV import creating
from write_file import writing_scv
from write_file import writing_txt

path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()