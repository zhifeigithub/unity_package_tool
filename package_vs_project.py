#打开打包VS工程

import package_cmd
import config


def open_project():
    package_cmd.os_excute("start " + config.get_data()["package_project_vs"],"打开打包VS工程")


open_project()