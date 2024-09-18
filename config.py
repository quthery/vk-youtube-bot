from vkbottle import API, BuiltinStateDispenser
from vkbottle.bot import BotLabeler
from dotenv import load_dotenv
import os

load_dotenv()
api = API(os.getenv("VK_TOKEN"))
labeler = BotLabeler()
state_dispenser = BuiltinStateDispenser()
