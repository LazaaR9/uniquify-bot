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
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1900466126").split())

    # session name
    TG_USER_SESSION_NAME = os.environ.get("TG_USER_SESSION_NAME", "expedia")

    # tg user session string
    TG_USER_SESSION_STRING = os.environ.get("TG_USER_SESSION_STRING", "AgGHlFYAFbwmLYD4K4cphSo1GQ-yFWwGLXj_wB8aI3-_pwEIZH4wHrZTve8kBuSipBTtIKRqkAVRpxW85QJDIhVbAfN65k_IqDZcI6p5mMweRj73ekj9BIO-bGznP_HbzojILBx4SSLnTcJoU4iGotAS2ETXV82uLGbix2Y4wnpxUAZOxkqMsCU061N5_TlCAMx413CbcxivZSOAaNdzQjAaRT7Z1vYe_W735IJj8YBTrPRoh2Y67sxbk5OIJMN3k75GfXaA7K5ALJmXYVGAkboLiLcAY2NgRByFi8DR2Q14-zJlDc8XDN6ZHXn2LpA4qSbKdDWulzO-i2_apaJjeEnhN2DycQAAAAHi758KAA")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
