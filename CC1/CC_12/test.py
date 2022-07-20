from faker import Faker

my_faker = Faker(["lt_LT"])
for _ in range(10):
    print(my_faker.name())
