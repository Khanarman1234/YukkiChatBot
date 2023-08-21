#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/YukkiChatBot >.
#
# This file is part of < https://github.com/TeamYukki/YukkiChatBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiChatBot/blob/master/LICENSE >
#
# All rights reserved.
#

from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID","28645948"))
API_HASH = getenv("API_HASH","0d1cca3a9f4f4beb7ae8508f05ec4fcd")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","6097049592:AAFqoIoUpFNiiXr7YrIk5uY0g_b5SVLMmsE")

# SUDO USERS
SUDO_USER = list(
    map(int, getenv("SUDO_USER","-6412641300").split())
)  # Input type must be interger

# You'll need a Private Group ID for this.
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID","-1001870000608"))

# Message to display when someone starts your bot
PRIVATE_START_MESSAGE = getenv(
    "PRIVATE_START_MESSAGE",
    "Hello! Welcome to my Personal Assistant Bot",
)

# Database to save your chats and stats... Get MongoDB:-  https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/mongodb#4.-youll-see-a-deploy-cloud-database-option.-please-select-shared-hosting-under-free-plan-here
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://ainul99050:575751ai@cluster0.ozzd6ua.mongodb.net/?retryWrites=true&w=majority")
