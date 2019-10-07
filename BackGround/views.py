from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from BackGround.models import *
import hashlib
from django.core.paginator import Paginator
# Create your views here.

# 装饰器
def LoginVaild(func):
    ##1.获取cookie中的username和eamil
    ##2.判断username和eamil
    ##3. 如果成功 跳转
    ##4. 如果失败 login.html
    def inner(request,*args,**kwargs):
        # 获取cookie
        username=request.COOKIES.get('username')
        #获取session
        session_username = request.session.get("username")
        # 三个条件都成立
        if username and session_username and username==session_username:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/BackGround/login/')
    return inner

# 加密
def setPassword(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    result=md5.hexdigest()
    return result

# 注册
def register(request):
    if request.method=="POST":
        error_msg=''
        email=request.POST.get('email')
        password=request.POST.get('password')
        if email:
            ##判断邮箱是否存在
            loginuser=LoginUser.objects.filter(email=email).first()
            if not loginuser:
                ##不存在写库
                user=LoginUser()
                user.email=email
                user.username=email
                # 将密码加密进行保存
                user.password=setPassword(password)
                user.user_type=0
                user.save()
            else:
                error_msg='邮箱已存在，请输入新的邮箱'
        else:
            error_msg='邮箱不能为空'
    return render(request,'background/register.html',locals())


# 登录
def login(request):
    if request.method=="POST":
        error_msg=''
        ##获取值
        email=request.POST.get('email')
        password=request.POST.get('password')
        # 如果用户输入了email
        if email:
            #实例化一个用户
            user=LoginUser.objects.filter(email=email,user_type=1).first()
            # 用户存在
            if user:
                # 密码相等
                if user.password==setPassword(password):
                   # #跳转页面
                    response=HttpResponseRedirect('/BackGround/index/')
                    ##设置cookie
                    response.set_cookie('email',user.email)
                    response.set_cookie('username',user.username)
                    response.set_cookie('userid',user.id)
                    request.session['username']=user.username #设置session
                    return response
                else:
                    error_msg='密码错误'
            else:
                error_msg='用户不存在'
        else:
            error_msg='登录邮箱不能为空'
    return render(request,"background/login.html",locals())

# 主页
@LoginVaild
def index(request):
    # username=request.COOKIES.get('username')
    return render(request,'background/index.html')

# 登出
def logout(request):
    # 删除cookie  删除session
    response=HttpResponseRedirect('/BackGround/login/')
    keys=request.COOKIES.keys()
    for i in keys:
        response.delete_cookie(i)


    return response

# 个人中心
def personal_info(request):
    user_id = request.COOKIES.get('userid')
    print(user_id)
    user = LoginUser.objects.filter(id=user_id).first()
    if request.method == "POST":
        data = request.POST
        print(data.get('email'))
        user.username = data.get('username')
        user.phone_number = data.get('phone_number')
        user.age = data.get("age")
        user.gender = data.get("gender")
        user.address = data.get("address")
        user.photo = request.FILES.get("photo")
        user.save()
        print(data)
    return render(request,'background/personal_info.html',locals())


# 增加文章
@LoginVaild
def addarticle(request):
    article_type=Type.objects.all()
    author=Author.objects.all()
    if request.method=='POST':
        data=request.POST
        article=Article()
        article.title=data.get('title')
        article.description=data.get('description')
        article.content = data.get('content')
        article.picture=data.get('picture')
        article.save()

        article_type=request.POST.get('type') #获取文章类型id
        article.type=Type.objects.get(id=article_type)

        author_author = request.POST.get('author')
        article.author =Author.objects.get(id=author_author)

        user_id=request.COOKIES.get('userid')
        article.user=LoginUser.objects.get(id=user_id)
        article.save()
    return render(request, 'background/addarticle.html', locals())

# 文章列表
@LoginVaild
def articlelist(request,page=1):
    user_id=request.COOKIES.get('userid')
    page=int(page)
    article_obj=Article.objects.order_by('-date')
    paginator=Paginator(article_obj,5)
    page_obj=paginator.page(page)
    nowpage=page_obj.number
    start=nowpage-2
    end=nowpage+2
    page_renge=paginator.page_range[start:end]
    return render(request,'background/articlelist.html',locals())

# 文章详情
def getarticle(request,id):
    id=int(id)
    article=Article.objects.get(id=id)
    return render(request,'background/getarticle.html',locals())