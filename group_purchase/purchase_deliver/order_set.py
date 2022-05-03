from collections import defaultdict
from pathlib import Path

from group_purchase.utils.pdf_gen import html_string_to_pdf


def group_orders_by_address(orders):
    ret = defaultdict(list)
    for i in orders:
        ret[i.address.building].append(i)
    return ret


def order_set_to_html(orders, title):
    ret = ''
    groups = group_orders_by_address(orders)
    orders = 0
    for group in sorted(groups):  # TODO: 改进排序算法，支持数字和非数字混合排序，不要用字典序
        orders += int(sum(sum(i.items.values()) for i in groups[group]))
        ret += f'''<div class='no-break'>
        <h2>{group}, 共{int(sum(sum(i.items.values()) for i in groups[group]))}单  {title}</h2>
        <table>
        <tr>
        <th>需求概述</th><th>楼栋号</th><th>房间号</th><th>购买物品</th><th>配送完成</th>
        </tr>
        {''.join(
            f'<tr><td>{order.address}: {title}</td><td>{order.address.building}</td><td>{order.address.room}</td>'
            f'<td>{"<br>".join(f"{item} ×{int(amount)}" for item, amount in order.items.items())}</td><td>&nbsp;</td></tr>'
            for order in sorted(groups[group], key=lambda x: x.address.room))}
        </table>
        </div>'''
    print(f'{title} - {orders}')
    return ret


class OrderSet:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def print_to_pdf(self, filename):
        r = order_set_to_html(self.orders, Path(filename).stem)
        html_string_to_pdf(r, filename)
