#!/usr/bin/python
import os
import shutil
import config


def make_dir(path):
    path = path.strip()
    is_exist = os.path.exists(path)
    if not is_exist:
        print('创建文件夹： ' + path+"/")
        os.makedirs(path)
        return True
    else:
        print('文件夹已存在： ' + path+"/")
        return False


#文件名末尾数字自动加1
def auto_change_path(path):
    return path[0:-1] + str(int(path[-1]) + 1)


def auto_make_dir(path):
    result = make_dir(path)
    if not result:
        if os.listdir(path):
            print('文件夹不为空： '+path+"/" )
            path = auto_change_path(path)
            if not make_dir(path):
                path = auto_make_dir(path)
    return path


data = config.get_data()

new_package_file_name = data['file_name']
new_package_path = data["package_path"] + new_package_file_name
print("创建新的包文件夹 开始！")
new_package_path = auto_make_dir(new_package_path)
print('创建新的包文件夹 成功！')