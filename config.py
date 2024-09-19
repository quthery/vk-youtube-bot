from vkbottle import API, BuiltinStateDispenser
from vkbottle.bot import BotLabeler
from dotenv import load_dotenv
from vkbottle import UserAuth
import os

load_dotenv()
api = API(os.getenv("VK_TOKEN"))
user_api = API(os.getenv("VK_USER_TOKEN"))
service_api = API(os.getenv("VK_SERVICE_TOKEN"))


labeler = BotLabeler()
state_dispenser = BuiltinStateDispenser()

