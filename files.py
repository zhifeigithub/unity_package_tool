#!/usr/bin/python
import os
import shutil


def copy(source_path,target_path,information):
    shutil.copy(source_path, target_path)
    print(information)


