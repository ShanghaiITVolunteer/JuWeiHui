from pathlib import Path

from group_purchase.purchase_deliver.order import Order
from .excel_parser import ExcelParserBase


# 群接龙
class JieLongParser(ExcelParserBase):
    """
    Excel模板，第一行：收货人 联系电话 订单总金额 支付状态 收货地址 订购数量
    后起每行一条记录，最后一行是合计
    商品名和excel文件名保持一致
    """

    def get_header(self):
        pass

    def loop_record(self):
        for r in self.sheet.iter_rows(min_row=2, max_row=self.sheet.max_row - 1):
            yield r

    def record_to_order(self, record, community):
        try:
            return (Order()
                    .set_buyer(record[0].value)
                    .set_address(community.parse_address(record[4].value))
                    .set_item(Path(self.file.name).stem, record[5].value))
        except ValueError:
            raise ValueError(f'{record[4].coordinate}')
