import shutil
import os


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


m_list = open("modules.txt").readlines()


for module in m_list:
    file_name = module.rstrip()
    source = ("C:\\Users\\Piotr\\OneDrive\\Dokumenty\\NG REPORT\\photos\\all\\")
    destination = "C:\\Users\\Piotr\\OneDrive\\Dokumenty\\NG REPORT\\photos\\202208_PIN_NG"
    test = find(file_name, source)
    if test is not None:
        file_path = source + file_name
        weight = os.path.getsize(file_path)
        if weight <= 1761:
            os.remove(file_path)
        else:
            shutil.copy(file_path, destination)
    else:
        print("Plik - " + file_name + " - nie został znaleziony.")