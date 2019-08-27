import unittest
import database


class MyTest(unittest.TestCase):
    def test_find_dish(self):
        self.assertEqual(database.find_dish(3).price, 3)
        self.assertEqual(database.find_dish(25), 'Dish not found!')

    def test_take_order(self):
        table1 = database.Table(1)
        table1.take_order(1, 2)
        self.assertEqual(table1.orders, {1: 2})
        self.assertEqual(table1.totalPrice, 6)

    def test_delete_order(self):
        table1 = database.Table(1)
        table1.take_order(1, 2)
        table1.take_order(2, 1)
        self.assertEqual(table1.totalPrice, 9.5)
        table1.delete_order(1)
        self.assertEqual(table1.totalPrice, 3.5)

if __name__ == '__main__':
    database.init()
    unittest.main()
