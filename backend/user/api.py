from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import get_object_or_404

from ninja import Router, Form
from ninja.security import django_auth
from datetime import datetime
from typing import List
from .schema import *
from .models import *

router = Router(auth=django_auth)


# Request Authentication
@router.post('/login/', auth=None)
def user_login(request, data: Form[UserLogin]):
    user = authenticate(username=data.username, password=data.password)
    if user is not None:
        login(request, user)
        return {'detail': 'login success', 'id': user.id}
    return {'detail': 'login fail'}


@router.post('/logout/')
def user_logout(request):
    logout(request)
    return {'detail': 'logout success'}


# Get all user
@router.get('/get_users/', response=List[UserListSchema])
def get_users(request):
    users =  User.objects.filter(is_active=1)
    return users


# get single user
@router.get('/get_user/{userid}/', response=UserDataSchema)
def get_user(request, userid: int):
    user = User.objects.get(id=userid)
    user_data = {
        'id': user.id,
        'user': user,
        'profile': user.profile,
        'stat': user.stat
    }
    return user_data


# create new user
@router.post('/create_user/', auth=None, response={200:UserListSchema, 404:ErrorSchema})
def create_user(request, data:UserCreateSchema):
    if User.objects.filter(username=data.username).exists():
        return 404, {'detail': 'User does exists'}
    else:
        user = User(username=data.username)        
        user.set_password(user.password)
        user.save()
        profile = UserProfile.objects.create(user=user)
        stat = UserStat.objects.create(user=user)
        return user


# delete user
@router.delete('delete_user/{userid}/')
def delete_user(request, userid: int):
    user = get_object_or_404(User, id=userid)
    user.delete()
    return {'detail': 'Deleted success', 'id': userid}


# edit user profile
@router.put('/edit_profile/{userid}/')
def edit_profile(request, userid: int, data:UserEditDataSchema):
    user = get_object_or_404(User, id=userid)
    user.first_name = data.user.first_name
    user.last_name = data.user.last_name
    user.save()
    profile = get_object_or_404(UserProfile, user=userid)
    profile.nick_name = data.profile.nick_name
    profile.save()
    return 200, {'detail': 'update success', 'id': userid}


# save stat
@router.put('/save_stat/{userid}/')
def save_stat(request, userid:int, data:UserStatSchema):
    stat = get_object_or_404(UserStat, user=userid)
    stat.win += data.win
    stat.lose += data.lose
    stat.save()
    return 200, {'detail': 'update success', 'id': userid}