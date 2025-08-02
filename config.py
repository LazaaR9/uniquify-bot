import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):
    # Get a bot token from @botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8090679623:AAFC0dEIoXcj3huhg0UV1FH9vSea9sAQuZ4")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "25662550"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "3d2663ae1493ece93fab45f83b659acc")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "8102321930").split())

    # session name
    TG_USER_SESSION_NAME = os.environ.get("TG_USER_SESSION_NAME", "expedia")

    # tg user session string
    TG_USER_SESSION_STRING = os.environ.get("TG_USER_SESSION_STRING", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
