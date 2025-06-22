# 车地通信无线智能检测后端

这是一个基于 Django 的车地通信无线智能检测后端项目。

## 环境准备

请确保您已安装 Python 3.10 和 pip。

## 安装步骤

1. **克隆代码库**

   ```bash
   git clone https://github.com/zhiqing0205/shanghai_subway_backend
   cd shanghai_subway_backend
   ```

2. **创建并激活虚拟环境 (推荐)**

   - Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **安装项目依赖**

   ```bash
   pip install -r requirements.txt
   ```

## 启动项目

1. **执行数据库迁移**

   ```bash
   python manage.py migrate
   ```

2. **启动开发服务器**

   ```bash
   python manage.py runserver
   ```

   项目默认将在 `http://127.0.0.1:8000/` 启动。

## 主要依赖

- Django==4.2.11
- django-simpleui==2024.3.25
- django-cors-headers==4.3.1
