from django.apps import AppConfig
import os

default_app_config = 'img_db.img_dbConfig'


def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


class img_dbConfig(AppConfig):
    # name = 'img_db'
    name = get_current_app_name(__file__)
    verbose_name = '工程图片'
