# from loader import dp, db, bot
# from data.config import ADMINS

# from aiogram import types

# @dp.message_handler(commands='sendusersfile')
# async def send_file(message: types.Message):
#     users = db.select_all_users()
#     users = [item for item in users if len(db.get_followers_list(item[0]))>2]
#     users.sort()

#     header = "User ID,Name\n"

#     data = ""
#     for user_id, name in users:
#         data += f"{user_id},{name}\n"

#     with open('data/users.csv', 'w') as file:
#         file.write(data)
#         file.write(header)

#     with open('data/users.csv', 'rb') as file:
#         await bot.send_document(file)