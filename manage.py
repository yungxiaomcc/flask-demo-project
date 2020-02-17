from app import create_app ,db 
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

migrate = Migrate()

def new_app(config='dev'):
    '''
    
    '''
    app = create_app(config)
    migrate.init_app(app,db)
    return app

manager = Manager(new_app)
# 使用不同的命令参数，启动不同环境的实例
# python manage.py -c dev runserver 使用开发环境配置启动实例,-c prod 参数启用生产环境实例
manager.add_option('-c','--config',dest='config',required=True)
manager.add_conmand('db',MigrateCommand)

if __name__ =='__main__':
    manager.run()