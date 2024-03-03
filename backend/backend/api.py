from ninja import NinjaAPI

from user.api import router as user_router

api = NinjaAPI(csrf=True)

api.add_router('/user/', user_router)