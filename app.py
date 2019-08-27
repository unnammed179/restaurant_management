import database
import tableUi
import orderUi
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTime, QTimer

database.init()
TABLES = []
TABLE = None
SUM = 0
ONGOING = 0


class TableWindow(QMainWindow, orderUi.Ui_MainWindow):
    def __init__(self, id, *args, **kwargs):
        super(TableWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.dishNum = '0'
        self.totalPrice.setText('0')
        self.btnExit.clicked.connect(self.btn_exit_pressed)
        self.dishes = []
        self.idToRemove = 0
        global TABLE
        TABLE = None
        self.order = {}
        for table in TABLES:
            if table.id == id:
                TABLE = table
        if TABLE is None:
            TABLE = database.Table(id)
            TABLES.append(TABLE)
        self.update()
        self.labelTable.setText('Table: ' + str(TABLE.id))
        for i in range(0, 10):
            getattr(self, 'btn%s' %i).clicked.connect(self.btn_num_pressed)
        self.btnQuanti.clicked.connect(self.btn_num_pressed)
        self.btnDel.clicked.connect(self.btn_del_pressed)
        self.btnOk.clicked.connect(self.btn_ok_pressed)
        self.btnOrder.clicked.connect(self.btn_order_pressed)
        self.btnCancel.clicked.connect(self.btn_cancel_pressed)
        self.btnPay.clicked.connect(self.btn_pay_pressed)
        self.listDish.clicked.connect(self.clicked)
        self.btnDelete.clicked.connect(self.btn_delete_pressed)
        self.btnMinus.clicked.connect(self.btn_delete_pressed)

    def clicked(self):
        self.idToRemove = database.find_dish(self.listDish.currentItem().text(), True).id

    def btn_delete_pressed(self):
        if self.idToRemove:
            if self.sender().text() == 'Delete':
                TABLE.delete_order(self.idToRemove, False)
            else:
                TABLE.delete_order(self.idToRemove, True)
        self.idToRemove = 0
        self.update()

    def btn_pay_pressed(self):
        global SUM
        SUM += TABLE.totalPrice
        TABLE.orders.clear()
        TABLE.totalPrice = 0
        self.btn_cancel_pressed()


    def btn_cancel_pressed(self):
        TABLE.orders.clear()
        TABLE.totalPrice = 0
        self.close()

    def btn_order_pressed(self):
        self.close()

    def btn_num_pressed(self):
        sender = self.sender()
        if self.dishNum != '0':
            if '*' not in self.dishNum or sender.text() != '*':
                self.dishNum += sender.text()
        else:
            if sender.text() != '*':
                self.dishNum = sender.text()
        self.display.setText(self.dishNum)

    def btn_del_pressed(self):
        if len(self.dishNum) > 1:
            self.dishNum = self.dishNum[:-1]
        else:
            self.dishNum = '0'
        self.display.setText(self.dishNum)

    def btn_exit_pressed(self):
        for key, value in self.order.items():
            TABLE.delete_order(key, True, value)
        self.close()

    def btn_ok_pressed(self):
        if '*' not in self.dishNum:
            self.quanti = 1
            self.dish = int(self.dishNum)
        else:
            self.quanti = int(self.dishNum.split('*')[0])
            if self.dishNum.endswith('*'):
                self.dish = 0
            else:
                self.dish = int(self.dishNum.split('*')[1])

        if type(database.find_dish(self.dish)) == str:
            self.labelDish.setText('Dish not found!')
        else:
            self.labelDish.setText(database.find_dish(self.dish).name)
            TABLE.take_order(self.dish, self.quanti)
            self.update()
            if self.dish in self.order:
                self.order[self.dish] += self.quanti
            else:
                self.order[self.dish] = self.quanti

    def update(self):
        self.listDish.clear()
        self.listPrice.clear()
        self.listQuanti.clear()
        for key, value in TABLE.orders.items():
            self.listDish.addItem(database.find_dish(key).name)
            self.listQuanti.addItem(str(value))
            self.listPrice.addItem(str(value * database.find_dish(key).price))
        self.dishNum = '0'
        self.display.setText(self.dishNum)
        self.totalPrice.setText(str(TABLE.totalPrice) + ' €')


class MainWindow(QMainWindow, tableUi.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.win = None
        self.tableNum = '0'
        for i in range(0, 10):
            getattr(self,'btn%s' %i).clicked.connect(self.btn_num_pressed)
        self.btnDel.clicked.connect(self.btn_del_pressed)
        self.btnExit.clicked.connect(self.btn_exit_pressed)
        self.btnOk.clicked.connect(self.btn_ok_pressed)
        self.listTable.clicked.connect(self.clicked)
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(500)

    def btn_num_pressed(self):
        self.update()
        sender = self.sender()
        if self.tableNum != '0':
            self.tableNum += sender.text()
        else:
            self.tableNum = sender.text()
        self.lcdTable.display(self.tableNum)

    def btn_del_pressed(self):
        self.update()
        if len(self.tableNum) > 1:
            self.tableNum = self.tableNum[:-1]
        else:
            self.tableNum = '0'
        self.lcdTable.display(self.tableNum)

    def btn_exit_pressed(self):
        self.close()

    def btn_ok_pressed(self):
        self.update()
        if self.tableNum != '0':
            self.win = TableWindow(int(self.tableNum))
            self.win.show()
            self.tableNum = '0'
            self.lcdTable.display(self.tableNum)

    def update(self):
        ONGOING = 0
        self.listPrice.clear()
        self.listTable.clear()
        for table in TABLES:
            if table.totalPrice:
                ONGOING += table.totalPrice
                self.listTable.addItem(str(table.id))
                self.listPrice.addItem(str(table.totalPrice) + ' €')
        self.ongoing.setText('Ongoing: ' + str(ONGOING) + ' €')
        self.sum.setText('Sum: ' + str(SUM) + ' €')

    def clicked(self):
        self.tableNum = self.listTable.currentItem().text()
        self.lcdTable.display(self.listTable.currentItem().text())
        self.win = TableWindow(int(self.tableNum))
        self.win.show()
        self.tableNum = '0'
        self.lcdTable.display(self.tableNum)