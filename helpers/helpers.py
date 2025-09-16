from faker import Faker

from burger import Burger
from bun import Bun
from ingredient import Ingredient


class Helpers:
    @staticmethod
    def create_new_burger() -> Burger:
        burger = Burger()
        return burger


    @staticmethod
    def create_bun(name: str, price: float) -> Bun:
        bun = Bun(name, price)
        return bun


    @staticmethod
    def create_ingredient(ingredient_type, name, price) -> Ingredient:
        ingredient = Ingredient(ingredient_type, name, price)
        return ingredient


    def create_user_data():
        faker = Faker()

        courier_data = {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.first_name()
        }

        return courier_data
