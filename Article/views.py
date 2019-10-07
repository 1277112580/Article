from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.core.paginator import Paginator
from BackGround.models import *
# Create your views here.

# 网站首页
def index(request):

    # 获取cookie 获取了用户名
    username=request.COOKIES.get('username')
    print(username)

    """
    查询6条数据
    查询推荐的7条数据
    查询点击率排行榜的12条数据
    :param request: 
    :return: 
    """

    article=Article.objects.order_by('-date')[:6]
    recommend_article=Article.objects.filter(recommend=1).all()[:7]
    click_article=Article.objects.order_by('-click')[:12]

    return render(request,'Article/index.html',locals())

# 个人相册
def listpic(request):
    return render(request,'Article/listpic.html')

# 文章列表分页
def newslistpic(request,page=1):
    page=int(page) #1为字符串类型，需要将类型转换
    article=Article.objects.order_by('-date')
    paginator=Paginator(article,6)  #显示每页6条数据
    page_obj=paginator.page(page)
    # 获取当前页
    current_page=page_obj.number
    start=current_page-3
    if start<1:
        start=0
    end=current_page+2
    if end > paginator.num_pages:
        end = paginator.num_pages
    if start==0:
        end=5
    if end==paginator.num_pages:
        start=paginator.num_pages-5
    page_range=paginator.page_range[start:end]
    return render(request,'Article/newslistpic.html',locals())

# 父模板
def base(request):
    # get请求
    data=request.GET
    serach=data.get('serach')
    print(serach)
    # 通过form表单提交的数据，判断数据库中是否存在某个文章
    # 通过模型查询
    article=Article.objects.filter(title__contains=serach).all()
    print(article)
    return render(request,'Article/base.html',locals())
# 文章详情
def articledetails(request,id):
    # id为字符串类型
    id=int(id)
    article=Article.objects.get(id=id)
    print(article)
    return render(request,'article/articledetails.html',locals())
# 个人简介
def about(request):
    return render(request,'article/about.html')




















