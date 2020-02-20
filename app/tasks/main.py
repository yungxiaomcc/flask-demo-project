from celery import Celery
from app.tasks import config

'''
win10 中运行报错
ValueError : not enough values to unpack(expect2,got 0)
解决方法：
1.安装eventlet
2.执行 celery -A <module> worker -l info -P eventlet
'''

# 定义celery对象
celery_app = Celery('app')

# 引入配置信息
'''
celery_app.config_from_object(config)
直接通过类名会报错：
Can't pickle <type 'module'> :it's not found as __builtin__.module
通过字符串方式 作为参数来解决
'''
celery_app.config_form_object('app.tasks.config')

# 自动搜索异步任务
celery_app.autodiscover_tasks(['app.tasks.task1','app.tasks.task2'])