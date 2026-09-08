from django.urls import path
from .views import (
    GetOneOwnerView, 
    VerifyOwnerView, 
    GetAllBotOwnerView, 
    GetAllActiveBotOwnerView, 
    GetAllInactiveBotOwnerView, 
    CRUDBotOwnerView,
    GetAllBotView,
    GetOneBotView,
    )

urlpatterns = [ 
    path("owners/<int:owner_id>/", GetOneOwnerView.as_view()), 
    path("owners/<int:owner_id>/verify/", VerifyOwnerView.as_view()), 
    
    path("owners/<int:owner_id>/bots/", GetAllBotOwnerView.as_view()), 
    path("owners/<int:owner_id>/bots/active/", GetAllActiveBotOwnerView.as_view()), 
    path("owners/<int:owner_id>/bots/inactive/", GetAllInactiveBotOwnerView.as_view()),
    path("owners/<int:owner_id>/bots/<int:bot_id>/", CRUDBotOwnerView.as_view()), 
    
    path("bots/", GetAllBotView.as_view()),
    path("bots/<int:bot_id>/", GetOneBotView.as_view()), 
]