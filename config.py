# Copyright (c) 2022 Itz-fork

import os

class Config(object):
    # Mandotory
    APP_ID = int(os.environ.get("10565113"))
    API_HASH = os.environ.get("d2220b87fb12fc430dc8fcebbb03d95c")
    BOT_TOKEN = os.environ.get("5487441303:AAFx5vMRSHZB0hUof0yg-IonqxQiDPZE2Es")
    LOGS_CHANNEL = int(os.environ.get("-1001767895874"))
    BOT_OWNER = int(os.environ.get("834554042"))
    MONGODB_URL = os.environ.get("mongodb+srv://Yoelbot:<yoel123456>@cluster0.uhjrs.mongodb.net/?retryWrites=true&w=majority")
    GOFILE_TOKEN = os.environ.get("XE8x7h0aiUBxowfylfAmSLspaxUjAs4U")
    # Optional
    MAX_DOWNLOAD_SIZE = int(os.environ.get("MAX_DOWNLOAD_SIZE")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 999737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/NexaBots"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6
