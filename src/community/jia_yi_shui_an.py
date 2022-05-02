from .community_base import CommunityBase, CommunityAddress
from utils.chinese import replace_location


class JiaYiShuiAn(CommunityBase):
    def __init__(self):
        super().__init__('嘉怡水岸')
        self.keywords = ['上海市', '上海', '闵行区', '闵行', '紫龙路', '500号', '五百号', '500']

        # In JiaYiShuiAn, number 7 -36 are houses, with no room number
        self.SPECIAL_NUMBERS_HOUSE = {
            5899: '商务楼'
        }
        for i in range(6, 37):
            self.SPECIAL_NUMBERS_HOUSE[i] = '别墅区'

    def parse_address(self, address):
        # TODO: 这里以后想办法优化下，感觉有点僵硬，好像还有bug。。。
        try:
            locations = replace_location(address, self.keywords)
        except Exception:
            raise ValueError

        if len(locations) == 2:
            if address.__contains__('5899'):
<<<<<<< HEAD:src/Communitiy/JiaYiShuiAn.py
                locations.remove(5899) 
=======
                locations.remove(5899)
>>>>>>> 3696f59 (重构):src/community/jia_yi_shui_an.py
                return CommunityAddress(f'商务楼{locations[0]}',
                                        '商务楼',
                                        int(locations[0]))
            return CommunityAddress(f'{locations[0]}号楼{locations[1]}号', f'{locations[0]}号楼', int(locations[1]))
        if len(locations) == 1:
<<<<<<< HEAD:src/Communitiy/JiaYiShuiAn.py

=======
>>>>>>> 3696f59 (重构):src/community/jia_yi_shui_an.py
            if self.SPECIAL_NUMBERS_HOUSE.__contains__(locations[0]):
                return CommunityAddress(f'{self.SPECIAL_NUMBERS_HOUSE[locations[0]]}{locations[0]}号',
                                        self.SPECIAL_NUMBERS_HOUSE[locations[0]],
                                        int(locations[0]))
            if address.__contains__('商务楼'):
                return CommunityAddress(f'商务楼{locations[0]}',
                                        '商务楼',
                                        int(locations[0]))
            if address.__contains__('居委会'):
                return CommunityAddress('居委会', '居委会')
        raise ValueError
