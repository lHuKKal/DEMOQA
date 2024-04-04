import base64
import os
import random

from data.data import Person
from faker import Faker

faker_ru = Faker("ru_RU")


def generate_person():
    """Генератор случайных данных для теста"""
    yield Person(
        full_name=faker_ru.name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        age=faker_ru.random_int(min=1, max=99),
        salary=faker_ru.random_int(min=1000, max=999999),
        departament=faker_ru.job(),
    )


def generate_file():
    # указываем директорию, откуда запускается скрипт
    current_directory = os.getcwd()
    file_name = f"filetest{random.randint(0, 999)}.txt"
    # Функция os.path.join() используется для объединения текущего рабочего каталога и имени файла,
    # чтобы создать полный путь к файлу
    path = os.path.join(current_directory, file_name)
    # Открывается файл с использованием open() в режиме записи и чтения ('w+').
    # Использование ключевого слова with гарантирует правильное закрытие файла после выполнения блока кода
    with open(path, 'w+') as file:
        file.write(f"Hello world {random.randint(0, 999)}")
    return file_name, path


def generate_jpeg(link):
    # указываем директорию, откуда запускается скрипт
    current_directory = os.getcwd()
    link_b = base64.b64decode(link)
    file_name = f"filetest{random.randint(0, 999)}.jpg"
    # Функция os.path.join() используется для объединения текущего рабочего каталога и имени файла,
    # чтобы создать полный путь к файлу
    path = os.path.join(current_directory, file_name)
    # Открывается файл с использованием open() в режиме записи и чтения ('w+').
    # Использование ключевого слова with гарантирует правильное закрытие файла после выполнения блока кода
    with open(path, 'wb+') as file:
        offset = link_b.find(b'\xff\xd8')
        file.write(link_b[offset:])
        check_file = os.path.exists(path)
    os.remove(path)
    return check_file
