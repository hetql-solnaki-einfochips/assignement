class Item:
    item_price=None
    item_des=None

    def __int__(self):
        self.item_quantity = None
        self.item_id = None

    def item_list(self):
        print(30 * '-')
        print("Item Price", self.item_price)
        print("Item Id", self.item_id)
        print("Item description",
              self.item_des)
        print("Item Quantity", self.item_quantity)
        print(30 * '-')

    def item_cal(self):
        if self.item_quantity==90:
            self.item_price= self.item_price - (self.item_price*10/100)*self.item_quantity
            print("FInal price is", self.item_price)
        elif self.item_quantity==20:
            self.item_price = self.item_price - (self.item_price * 15 / 100) * self.item_quantity
            print("FInal price is", self.item_price)
        else:
            print("Out of stock")



