# (c) @biisal
from os import getenv
import re

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "1249672673"))
API_ID = int(getenv("API_ID", "26597768"))
API_HASH = str(getenv("API_HASH", "340f87444e648a712eae77c310648e21"))
BOT_TOKEN = str(getenv("BOT_TOKEN", "8023193614:AAFzQOvIth3DUb1NWaK0_qZmdRHmwUSv5ac"))
MONGO_DB = str(
    getenv(
        "MONGO_DB",
        "mongodb+srv://replacewithyourmongodb:replacewithyourmongodb@cluster0.zi78j51.mongodb.net/?retryWrites=true&w=majority",
    )
)
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b><a href='telegram.me/bisal_files'>{file_name} Telegram : @Bisal_Files\n\nForward the file before Downloading.</a></b>",
    )
)
