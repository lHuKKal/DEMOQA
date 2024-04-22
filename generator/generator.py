import base64
import calendar
import os
import random
import datetime

from data.data import Person, Date
from faker import Faker

faker_ru = Faker("ru_RU")
faker_en = Faker("En")


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
        mobile=faker_ru.random_int(min=1000000000, max=9999999999),
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


def subject_keys():
    subject_values = {
        "Hindi": 'Hindi',
        "English": 'English',
        "Maths": 'Maths',
        "Physics": 'Physics',
        "Chemistry": 'Chemistry',
        "Biology": 'Biology',
        "Computer Science": 'Computer Science',
        "Commerce": 'Commerce',
        "Accounting": 'Accounting',
        "Economics": 'Economics',
        "Arts": 'Arts',
        "Social Studies": 'Social Studies',
        "History": 'History',
        "Civics": 'Civics',
    }
    return subject_values


def get_states_and_cities():
    """Штаты и города"""
    states_and_cities = {
        "NCR": ["Delhi", "Gurgaon", "Noida"],
        "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
        "Haryana": ["Panipat", "Karnal"],
        "Rajasthan": ["Jaipur", "Jaiselmer"]
    }
    return states_and_cities


def multiple_color():
    multiple_color_key = {

        "Red": "Red",
        "Blue": "Blue",
        "Green": "Green",
        "Yellow": "Yellow",
        "Purple": "Purple",
        "Black": "Black",
        "White": "White",
        "Voilet": "Voilet",
        "Indigo": "Indigo",
        "Magenta": "Magenta",
        "Aqua": "Aqua"
    }
    return multiple_color_key


def generate_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time="12:00"
    )


def random_year_between_five_years():
    random_date = faker_en.date_time_between(start_date='-5y', end_date='+5y')
    random_year = random_date.year
    random_month = random_date.month
    random_day = random_date.day

    return str(random_year), str(random_month), str(random_day)


def select_random_not_current_year_and_month():
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month

    random_month = random.randint(1, 12)

    while random_month == current_month:
        random_month = random.randint(1, 12)

    # Используется только для теста где необходимо передать наименования месяца
    # А так, можно использовать просто random_month
    not_current_month_name = calendar.month_name[random_month]

    not_current_year = current_year - random.randint(1, 5)

    return not_current_month_name, str(not_current_year)


def not_today_day():
    today = datetime.datetime.now().day
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month

    total_days = calendar.monthrange(current_year, current_month)[1]
    random_day = random.randint(1, total_days)

    while random_day == today:
        random_day = random.randint(1, total_days)

    return str(random_day)

