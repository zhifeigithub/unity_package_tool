#更新打包文件夹

import svn
import config


data = config.get_data()


svn.update(data["svn_gui_path"],data["package_project_path"])