

import subprocess
import shutil
def excute_cmd_lines(lines,information):
    print(information + " 开始!")
    clear_wrap_and_generate = subprocess.Popen(lines)
    stdout, stderr = clear_wrap_and_generate.communicate()
    #print(stdout)
    #print(stderr)
    print(information + " 完成！")

def copy_files(source_path,target_path,information):
    shutil.copy(source_path, target_path)
    print(information)

new_package_path = "C:/Users/SzoFiel/Desktop/OrangeGameMakerII_Engine_PC_TestVersion/OrangeGameMakerII_Engine_PC_TestVersion_4.3.4/"
config_path = "C:/Users/SzoFiel/Desktop/OrangeGameMakerII_Engine_PC_TestVersion/config.txt"
copy_files(config_path,new_package_path,"复制config.txt 完成！")

new_package_file_path = "C:/Users/SzoFiel/Desktop/OrangeGameMakerII_Engine_PC_TestVersion/OrangeGameMakerII_Engine_PC_TestVersion_4.3.4/OrangeGameMakerII_Engine_PC_TestVersion_4.3.4.exe"
excute_cmd_lines(new_package_file_path,"测试新包文件")