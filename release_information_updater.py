#!/usr/bin/python
import os
import shutil
import config


def update_release_information(path,content):
    fo = open(path, 'r+')
    source_content = fo.read()
    new_content =  content+ '\n' + source_content
    fo.close()
    fo = open(path, 'w')
    fo.write(new_content)
    fo.flush()
    fo.close()
    print('修改： '+path)

data = config.get_data()
release_file_path = data['release_file_path']
update_release_information(release_file_path,data['release_information'])
