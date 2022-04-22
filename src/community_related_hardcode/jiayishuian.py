
from community_related_hardcode.community_hardcode import *
from utils.chinese import replace_location

class JiaYiShuiAn(Community):

    def __init__(self):
        self.keywords = ['上海市', '上海', '闵行区', '闵行', '紫龙路', '500号', '五百号', '500']

        self.SPECIAL_NUMBERS_BUILDING = {
            9999: '居委会'
        }

        # In JiaYiShuiAn, number 7 -36 are houses, with no room number
        self.SPECIAL_NUMBERS_HOUSE = {
            5899: '商务楼'
        }
        for i in range(7, 37):
            self.SPECIAL_NUMBERS_HOUSE[i] = '别墅区'


    def special_building_numbers(self, df):
        failed_address = []
        df = df[df['收货人'] != '合计']
        for i, row in df.iterrows():
            try:
                locations = replace_location(row['收货地址'], self.keywords)
            except:
                failed_address.append(i)
                continue

            if len(locations) > 2:
                failed_address.append(i)
            elif len(locations) == 2:
                df.loc[i, '楼栋号'] = str(locations[0]) + '号楼'
                df.loc[i, '门牌号'] = locations[1]
            elif len(locations) == 1:
                if self.SPECIAL_NUMBERS_BUILDING.__contains__(locations[0]):
                    df.loc[i, '楼栋号'] = self.SPECIAL_NUMBERS_BUILDING[locations[0]]
                    df.loc[i, '门牌号'] = ''
                elif self.SPECIAL_NUMBERS_HOUSE.__contains__(locations[0]):
                    df.loc[i, '楼栋号'] = self.SPECIAL_NUMBERS_HOUSE[locations[0]]
                    df.loc[i, '门牌号'] = locations[0]
                else:
                    failed_address.append(i)
            else:
                if row['收货地址'].__contains__('居委会'):
                    df.loc[i, '楼栋号'] = '居委会'
                    df.loc[i, '门牌号'] = ''
                else:
                    failed_address.append(i)

        if len(failed_address) != 0:
            return False, df.loc[failed_address]

        df['订购数量'] = df['套餐数量'].apply(lambda x: tryGetValue(x, lambda y: int(y), 0))
        groups = df.groupby('楼栋号')

        return True, groups
