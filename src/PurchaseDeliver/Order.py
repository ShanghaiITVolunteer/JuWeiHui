from collections import defaultdict


class Order:
    def __init__(self):
        self.buyer_name = ''
        self.address = None
        self.items = defaultdict(int)

    def set_buyer(self, buyer):
        self.buyer_name = buyer
        return self

    def set_address(self, address):
        self.address = address
        return self

    def set_item(self, item_name, amount):
        self.items[item_name] = amount
        return self
