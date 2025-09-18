from textwrap import dedent

from helpers.helpers import Helpers
from data.data import Data


class TestBurger:
    #Успешное добавление булочки
    def test_set_buns_success(self):
        bun_data = Data.BUN_DATA

        burger = Helpers.create_new_burger()
        bun = Helpers.create_bun(bun_data['name'], bun_data['price'])

        burger.set_buns(bun)
        assert burger.bun == bun


    #Успешное добавление ингредиента
    def test_add_ingredient_success(self):
        ingredient_data_1 = Data.INGREDIENT_DATA[0]
        ingredient_data_2 = Data.INGREDIENT_DATA[1]

        burger = Helpers.create_new_burger()

        ingredient_1 = Helpers.create_ingredient(
            ingredient_data_1['type'],
            ingredient_data_1['name'],
            ingredient_data_1['price']
        )

        ingredient_2 = Helpers.create_ingredient(
            ingredient_data_2['type'],
            ingredient_data_2['name'],
            ingredient_data_2['price']
        )

        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        assert burger.ingredients == [ingredient_1, ingredient_2]


    #Успешное удаление ингредиента
    def test_remove_ingredient_success(self):
        ingredient_data_1 = Data.INGREDIENT_DATA[0]
        ingredient_data_2 = Data.INGREDIENT_DATA[1]
    
        burger = Helpers.create_new_burger()

        ingredient_1 = Helpers.create_ingredient(
            ingredient_data_1['type'],
            ingredient_data_1['name'],
            ingredient_data_1['price']
        )

        ingredient_2 = Helpers.create_ingredient(
            ingredient_data_2['type'],
            ingredient_data_2['name'],
            ingredient_data_2['price']
        )

        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.remove_ingredient(1)

        assert burger.ingredients == [ingredient_1]


    #Успешная замена местами ингредиентов в рецепте
    def test_move_ingredient_success(self):
        ingredient_data_1 = Data.INGREDIENT_DATA[0]
        ingredient_data_2 = Data.INGREDIENT_DATA[1]
        burger = Helpers.create_new_burger()

        ingredient_1 = Helpers.create_ingredient(
            ingredient_data_1['type'],
            ingredient_data_1['name'],
            ingredient_data_1['price']
        )

        ingredient_2 = Helpers.create_ingredient(
            ingredient_data_2['type'],
            ingredient_data_2['name'],
            ingredient_data_2['price']
        )

        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients == [ingredient_2, ingredient_1]


    #Успешное получение цены у рецепта
    def test_get_price_success(self):
        bun_data = Data.BUN_DATA
        ingredient_data_1 = Data.INGREDIENT_DATA[0]
        ingredient_data_2 = Data.INGREDIENT_DATA[1]

        burger = Helpers.create_new_burger()
        bun = Helpers.create_bun(bun_data['name'], bun_data['price'])

        ingredient_1 = Helpers.create_ingredient(
            ingredient_data_1['type'],
            ingredient_data_1['name'],
            ingredient_data_1['price']
        )

        ingredient_2 = Helpers.create_ingredient(
            ingredient_data_2['type'],
            ingredient_data_2['name'],
            ingredient_data_2['price']
        )

        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        assert burger.get_price() == (bun_data['price'] * 2 +
            ingredient_data_1['price'] + ingredient_data_2['price'])


    #Успешное получение текста рецепта
    def test_get_receipt_success(self):
        bun_data = Data.BUN_DATA
        ingredient_data_1 = Data.INGREDIENT_DATA[0]
        ingredient_data_2 = Data.INGREDIENT_DATA[1]

        total_price = (bun_data['price'] * 2 +
            ingredient_data_1['price'] + ingredient_data_2['price'])

        receipt_text = dedent(f"""\
        (==== Булочка ====)
        = начинка {ingredient_data_1['name']} =
        = соус {ingredient_data_2['name']} =
        (==== Булочка ====)\n
        Price: {total_price}"""
        )

        burger = Helpers.create_new_burger()
        bun = Helpers.create_bun(bun_data['name'], bun_data['price'])

        ingredient_1 = Helpers.create_ingredient(
            ingredient_data_1['type'],
            ingredient_data_1['name'],
            ingredient_data_1['price']
        )

        ingredient_2 = Helpers.create_ingredient(
            ingredient_data_2['type'],
            ingredient_data_2['name'],
            ingredient_data_2['price']
        )

        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        assert burger.get_receipt() == receipt_text
