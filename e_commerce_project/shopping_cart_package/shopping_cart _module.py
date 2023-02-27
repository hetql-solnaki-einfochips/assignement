
class ShoppingCart:

    item1 = Item()
    item2 = Item()

    item1.item_des = "Grocery item"
    item1.item_id = 1000
    item1.item_quantity = 20
    item1.item_price = 800000

    item2.item_des = "Clothes"
    item2.item_id = 2000
    item2.item_quantity = 90
    item2.item_price = 1000000

    item1.item_list()
    item2.item_list()

    item1.item_cal()
    item2.item_cal()