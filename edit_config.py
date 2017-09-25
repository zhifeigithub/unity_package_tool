#打开配置文件

import package_cmd
import config


data = config.get_data()

package_cmd.excute("notepad "+data["package_config_path"],"打开配置文件")



