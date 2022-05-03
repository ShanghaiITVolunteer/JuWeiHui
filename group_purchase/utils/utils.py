#-*- coding:utf-8 –*-

import re
import os
import pandas as pd
from asq.initiators import query


def find_all_files(path, suffix=None):
    all_files = []
    for root, directories, files in os.walk(path):
        for file in files:
            if((suffix is not None) and query(suffix).any(lambda s: file.endswith(s))):
                all_files.append((root, file))

    return all_files


def read_excel(fileName, community):    
    df = pd.read_excel(fileName)
    success, results = community.special_building_numbers(df)

    if success:
        return results
    else:
        error_str = ''
        for i, row in results.iterrows():
            error_str += f"\n{row['收货人']} {int(row['联系电话'])} {row['收货地址']}"
        raise ValueError(f'Some users address are not correct! Errors:\n{error_str}\n')

