from django.shortcuts import render
from .models import GoodsCategory, GoodsItem
from django.core.paginator import Paginator, Page


def index(request):
    # 查询各分类的最新4条、最热4条数据
    typelist = GoodsCategory.objects.all()
    type0 = typelist[0].goodsitem_set.order_by('-id')[0:4]
    type01 = typelist[0].goodsitem_set.order_by('-click')[0:4]
    type1 = typelist[1].goodsitem_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsitem_set.order_by('-click')[0:4]
    type2 = typelist[2].goodsitem_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsitem_set.order_by('-click')[0:4]
    type3 = typelist[3].goodsitem_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsitem_set.order_by('-click')[0:4]
    type4 = typelist[4].goodsitem_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsitem_set.order_by('-click')[0:4]
    type5 = typelist[5].goodsitem_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsitem_set.order_by('-click')[0:4]
    context = {
        'title': '首页',
        'type0': type0,
        'type01': type01,
        'type1': type1,
        'type11': type11,
        'type2': type2,
        'type21': type21,
        'type3': type3,
        'type31': type31,
        'type4': type4,
        'type41': type41,
        'type5': type5,
        'type51': type51,
    }
    return render(request, 'goods/index.html', context)


def list(request, category_id):
    # deprecated sort_key: 1 id, 2 price, 3 click
    page_num = int(request.GET.get('page', 1))
    sort_key = request.GET.get('sort', 'id')
    typeinfo = GoodsCategory.objects.get(pk=int(category_id))
    news = typeinfo.goodsitem_set.order_by('-id')[0:2]
    if sort_key == 'id' or not sort_key:  # 默认，最新
        goods_list = GoodsItem.objects.filter(category_id=int(category_id)).order_by(
            '-id'
        )
    elif sort_key == 'price':  # 价格
        goods_list = GoodsItem.objects.filter(category_id=int(category_id)).order_by(
            '-price'
        )
    elif sort_key == 'click':  # 人气，点击量
        goods_list = GoodsItem.objects.filter(category_id=int(category_id)).order_by(
            '-click'
        )
    paginator = Paginator(goods_list, 10)
    page = paginator.page(int(page_num))
    context = {
        'title': typeinfo.name,
        'page': page,
        'paginator': paginator,
        'typeinfo': typeinfo,
        'sort': sort_key,
        'news': news,
    }
    return render(request, 'goods/list.html', context)


def detail(request, id):
    goods = GoodsItem.objects.get(pk=int(id))
    goods.click = goods.click + 1
    goods.save()
    news = goods.category.goodsitem_set.order_by('-id')[0:2]
    context = {'title': goods.category.name, 'g': goods, 'news': news, 'id': id}
    response = render(request, 'goods/detail.html', context)

    # record recent visited items in cookies,
    # formatted as items separated with comma
    goods_ids = request.COOKIES.get('goods_ids', '')
    current_id = str(goods.id)
    if goods_ids:
        goods_id_list = goods_ids.split(',')
        if goods_id_list.count(current_id) >= 1:
            goods_id_list.remove(current_id)
        goods_id_list.insert(0, current_id)
        if len(goods_id_list) >= 6:
            goods_id_list = goods_id_list[:6]
        goods_ids = ','.join(goods_id_list)
    else:
        goods_ids = current_id
    response.set_cookie('goods_ids', goods_ids)
    return response


from haystack.views import SearchView


class GoodsSearchView(SearchView):
    # default template for search: <app_name>/templates/search/search.html
    def extra_context(self):
        context = super().extra_context()
        context['title'] = '搜索'
        return context
