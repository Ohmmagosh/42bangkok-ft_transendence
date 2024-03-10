from ninja import NinjaAPI

from user.api import router as user_router
from match.api import router as match_router

api = NinjaAPI(csrf=True)

api.add_router('/user/', user_router)
api.add_router('/match/', match_router)
