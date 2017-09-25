#更新工程文件夹

import svn
import config


data = config.get_data()


svn.update(data["svn_gui_path"],data["test_project_path"])