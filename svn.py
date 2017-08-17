#!/usr/bin/python
import os
import subprocess


def update(program_path,path):
    print("svn更新： " + path)
    result = subprocess.Popen(program_path + " /command:update /path:\"" + path + "\" /closeonend:0")
    result.communicate()


def commit(program_path,path,log_message):
    print("svn提交： " + path)
    result = subprocess.Popen(program_path + " /command:commit /path:\""+path+"\" /logmsg:\""+log_message+"\" /closeonend:0")
    result.communicate()




