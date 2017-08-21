#用unity打包
import subprocess
import config
import files
import package_cmd


'''''''#########################创建打包文件夹##################################'''
import new_package_dir



data = config.get_data()

#打包
new_package_path = new_package_dir.new_package_path

old_char = data["file_name"][-1]
new_char = new_package_path[-1]
new_package_name = data["file_name"]
if old_char != new_char:
    new_package_name = data["file_name"][0:-1]+new_char
new_package_file_path = new_package_path +"/"+new_package_name+".exe"

unity_package_argument = "+PackagePath"+" "+new_package_file_path

package_cmd.excute(data["unity_file_path"]+" "+"-batchmode -quit -projectPath " + data["project_path"] + " -executeMethod TestEditor.Package"+" "+unity_package_argument,"打包")

'''############复制config.txt文件#################'''

#new_package_path = new_dir_creator.new_package_path
#config_path = data["config_path"]
files.copy(data["config_path"],new_package_path,"复制： "+data["config_path"])

'''############测试新包文件#################'''
package_cmd.excute(new_package_file_path,"测试新包")

print("打包 完成！")