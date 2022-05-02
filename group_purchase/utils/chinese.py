#-*- coding:utf-8 –*-
import re
from unicodedata import numeric

CHINESE_NUMBERS_UTF_8 = '\u96f6\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343'


# Simple chinese to int function
# allows all values less than 10000
# If your address contains Chinese represent higher than 10000, please leave issues and I will update (which is rare in reality)
def forward_cn2int(inputs):
    output = 0
    unit = 1
    num = 0
    for index, cn_num in enumerate(inputs):
        numeric_num = numeric(cn_num)
        if  numeric_num < 10:
            # 数字
            num = numeric_num
            # 最后的个位数字
            if index == len(inputs) - 1:
                output = output + num
        else:
            # 单位
            unit = numeric_num
            # 累加
            output = output + num * unit
            num = 0
 
    return output


# Please design keyword for your community
# for example your community name, city name, district name
def replace_location(location, community_keywords = []):
    for keyword in community_keywords:
        location = location.replace(keyword, '')

    result = re.findall(f'([{CHINESE_NUMBERS_UTF_8}]+|[0-9]+)', location)

    for index, rst in enumerate(result):
        if len(re.findall(f'([{CHINESE_NUMBERS_UTF_8}]+)', rst)) > 0:
            result[index] = forward_cn2int(rst)
        result[index] = int(result[index])

    return result


# Community Consts
