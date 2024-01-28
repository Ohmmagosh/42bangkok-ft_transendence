from django.shortcuts import get_object_or_404
from ninja import Router
from .models import Users

from ninja.orm import create_schema

router = Router()

################################################
# Schema

UserNew = create_schema(Users, exclude=['id'])
UserInfo = create_schema(Users)

# class UserNew(Schema):
#     username:str
#     password:str
#     created:datetime
#     updated:datetime

# class UserInfo(Schema):
#     id:int = None
#     username:str = None
#     password:str = None
#     created:datetime = None
#     updated:datetime = None
    
    
################################################
# route

@router.post('/create')
def user_create(request, payload:UserNew):
    check = Users.objects.filter(username=payload.username)
    
    if not check:
        user = Users.objects.create(**payload.dict())
        return {'id': user.id, 'username': user.username }
    
    return {'detail': 'username cannot be used'}


@router.get('/retrive/{user_name}',  response=UserInfo)
def user_retrive(request, user_name:str):
    user = get_object_or_404(Users, username=user_name)
    return user


@router.put('/update/{user_id}')
def user_update(request, user_id:int, payload:UserInfo):
    user = get_object_or_404(Users, id=user_id)
    
    if not user:
        return {'detail': 'User not found'}
    
    for attr, value in payload.dict().items():
        setattr(user, attr, value)
    user.save()
    
    return {'id': user.id, 'username': user.username }


@router.delete('/delete/{user_id}')
def user_delete(request, user_id:int):
    user = get_object_or_404(Users, id=user_id)
    
    if not user:
        return {'detail': 'User not found'}
    
    userId = user.id
    user.delete()
    
    return {'detail': 'User delete', 'id': userId }