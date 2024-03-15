from data.data import Person
from faker import Faker

faker_ru = Faker("ru_RU")


def generated_person():
    yield Person(
        full_name=faker_ru.name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )
