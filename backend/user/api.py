from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from ninja import Router
from ninja.security import django_auth
from datetime import datetime
from typing import List
from .schema import *
from .models import *

router = Router()


# Request Authentication
@router.post('/get_auth', auth=None)
def get_auth(request, data: UserSchema):
    username = data.username
    password = data.password
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return f'Authorized Successfully {user}'
    return f'Failed to get authorized'


# Get basic multiple User profile
@router.get('/get_users' ,auth=django_auth, response=List[UserList])
def get_users(request):
    users =  User.objects.all()
    return users


# # Create new user
# @router.post('/create_user')
# def create_user(request, payload: UserSchema):
#     user = User.objects.filter(username=payload.username)
#     if user:
#         return {'detail': 'username is exist'}
#     else:
#         user = User.objects.create(**payload.dict())
#         user.set_password(payload.password)
#         user.save()
#         ustat = UserStat.objects.create(id=user.id)
#         user_profile = UserProfile.objects.create(id=user.id, user_stat=ustat, first_name=user.username)
#         return user


# get single user
@router.get('/get_user/{userid}', response=UserCombinedSchema)
def get_user(request, userid: int):
    user = User.objects.get(id=userid)
    user_data = {
        'user': user,
        'user_profile': user.userprofile,
        'user_stat': user.userstat
    }
    return user_data