#打开测试VS工程

import package_cmd
import config


def open_project():
    package_cmd.os_excute("start " + config.get_data()["test_project_vs"],"打开测试VS工程")


open_project()