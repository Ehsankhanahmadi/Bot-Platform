database = [
    {
        "token":'8718447220:AAFUFTbQ_BZVhLsrcoXIwBx1ehcvHEfyWGI',
        "bot_username": "@sdcsdfswefwef_bot",
        "bot_id": 8718447220,
        "user_id": 6247073627,
        "active": True
    },
    {
        "token":'8620932466:AAHpUgtbBICRBsp_dYsRDWGMyBCHK8Fb_mE',
        "bot_username": "@sdgfsddgr_bot",
        "bot_id": 8620932466,
        "user_id": 6247073627,
        "active": False
    }
]

from .crud import create_bot, get_all_bot, get_all_active_bot, get_all_inactive_bot, get_bot_by_id, update_bot, delete_bot_by_id 
from .status import status_change_bot