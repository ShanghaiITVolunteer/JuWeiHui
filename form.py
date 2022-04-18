#-*- coding:utf-8 –*-
from pylatex import Document, Section, Subsection, Command, Package, Figure, Tabular
from pylatex.utils import italic, NoEscape
import pandas as pd
import sys
import os


class CombinedGroups():

    def __init__():
        self.buildingNums = []
        

def read_csv(fileName):
    df = pd.read_csv(fileName)

    def tryGetValue(x, func, default):
        try:
            return func(x)
        except:
            return default

    df['楼栋号'] = df['楼栋号'].apply(lambda x: tryGetValue(x, lambda y: int(y), 0))
    df['门牌号'] = df['门牌号'].apply(lambda x: tryGetValue(x, lambda y: int(y), 0))
    df['订购数量'] = df['套餐数量'].apply(lambda x: tryGetValue(x, lambda y: int(y), 0))
    
    for i, ask in df.iterrows():
        if ask['楼栋号'] == ask['门牌号'] or ask['门牌号'] == 0 or (ask['楼栋号'] <= 36 and ask['楼栋号'] >= 7):
            df.loc[i, '门牌号'] = df.loc[i, '楼栋号']
            df.loc[i, '楼栋号'] = 500

    groups = df.groupby('楼栋号')
    
    return groups
        

def combineGroups(groups):
    pass



def generate_latex(groups, folder, title):
    geometry_options = {"tmargin":"1.5cm", "lmargin":"1.5cm"}
    doc = Document(geometry_options=geometry_options, default_filepath='basic', documentclass='article')
    doc.packages.add(Package('ctex'))
    doc.append(NoEscape(r'\renewcommand\arraystretch{1.2}'))

    doc.packages.add(Package('ctex'))

    c = 0
    index = 0

    for name, group in groups:
        index += 1

        buildingNum = (str(int(name)) + '号楼')

        if name == 500:
            buildingNum = '别墅区'
        elif name == 5889 or name == 5899:
            buildingNum = '商务楼'
        elif name == 9999:
            buildingNum = '居委会'

        with doc.create(Section(buildingNum + '， 共' + str(int(sum(group['订购数量']))) + '单', False)):
            with doc.create(Tabular('|c|c|c|c|c|c|c|')) as table:
                table.add_hline()
                table.add_row(('需求概述', '业主姓名', '订单金额', '楼栋号', '门牌号', '套餐数量', '配送完成'))
                table.add_hline()
                asks = []
                for _, ask in group.iterrows():
                    asks.append(ask)

                asks.sort(key=lambda ask: ask['门牌号'])
                for ask in asks:
                    table.add_row((
                            #ask['需求概述'] if name != 500 else buildingNum + str(int(ask['门牌号'])) + '号', 
                            buildingNum + str(int(ask['门牌号'])) + '号：' + title, 
                            ask['业主姓名'], 
                            ask['订单金额'],
                            buildingNum,
                            str(int(ask['门牌号'])) if ask['门牌号'] != 0 else str(int(ask['楼栋号'])),
                            ask['套餐数量'],
                            ''))
                    table.add_hline()
                    c += ask['订购数量']
            doc.append('\n')
            doc.append('签名：')
            if (index != len(groups)):
                doc.append('\n')

    doc.generate_pdf(filepath=os.path.join(folder, '居委团购-' + title), compiler='xelatex', clean_tex=False)
    tex = doc.dumps()
    print(title, '-', c)

def main():
    generate_latex()

#pairs = [('files\\0416萃阳楼肉品.csv', '居委团购-萃阳楼肉品'), ('files\\0416防疫.csv', '居委团购-防疫'), ('files\\0416水产.csv', '居委团购-水产'), ('files\\0416水果.csv', '居委团购-水果')]
pairs = [('files\\0418小番茄.csv', '0418小番茄'), ('files\\0418蔬菜.csv', '0418蔬菜')]
for p in pairs:
    groups = read_csv(p[0])
    generate_latex(groups, 'outputfiles', p[1])