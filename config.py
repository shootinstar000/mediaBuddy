import os
import logging
#
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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQBgSc8elitMGPv9tR2EfK_L7z0VK4wOxL1R8KrESPCsPbtxZuTsHTqS54WrT8TQAR4XcUCy8fR28hCDtz89Faqy6-w26SaKzvfocR0oZCv8qLCpzE_KV3xqyfyVcPJLloXcFlq5FM1j0Ybg1hdluiN9NNBU9viPDMc_0S76q_5M6BR59-3MFLBhq1470JQXBUnGm72xg9r_bJw0aC0tuXv56H-1kdTe0y_7vCzDYjd9FxR_Yyly-F0Zcdnwmk_-NFcYWktSvFpahFSXb4ivnOF9VypekmUr_i1mQCni147GJRX9EWEg28VIPlnC8D7qhUJZDFNWij_z8GcvkAMPhKQJNHBcNwA")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
