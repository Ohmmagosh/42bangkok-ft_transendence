from ninja import Schema, ModelSchema
from datetime import datetime
from .models import *
from typing import List

class ErrorSchema(Schema):
    detail: str

class UserListSchema(Schema):
    id: int
    username: str

class UserLogin(Schema):
    username: str
    password: str

class UserProfileSchema(ModelSchema):
    class Meta:
        model = UserProfile
        exclude = ['id', 'user']

class UserStatSchema(ModelSchema):
    class Meta:
        model = UserStat
        exclude = ['id', 'user']

class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'is_active']

class UserDataSchema(Schema):
    id: int
    user: UserSchema
    profile: UserProfileSchema
    stat: UserStatSchema


class UserCreateSchema(Schema):
    username: str
    password: str

class UserEditSchema(ModelSchema):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class UserEditDataSchema(Schema):
    user: UserEditSchema
    profile: UserProfileSchema