import csv


class Dish:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __iter__(self):
        return iter([self.id, self.name, self.price])


def load_dish():
    result = []
    with open('dishes.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        for row in reader:
            if len(row):
                result.append(Dish(int(row[0]), row[1], float(row[2])))
    return result


def save_dish(dishes):
    with open('dishes.csv', 'w') as csvFile:
        writer = csv.writer(csvFile, delimiter=',')
        for dish in dishes:
            writer.writerow(list(dish))


dishes = []


def init():
    global dishes
    dishes.append(Dish(1,'Sate chicken',3))
    dishes.append(Dish(2, 'Summer roll', 3.5))
    dishes.append(Dish(3, 'Spring roll', 3))
    dishes.append(Dish(4, 'Chicken soup with coconut', 3))
    dishes.append(Dish(5, 'Shrimp soup with coconut', 3))
    dishes.append(Dish(6, 'Hot and sour soup', 2.5))
    dishes.append(Dish(8, 'Chicken soup',  3))
    dishes.append(Dish(9, 'Shrimp soup', 3))
    dishes.append(Dish(10, 'Wantan soup', 3))
    dishes.append(Dish(11, 'Fried wantan', 4))
    dishes.append(Dish(12, 'Veg. sumer roll', 3.5))
    dishes.append(Dish(13, 'Veg. spring roll', 3.5))
    dishes.append(Dish(14, 'Tofu soup with coconut', 3))
    dishes.append(Dish(15, 'Tofu soup', 3))
    dishes.append(Dish(16, 'Glass noodle soup with vegetables', 3))
    dishes.append(Dish(20, 'Pho with beef', 7))
    save_dish(dishes)


def find_dish(id, byName = False):
    if not byName:
        for dish in dishes:
            if dish.id == id:
                return dish
    else:
        for dish in dishes:
            if dish.name == id:
                return dish
    return 'Dish not found!'


class Table:
    def __init__(self, id):
        self.id = id
        self.totalPrice = 0
        self.orders = {}

    def cal_price(self):
        self.totalPrice = 0
        for key, value in self.orders.items():
            for dish in dishes:
                if dish.id == key:
                    self.totalPrice += dish.price * value

    def take_order(self, id, quanti):
        if type(find_dish(id)) == str:
            print(find_dish(id))
        elif id not in self.orders:
            self.orders[id] = quanti
        else:
            self.orders[id] += quanti
        self.cal_price()

    def delete_order(self, id, decrement=False, quanti = 1):
        if id in self.orders:
            if not decrement:
                del self.orders[id]
            else:
                self.orders[id] -= quanti
                if not self.orders[id]:
                    del self.orders[id]
        self.cal_price()