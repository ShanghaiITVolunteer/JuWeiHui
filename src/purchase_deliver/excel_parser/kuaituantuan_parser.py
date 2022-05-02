from audioop import add
from pathlib import Path

from purchase_deliver.order import Order
from .excel_parser import ExcelParserBase


# 快团团
class KuaiTuanTuanParser(ExcelParserBase):
    """
    Excel模板，第一行：
    下单人 团员备注 团长备注 跟团号 商品 规格 数量 商品金额 
    运费 优惠 订单金额 退款金额 物流方式 服务小区 服务小区联系人 
    服务小区电话 服务小区地址 收货人 联系电话 详细地址 团长 房号 楼号 弄号

    商品名和excel文件名保持一致
    """

    def __init__(self, file):
        super().__init__(file)
        self.amount_col = None
        self.full_address_col = None

    def get_header(self):
        for i in range(self.sheet.max_column):
            if self.sheet.cell(1, i + 1).value == "详细地址":
                self.full_address_col = i
            if self.sheet.cell(1, i + 1).value == "数量":
                self.amount_col = i

    def loop_record(self):
        for r in self.sheet.iter_rows(min_row=2, max_row=self.sheet.max_row):
            yield r

    def record_to_order(self, record, community):
        try:
            return (Order()
                    .set_buyer(record[0].value)
                    .set_address(community.parse_address(record[self.full_address_col].value))
                    .set_item(Path(self.file.name).stem, record[self.amount_col].value))
        except ValueError:
            raise ValueError(f'{record[self.full_address_col].coordinate}')
