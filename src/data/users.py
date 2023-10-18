from dataclasses import dataclass
import datetime
from strenum import StrEnum


class Hobby(StrEnum):
    SPORTS = "Sports"
    READING = "Reading"
    MUSIC = "Music"


@dataclass
class User:
    name: str
    last_name: str
    email: str
    gender: str
    number: str
    date_of_birth: datetime.date
    subjects: list
    hobbies: list
    address: str
    state: str
    city: str

    @property
    def date_of_birth_str(self):
        return self.date_of_birth.strftime("%d %B,%Y")

    @property
    def subjects_str(self):
        return ", ".join(self.subjects)

    @property
    def hobbies_str(self):
        return ", ".join(self.hobbies)

    def __str__(self):
        return self.name + " " + self.last_name


test_user = User(
    name="test_name",
    last_name="test_last_name",
    email="test@gmail.com",
    gender="Female",
    number="0123456789",
    date_of_birth=datetime.date(1942, 1, 1),
    subjects=["History", "Maths"],
    hobbies=[Hobby.READING, Hobby.MUSIC],
    address="Some-street, Some-house, Some-apartment",
    state="Haryana",
    city="Panipat"
)
