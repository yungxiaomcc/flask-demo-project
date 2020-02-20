
from  app.tasks.main import celery_app

@celery_app.task
def fun1():
    pass
@celery_app.task
def fun2(arg1,arg2):
    pass


'''
使用方式：
在视图函数中导入  fun1，fun2
调用方式
fun2.delay(arg1,arg2)
'''