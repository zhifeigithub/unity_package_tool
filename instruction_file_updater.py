#!/usr/bin/python
import os
import shutil

#解析元数据
import config

data = config.get_data()

#svn更新说明文档文件夹
import svn

svn.update(data["svn_gui_path"],data["instruction_files_path"])

#更新:更新日志.txt
import release_information_updater

#更新api_factory_new和test_new文件
import files

files.copy(data["api_factory_new_path"],data["instruction_files_path"],"复制: "+data["api_factory_new_path"])
files.copy(data["test_new_path"],data["instruction_files_path"],"复制: "+data["test_new_path"])

#svn提交:更新日志.txt,api_factory_new.lua,test_new.lua
svn.commit(data["svn_gui_path"],data["release_file_path"],data["release_information"])
svn.commit(data["svn_gui_path"],data["instruction_files_path"]+"test_new.lua",data["release_information"])
svn.commit(data["svn_gui_path"],data["instruction_files_path"]+"api_factory_new.lua",data["release_information"])



