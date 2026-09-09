from django.urls import path
from .views import (
    CRUDOwnerView,
    CRUDBotOwnerView,
    GetAllBotView,
    GetOneBotView,
    )

urlpatterns = [ 
    path("owners/<int:owner_id>/", CRUDOwnerView.as_view()), 
    path("owners/<int:owner_id>/bots/<int:bot_id>/", CRUDBotOwnerView.as_view()), 
    
    path("bots/", GetAllBotView.as_view()),
    path("bots/<int:bot_id>/", GetOneBotView.as_view()), 
]