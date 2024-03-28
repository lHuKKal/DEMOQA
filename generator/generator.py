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
