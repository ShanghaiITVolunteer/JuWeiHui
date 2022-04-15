#-*- coding:utf-8 –*-
from pylatex import Document, Section, Subsection, Command, Package, Figure, Tabular
from pylatex.utils import italic, NoEscape
from asq.initiators import query
import pandas as pd
import sys
import os

COMBINE_THRESHOLD = 15

buildingGroups = [
    [1, 2, 3, 5],
    [37, 38],
    [39, 40, 41],
    [42, 43, 45, 46],
    [47, 48, 49, 50],
    [51, 52, 53, 55],
    [56, 57, 58],
    [59, 60],
    [62, 63],
    [65, 66, 67, 68],
    [69, 70, 71],
    [72, 73, 75, 76],
    [77, 78, 79],
    [80, 81, 82, 83, 85],
    [86, 87],
    [88, 89],
    [90, 91],
    [92, 93],
    [95, 96, 97],
    [98, 99]
]
        

def read_csv(fileName):
    df = pd.read_csv(fileName)

    def tryGetValue(x, func, default):
        try:
            return func(x)
        except:
            return default

    df['手机号'] = df['手机号'].apply(lambda x: tryGetValue(x, lambda y: str(int(y)), None))
    df['楼栋号'] = df['楼栋号'].apply(lambda x: tryGetValue(x, lambda y: int(y), 0))
    df['门牌号'] = df['门牌号'].apply(lambda x: tryGetValue(x, lambda y: int(y), None))
    df['订购数量'] = df['套餐数量'].apply(lambda x: tryGetValue(x, lambda y: int(y), 0))
    
    for i, ask in df.iterrows():
        if ask['楼栋号'] == ask['门牌号']:
            df.loc[i, '楼栋号'] = 500

    groups = df.groupby('楼栋号')
    
    return groups
        

def combineGroups(groups):
    groupsDic = {}
    for name, group in groups:
        groupsDic[name] = group

    def create_buckets(dfs):
        dfs = query(dfs).order_by_descending(lambda df_pair: len(df_pair[1])).to_list()
        dfs_index = [i for i in range(len(dfs))]
        bucket_list = []
        current_bucket = []

        remove_list = []
        for i in dfs_index:
            if len(dfs[i][1]) > COMBINE_THRESHOLD:
                bucket_list.append([dfs[i]])
                remove_list.append(i)
        for r in remove_list:
            dfs_index.remove(r)

        while len(dfs_index) > 0:
            current_nums = query(current_bucket).select(lambda df_pair: len(df_pair[1])).sum()
            add_new = False
            for i in dfs_index:
                if len(dfs[i][1]) + current_nums <= COMBINE_THRESHOLD:
                    current_bucket.append(dfs[i])
                    add_new = True
                    dfs_index.remove(i)
                    break
            
            current_nums = query(current_bucket).select(lambda df_pair: len(df_pair[1])).sum()
            
            if not add_new:
                bucket_list.append(current_bucket)
                current_bucket = []

        if len(current_bucket) != 0 and query(current_bucket).select(lambda df_pair: len(df_pair[1])).sum() != 0:
            bucket_list.append(current_bucket)
            
        return bucket_list
        
    tasks = []
    for buildingList in buildingGroups:
        dfs = []
        for b in buildingList:
            dfs.append((b, groupsDic.get(b, pd.DataFrame())))
        dfs = query(dfs).order_by_descending(lambda df_pair: len(df_pair[1])).to_list()
        buckets = create_buckets(dfs)
        for b in buckets:
            tasks.append(query(b).select(lambda x: x[0]).to_list())

    tasks = query(tasks).select(lambda x: query(x).order_by(lambda y: y).to_list()).order_by(lambda x: x[0]).to_list()
    return tasks


def generate_latex(groups, folder, title):
    geometry_options = {"tmargin":"1cm", "lmargin":"1cm"}
    doc = Document(geometry_options=geometry_options, default_filepath='basic', documentclass='article')
    doc.packages.add(Package('ctex'))
    doc.append(NoEscape(r'\renewcommand\arraystretch{1.2}'))

    doc.packages.add(Package('ctex'))
    doc.preamble.append(Command('title', title + ' 2022/4/15'))
    doc.append(NoEscape(r'\maketitle'))

    groupsDic = {}
    for name, group in groups:
        groupsDic[name] = group

    c = 0
    tasks = combineGroups(groups)
    other_tasks = [500, 5889, 9999]
    for t in other_tasks:
        if groupsDic.__contains__(t):
            tasks.append([t])

    for task in tasks:

        buildingRangeName = ('高楼' + '，'.join(query(task).select(lambda x: str(x)).to_list()) + '号楼')

        special_name = None
        if len(task) == 1 and (task[0] == 500 or task[0] == 0):
            special_name = '别墅区'
        elif len(task) == 1 and task[0] == 5889:
            special_name = '商务楼'
        elif len(task) == 1 and task[0] == 9999:
            special_name = '居委会'

        if special_name is not None:
            buildingRangeName = special_name

        number_of_purchase = query(task).select(lambda b: sum(groupsDic[b]['套餐数量'])).sum()

        with doc.create(Section(buildingRangeName + '， 共' + str(number_of_purchase) + '单', False)):
            with doc.create(Tabular('|c|c|c|c|c|c|c|')) as table:
                table.add_hline()
                table.add_row(('需求概述', '业主姓名', '订单金额', '楼栋号', '门牌号', '套餐数量', '配送完成'))
                table.add_hline()
                asks = []
                for t in task:
                    for _, ask in groupsDic[t].iterrows():
                        asks.append(ask)

                asks.sort(key=lambda ask: ask['楼栋号'] * 100000 + ask['门牌号'])

                for ask in asks:
                    table.add_row((
                            special_name if special_name is not None else (str(int(ask['楼栋号'])) + '号楼') + str(int(ask['门牌号'])) + '号', 
                            ask['业主姓名'], 
                            ask['订单金额'],
                            special_name if special_name is not None else str(int(ask['楼栋号'])),
                            str(int(ask['门牌号'])),
                            ask['套餐数量'],
                            ''))
                    table.add_hline()
                    c += ask['订购数量']
            doc.append('\n')
            doc.append('签名：\n')

    doc.generate_pdf(filepath=os.path.join(folder, title), compiler='xelatex', clean_tex=False)
    print(c)

def main():
    generate_latex()

groups = read_csv('files\\0415蔬菜(1).csv')
combineGroups(groups)
generate_latex(groups, 'outputfiles', '居委团购-蔬菜')