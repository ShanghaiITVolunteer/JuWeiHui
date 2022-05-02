import openpyxl

from purchase_deliver.order_set import OrderSet


class ExcelParserBase:
    """
    Excel模板Base类。
    """

    def __init__(self, file):
        self.file = file
        self.sheet = openpyxl.load_workbook(self.file).active

    def parse_for_community(self, community):
        order_set = OrderSet()
        error_cells = []
        self.get_header()
        for record in self.loop_record():
            try:
                order = self.record_to_order(record, community)
                order_set.add_order(order)
            except ValueError as e:
                error_cells.append(str(e))
        return order_set, error_cells

    def get_header(self):
        raise NotImplementedError

    def loop_record(self):
        raise NotImplementedError

    def record_to_order(self, record, community):
        # 这个函数还不能弄成static，有些表格的表头含有有效信息，要通过self传递
        # !!! 覆写时，用community.parse_address解析地址；对于解析失败(ValueError)的地址raise ValueError并把单元格坐标加到msg中
        raise NotImplementedError
