# 🛍️ Django Modular Store

一个基于 Django 构建的电商商店项目，支持商品展示、购物车、结算模块。

---

## 🚀 功能特色
- 商品分类（Featured / Essentials / New Arrivals）
- 首页商品展示卡
- 支持商品图片展示、价格、描述等
- 购物车模块（添加/移除）
- 后台管理（可创建商品与分类）

---

## 🛠️ 安装与运行

```bash
# 克隆项目
https://github.com/Rem1x-2019/shop.git
cd shop

# 创建虚拟环境并激活
python -m venv venv
source venv/bin/activate  # Windows 用 venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 初始化数据库
python manage.py makemigrations
python manage.py migrate

# 导入示例数据（可选）
python manage.py loaddata categories.json
python manage.py loaddata initial_data_fk.json

# 启动服务
python manage.py runserver
```

访问地址：[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📦 管理后台
```bash
python manage.py createsuperuser
```
访问：[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📁 文件结构
```
shop/
├── apps/
│   ├── store/         # 商品与分类
│   ├── cart/          # 购物车功能
│   └── checkout/      # 结算功能
├── manage.py
├── requirements.txt
└── templates/
```

---

## 📄 License
MIT License

---

欢迎 star ⭐ / fork 🍴 / PR 🔧
