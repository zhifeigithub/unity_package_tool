#执行命令行
import subprocess


def excute(lines,information):
    print(information + " 开始!")
    result = subprocess.Popen(lines)
    result.communicate()
    print(information + " 完成！")


