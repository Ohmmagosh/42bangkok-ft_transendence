from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.security import django_auth
from .models import MatchInfo
from user.models import User
from .schema import MatchCreateSchema, MatchUpdateSchema, MatchInfoSchema
from typing import List

router = Router(auth=django_auth)

@router.get('/get_matches/', response=List[MatchCreateSchema])
def get_matches(request):
    match = MatchInfo.objects.all()
    return match

@router.get('/get_match/{mid}/', response=MatchInfoSchema)
def get_match(request, mid: int):
    match = get_object_or_404(MatchInfo, pk=mid)
    return match


@router.post('/create_match/')
def create_match(request, id1:int, id2:int):
    u1 = get_object_or_404(User, pk=id1)
    u2 = get_object_or_404(User, pk=id2)
    match = MatchInfo.objects.create(user1=u1, user2=u2)
    match.save()
    return f'Match: {match.id} => {match.user1} vs {match.user2}'


@router.post('/update_match/{mid}/')
def update_match(request, mid:int, data:MatchUpdateSchema):
    match = get_object_or_404(MatchInfo, pk=mid)
    match.update_match(data.winner, data.user1_score, data.user2_score)
    match.save()
    return f'update success'