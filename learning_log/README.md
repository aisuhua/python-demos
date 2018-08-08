# Learning log

```sh
# 创建新项目
mkdir learning_logs

# 新建虚拟环境
python3 -m venv ll_env

# 安装django
source ll_env/bin/activate
pip3 install Django

# 创建项目
django-admin.py startproject learning_log .

# 创建数据库
python manage.py migrate

# 运行项目
python manage.py runserver

# 创建一个应用(app)
python manage.py startapp learning_logs

# 定义模型
# 激活模型，每次修改模型后都需要执行此步骤
python manage.py makemigrations learning_logs
python manage.py migrate

# 创建超级用户（后台管理员）
python manage.py createsuperuser

# 向管理后台注册模型

# Django shell
python manage.py shell
```

初始化主页

```sh
# 定义路由规则
# 编写视图
# 编写模板
```
