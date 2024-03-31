from datetime import datetime

from faker import Faker
from faker.generator import random

fake = Faker()

departments = ["IT", "Marketing", "Finance", "Sales", "HR", "Engineering"]

for _ in range(100):
    age = random.randint(18, 65)
    birthdate = fake.date_of_birth(minimum_age=age, maximum_age=age)
    formatted_birthdate = (datetime.now() - datetime(birthdate.year, birthdate.month, birthdate.day)).days // 365
    print(f'"FIRST_NAME": "{fake.name()}",')
    print(f'"LAST_NAME": "{fake.last_name()}",')
    print(f'"EMAIL": "{fake.email()}",')
    print(f'"AGE": {formatted_birthdate},')
    print(f'"SALARY": {fake.random_int(min=30000, max=100000, step=1000)},')
    print(f'"DEPARTMENT": "{random.choice(departments)}",')
    print("\n")