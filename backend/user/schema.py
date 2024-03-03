from ninja import Schema, ModelSchema
from datetime import datetime
from .models import *
from typing import List

class UserList(Schema):
    username: str

class UserProfileSchema(ModelSchema):
    class Meta:
        model = UserProfile
        exclude = ['id']

class UserStatSchema(ModelSchema):
    class Meta:
        model = UserStat
        exclude = ['id']

class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ['id', 'username','password']

class UserCombinedSchema(Schema):
    user: UserSchema
    user_profile: UserProfileSchema
    user_stat: UserStatSchema
