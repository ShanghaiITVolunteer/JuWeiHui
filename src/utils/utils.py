#-*- coding:utf-8 –*-

import re
import os
from asq.initiators import query


def find_all_files(path, suffix=None):
    all_files = []
    for root, directories, files in os.walk(path):
        for file in files:
            if((suffix is not None) and query(suffix).any(lambda s: file.endswith(s))):
                all_files.append((root, file))

    return all_files