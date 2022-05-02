from typing import *
from collections import defaultdict
from community.community_base import CommunityAddress


class Order:
    def __init__(self):
        self.buyer_name: str = ''
        self.address: Optional[CommunityAddress] = None
        self.items: defaultdict[str, int] = defaultdict(int)

    def set_buyer(self, buyer: str) -> 'Order':
        self.buyer_name = buyer
        return self

    def set_address(self, address: CommunityAddress) -> 'Order':
        self.address = address
        return self

    def set_item(self, item_name: str, amount: int) -> 'Order':
        self.items[item_name] = amount
        return self
