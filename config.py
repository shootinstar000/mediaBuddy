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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQC9hCYM7gWdIYwz7EmM8nQeRgBLjTARgDtW0tLyxF9mQUfifLWx_wZwMx3TpzNrXKJZqniezdettRlJ_z_Cx2PJyH5lURs6aDmXZ3VmfpOJqzHBwmbnWH-0WeIPhEQ9_NtOQ1HR7ftBdMzgpiik303IZpNJA3er712C2z2eo4NjbSlrdE25pxx1E78uz5wo1eQuUbh4NNwbsAHc_T5wwlIpZRM1-WEQ-8kXGvCBiCWLLanBS8fiVhYjpqoY-kkp_EfVSVbSfp93iPbVkzQz_2HEe_LZ4QICZ2GGH5g9x3ZJlcEDFQW-NkNgXPaXGSRLROL-yEeSICw_l_5VA_KKaaK4NHBcNwA")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
