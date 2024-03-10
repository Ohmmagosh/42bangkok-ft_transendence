from ninja import Schema, ModelSchema
from .models import MatchInfo
from user.models import User
from user.schema import UserListSchema
from datetime import datetime

class MatchCreateSchema(Schema):
    user1: UserListSchema
    user2: UserListSchema
    created_datetime: datetime
    
class MatchInfoSchema(Schema):
    id: int
    user1: UserListSchema
    user2: UserListSchema
    isUser1Win: bool
    isUser2Win: bool
    score_user1: int
    score_user2: int
    updated_datetime: datetime
    
class MatchUpdateSchema(Schema):
    winner: int
    user1_score: int
    user2_score: int