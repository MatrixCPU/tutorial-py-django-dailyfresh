## 天天生鲜项目
基于 Django 2.x，天天生鲜产品销售网站。

## 简介

- 商品分类展示：首页大屏幕热销产品，四种产品分类
- 用户登录注册：联系方式、收货地址管理
- 详情页面：商品图片、描述、销量、剩余，下单后加入物品进购物车
- 购物车结算
- 全文检索：Haystack + Whoosh 检索商品信息
- 后台利用 Django 自带后台管理，方便商户上传产品图片。
- 后台集成 tinymce 富文本编辑器，描述商品详情

注

- 由于项目重点在于商品展示、销售逻辑，邮件验证等用户信息管理较为薄弱

### 部署
Copy `.env-example` as `.env` and configure the app in `.env`.

```shell
# install required pkgs
pipenv sync
# or
pip install requirements/prod.txt

# create db and tables
python manage.py migrate

# rebuild index files
python manage.py rebuild_index
```

### TODOs
源教程有多处不足，本项目尝试修正

- [x] 移除URL硬编码（基本完成，除部分静态文件链接）
- [x] 使用查询参数，避免出现类似于`/list1_1_1`形式的山炮URL
- [x] Whoosh配合Jieba分词支持中文全文搜索，避免直接修改包源码
- [x] 合并多个记录查询的多次查询为一次（使用`fieldname__in`）
- [ ] 交易记录直接记录用户信息，而不是使用外键，避免用户信息变更导致交易记录亦随之变化
- [x] Load settings from `.env` by `python-dotenv`
