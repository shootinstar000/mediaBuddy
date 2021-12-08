import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1819979146:AAEEcY773i7H_3PS6UB6mUVEGbr6bPq878s")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "2557747"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "3022e575059ce68696f4fa4120ae33a2")

    # Authorized users to use this bot

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQCphF_75h3PWWgNe2Hr05nBY8sIZdHQRSya9DB87WhDLMgIRZviwDxwQpEQcZFfK565WH8FTf-iGQEnxt1zXNa0cU4KkTS3Ixth-sHnfmM0EtC887NS8GlwMX5iZsxbgDckZh3zvwcXJeYa9ZAMOTJ5jHoVzql5h9NsM1Sm46wUlscz_keIhtYOvBxZuVh8vd0Qy1aan5q2lwE-cTMe_ol_tbrGsRsYsT7yIgouUVGzEAnuEeHavgTNwlveMMozfW7wQ2mrbhvL85XhgnGJLiy9ubgpNnTrs_x81Dnu2yxF9hjZCVIWdzKZvmFxL_jEsNN1cX07ROTEvdcu35a6ptiCNHBcNwA")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
