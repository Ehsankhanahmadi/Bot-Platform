from django.urls import path
# from .views import OwnerCRUDView, OwnerBotCRUDView
from .views import (
    GetOneOwnerView, 
    VerifyOwnerView, 
    GetAllBotOwnerView, 
    GetAllActiveBotOwnerView, 
    GetAllInactiveBotOwnerView, 
    CreateBotOwnerView, 
    UpdateBotOwnerView, 
    DeleteBotOwnerView,
    GetAllBotView,
    GetOneBotView,
    )

urlpatterns = [ 
    # path("owners/", OwnersCRUDView.as_view()),
    # path("owners/<int:owner_id>/", OwnersCRUDView.as_view()),
    # path("owners/bots/", ...),
    # path("owners/bots/active/", ...),
    # path("owners/bots/inactive/", ...),
    # path("owners/bots/<int:bot_id>/", ...),


    path("owners/<int:owner_id>/", GetOneOwnerView.as_view()), #get one owner GetOneOwnerView
    path("owners/verify/", VerifyOwnerView.as_view()), #verify or create owner VerifyOwnerView
    
    path("owners/bots/<int:owner_id>/", GetAllBotOwnerView.as_view()), #get all bot this owner GetAllBotOwnerView
    path("owners/bots/active/<int:owner_id>/", GetAllActiveBotOwnerView.as_view()), #get all bot active this owner GetAllActiveBotOwnerView
    path("owners/bots/inactive/<int:owner_id>/", GetAllInactiveBotOwnerView.as_view()), #get all bot inactive this owner GetAllInactiveBotOwnerView
    path("owners/bots/add/", CreateBotOwnerView.as_view()), #create bot CreateBotOwnerView
    path("owners/bots/update/", UpdateBotOwnerView.as_view()), #edit bot UpdateBotOwnerView
    path("owners/bots/delete/", DeleteBotOwnerView.as_view()), #delete bot DeleteBotOwnerView
    
    path("bots/", GetAllBotView.as_view()), #get all bot GetAllBotView
    path("bots/<int:bot_id>/", GetOneBotView.as_view()), #get one bot GetOneBotView
]