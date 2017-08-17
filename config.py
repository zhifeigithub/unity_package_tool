#!/usr/bin/python
import os
import shutil

config_path = "F:/workspace/ORG_GameMaker/Documents/共享文档/橙光引擎II/说明文档/package_config.txt"


def get_data():
    data = {}
    data_str = open(config_path, 'r+', encoding='utf-8').read()
    data_str_array = data_str.strip().split('#')[1:-1]
    for child in data_str_array:
        child = child.strip().strip('\n')
        if child != "":
            str_tmp = child.split('=')
            key = str_tmp[0].strip()
            value = str_tmp[1].strip()
            data[key] = value
    return data
