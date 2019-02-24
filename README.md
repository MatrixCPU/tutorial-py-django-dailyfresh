## 天天生鲜项目

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
源教程有多处不足、败笔，本项目尝试修正
- [x] 移除URL硬编码（基本完成，除部分静态文件链接）
- [x] 使用查询参数，避免出现类似于`/list1_1_1`形式的山炮URL
- [x] Whoosh配合Jieba分词支持中文全文搜索，避免直接修改包源码
- [x] 合并多个记录查询的多次查询为一次（使用`fieldname__in`）
- [ ] 交易记录直接记录用户信息，而不是使用外键，避免用户信息变更导致交易记录亦随之变化
- [x] Load settings from `.env` by `python-dotenv`
