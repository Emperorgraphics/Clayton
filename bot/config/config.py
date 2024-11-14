from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: str 25919445
    API_HASH: str ee53bc74083bffda82227a5f88082b84


    REF_LINK: str = "https://t.me/claytoncoinbot/game?startapp=952149020"

    AUTO_TASK: bool = True
    AUTO_CONNECT_WALLET: bool = True
    AUTO_JOIN_CHANNEL: bool = False

    GAMES_TO_PLAY: list[str] = ["stack", "clayball"]

    DELAY_EACH_ACCOUNT: list[int] = [20, 30] # seconds
    SLEEP_TIME_BETWEEN_EACH_ROUND: list[int] = [2, 3] # hours
    ADVANCED_ANTI_DETECTION: bool = True

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()

