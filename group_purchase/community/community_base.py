class CommunityAddress:
    """
    小区地址类，building表示楼栋，供表格分组用；full_addr是地址全写，用来输出
    """

    def __init__(self, full_addr, building='', room=0, area=-1):
        self.full_addr = full_addr
        self.building = building
        self.room = room
        self.area = area

    def __str__(self):
        return str(self.full_addr)


class CommunityBase:
    def __init__(self, name):
        self.name = name
        self.has_area = False

    def parse_address(self, address):
        raise NotImplementedError
        
