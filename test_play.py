#用unity测试

import config
import package_cmd

data = config.get_data()
project_path = data["project_path"]
unity_file_path = data["unity_file_path"]

#clear_wrap_and_generate
package_cmd.excute(unity_file_path+" "+"-batchmode -quit -projectPath " + project_path + " -executeMethod ToLuaMenu.ClearLuaWraps","clear_wrap_and_generate")
#build_windows_resource
package_cmd.excute(unity_file_path+" "+"-batchmode -quit -projectPath " + project_path + " -executeMethod Packager.BuildWindowsResource","build_windows_resource")
#查看测试
package_cmd.excute(unity_file_path+" "+"-projectPath " + project_path + " -executeMethod TestEditor.TestPlay","测试")
