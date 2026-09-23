# from . import ADAPTER_NAME,database



# async def verify_user(user,phone):
#     user_data = {
#         "telegram_id": user.id,
#         "user_name": user.username,
#         "is_bot": user.is_bot,
#         "adapter_name": ADAPTER_NAME,
#         "phone_number": phone,
#     }
#     for i in database:
#         if i["telegram_id"] == user.id:
#             print("user already exists")
#             return "verified"
#     database.append(user_data)
#     print(user_data)
#     print(database)
#     return "user added"