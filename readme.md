# 

1 数据迁移命令，把模型映射到数据库中
初始化一次就可以，
python manage.py db init

python manage.py db migrate

把生成的迁移文件映射到数据库中
python manage.py db upgrade

