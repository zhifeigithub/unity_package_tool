#执行命令行
import subprocess
import os


def excute(lines,information):
    print(information + " 开始!")
    result = subprocess.Popen(lines)
    result.communicate()
    print(information + " 完成！")

def os_excute(lines,information):
    print(information + " 开始!")
    os.system(lines)
    print(information + " 完成！")



