from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()


class Department(models.Model):
    """ 部门表 """
    title = models.CharField(max_length=16)


"""
create table app01_userinfo(
    id *** #django自动为用户创建的
    name ***
    password ***
    
)
"""
