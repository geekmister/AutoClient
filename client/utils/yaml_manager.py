"""
@Project : cd-auto-test-client.git
@File    : yaml_manager.py
@IDE     : PyCharm
@Author  : geek mister
@Date    : 2024/1/9 15:10
@MyHome  : https://github.com/geekmister
@Desc    : Yaml file manager
"""


import os


import yaml


def map_yaml_files(path):
    """
    Map root path and return yaml files
    Args:
        path(str): yaml file root path

    Returns:
        type: list
        -> yaml files
    """

    yaml_files = []

    if path is not None and path != "":
        for root, dirs, files in os.walk(top=path, topdown=True, onerror=None, followlinks=False):
            yaml_files = files

    return yaml_files


def load_yaml_file(path):
    """
    Load yaml file and return
    Args:
        path(str): yaml file path

    Returns:
        type: dict
        -> yaml file to dict data
    """

    if path is not None and path != "":
        with open(path, "r", encoding='utf-8') as yarm_file:
            data = yaml.safe_load(yarm_file)
            return data


if __name__ == "__main__":
    # the under code are test code
    load_yaml_file("D:\Repositories\Paracraft\QualityAdmin\cd-auto-test\cd-auto-test-client.git\\repositories\Login.yaml")
    # map_yaml_files("D:\Repositories\Paracraft\QualityAdmin\cd-auto-test\cd-auto-test-client.git\\repositories")
    pass