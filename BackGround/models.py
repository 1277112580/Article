from django.db import models

# Create your models here.

GENDER_LIST=(
    (1,'男'),
    (2,'女'),
)
class Author(models.Model):
    name=models.CharField(max_length=32,verbose_name='作者姓名')
    age=models.IntegerField(verbose_name='年龄')
    gender=models.IntegerField(choices=GENDER_LIST,verbose_name='作者性别')
    email=models.EmailField(max_length=32,verbose_name='邮箱')

class Type(models.Model):
    type_name=models.CharField(max_length=32,verbose_name='文章类型')
    type_description=models.TextField(verbose_name='类型描述')


class LoginUser(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=32)
    username=models.CharField(max_length=32,null=True,blank=True)
    pthone_number=models.CharField(max_length=11,null=True,blank=True)
    photo=models.ImageField(upload_to='img',null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    gender=models.CharField(null=True,blank=True,max_length=8)
    address=models.TextField(null=True,blank=True)
    user_type=models.IntegerField(default=1)#0代表前台登录， 1代表后端登录，2代表管理员


class Article(models.Model):
    title=models.CharField(max_length=32,verbose_name='文章名字')
    date=models.DateField(auto_now=True,verbose_name='文章日期')
    content=models.TextField(verbose_name='文章内容')
    description=models.TextField(verbose_name='文章描述')
    picture=models.ImageField(upload_to='images',verbose_name='图片')
    # 推荐
    recommend = models.IntegerField(verbose_name='推荐', default=0)  # 0代表不推荐 1代表推荐
    # 点击率
    click = models.IntegerField(verbose_name='点击率', default=0)
    author = models.ForeignKey(to=Author, on_delete=models.SET_DEFAULT, default=1, verbose_name='文章作者')
    type = models.ForeignKey(to=Type,on_delete=models.SET_DEFAULT,default=1)
    user=models.ForeignKey(to=LoginUser,on_delete=models.SET_DEFAULT,default=1,verbose_name='文章发表者')


