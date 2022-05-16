from .community_base import CommunityBase, CommunityAddress
from group_purchase.utils.chinese import replace_location


class QingShuiYuan(CommunityBase):

    def __init__(self):
        super().__init__('清水苑')
        self.keywords = ['上海市', '上海', '浦东新区', '浦东', '363', '1280', '828']
        self.has_area = True
        self.area_keywords = {
            '363弄': ['363', '台儿庄'],
            '1280弄': ['1280', '长岛'],
            '828弄': ['828', '荷泽']
        }

    def parse_address(self, address):
        # TODO: 这里以后想办法优化下，感觉有点僵硬，好像还有bug。。。
        try:
            locations = replace_location(address, self.keywords)
            return CommunityAddress(f'{locations[0]}号楼{locations[1]}号', f'{locations[0]}号楼', int(locations[1]))
        except Exception:
            raise ValueError

    def parse_area(self, area):
        for area_name, possible_area_keywords in self.area_keywords.items():
            for word in possible_area_keywords:
                if area.__contains__(word):
                    return area_name

