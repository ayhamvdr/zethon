from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("24757025")
APP_HASH = os.environ.get("0f7f459f8afef5f49a42dd2738644bcb")
BOT_USERNAME = os.environ.get("@zz44zzbot")
session = os.environ.get("1ApWapzMBuxLExxOzjxNmXGaDoUzkbfBD3ghFPM4lp0yhuLdGIPFrjO5D_bn3Rgv4BDYTYtXs0luI9_1E5bca7r3IfimUAJA8xanT_vAMOD7U3MAwNAs8l-ow8fixXXft2AFDJyziF0Rmu9iU-juuiGn9QhF5eUO5PWf-kuvSm9DiyydhlUstc26jFXK33BTvISNN6VZBp1L2-ZjDJHDPPJfoxzgx1V7xY_EiOPpV0wU8D5RRKDHMmhWCatBKOeDT07o66LkgiINZM8KErLNeRqRw_fBbdVNNaheGieKf6d6-7-j6NZQfEd7HB0BXP8108tYzCVEW3zLX1c70cQCWL8s7Ub2W6I4=")
SESSION = os.environ.get("TERMUX")
token = os.environ.get("6849130408:AAGg9xCo5TwlFStmnbA6SSQVYAc02g0MIeA")
Ze = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()

