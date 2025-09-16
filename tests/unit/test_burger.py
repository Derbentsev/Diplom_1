from textwrap import dedent

from helpers.helpers import Helpers


class TestBurger:
    #Успешное добавление булочки
    def test_set_buns_success(self):
        burger = Helpers.create_new_burger()
        bun = Helpers.create_bun('Булочка', 150.3)

        burger.set_buns(bun)
        assert burger.bun == bun


    #Успешное добавление ингредиента
    def test_add_ingredient_success(self):
        burger = Helpers.create_new_burger()

        ingredient_1 = Helpers.create_ingredient('Начинка', 'Джем', 50)
        ingredient_2 = Helpers.create_ingredient('Соус', 'Чесночный', 120)

        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        assert burger.ingredients == [ingredient_1, ingredient_2]


    #Успешное удаление ингредиента
    def test_remove_ingredient_success(self):
        burger = Helpers.create_new_burger()

        ingredient_1 = Helpers.create_ingredient('Начинка', 'Джем', 50)
        ingredient_2 = Helpers.create_ingredient('Соус', 'Чесночный', 120)

        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.remove_ingredient(1)

        assert burger.ingredients == [ingredient_1]


    #Успешная замена местами ингредиентов в рецепте
    def test_move_ingredient_success(self):
        burger = Helpers.create_new_burger()

        ingredient_1 = Helpers.create_ingredient('Начинка', 'Джем', 50)
        ingredient_2 = Helpers.create_ingredient('Соус', 'Чесночный', 120)

        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients == [ingredient_2, ingredient_1]

    
    #Успешное получение цены у рецепта
    def test_get_price_success(self):
        bun_price = 200
        ingredient_1_price = 50
        ingredient_2_price = 120

        burger = Helpers.create_new_burger()
        bun = Helpers.create_bun('Булочка', bun_price)

        ingredient_1 = Helpers.create_ingredient('Начинка', 'Джем', ingredient_1_price)
        ingredient_2 = Helpers.create_ingredient('Соус', 'Чесночный', ingredient_2_price)

        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        assert burger.get_price() == bun_price * 2 + ingredient_1_price + ingredient_2_price


    #Успешное получение текста рецепта
    def test_get_receipt_success(self):
        bun_price = 200
        ingredient_1_price = 50
        ingredient_2_price = 120

        total_price = bun_price * 2 + ingredient_1_price + ingredient_2_price

        receipt_text = dedent(f"""\
        (==== Булочка ====)
        = начинка Джем =
        = соус Чесночный =
        (==== Булочка ====)\n
        Price: {total_price}"""
        )

        burger = Helpers.create_new_burger()
        bun = Helpers.create_bun('Булочка', 200)

        ingredient_1 = Helpers.create_ingredient('Начинка', 'Джем', 50)
        ingredient_2 = Helpers.create_ingredient('Соус', 'Чесночный', 120)

        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        assert burger.get_receipt() == receipt_text
