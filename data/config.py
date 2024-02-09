from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_LINK = env.str("BOT_LINK")
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn

ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili

CHANEL_ID = env.int("CHANEL_ID") # Qanallar idisi
CHANEL_LINK = env.str("CHANEL_LINK")