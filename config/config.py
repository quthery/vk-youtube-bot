from vkbottle import API, BuiltinStateDispenser
from vkbottle.bot import BotLabeler
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    VK_TOKEN: str
    VK_USER_TOKEN: str
    MAIN_GROUP_TOKEN: str
    
    @property
    def DATABASE_URL_asyncpg(self):
        # postgresql+asyncpg://postgres:postgres@localhost:5432/sa
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DATABASE_URL_psycopg(self):
        # DSN
        # postgresql+psycopg://postgres:postgres@localhost:5432/sa
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    @property
    def main_bot(self):
        return API(self.MAIN_GROUP_TOKEN)
    
    @property
    def user_api(self):
        return API(self.VK_USER_TOKEN)

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()


labeler = BotLabeler()
state_dispenser = BuiltinStateDispenser()

