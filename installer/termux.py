# /usr/bin/python3
# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# Please read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
# Recode Panda Userbot
## Thanks full Ultroid For installer termux env


from time import sleep
from os import system, path

ALBY = "★ ALBY PYROBOT DEPLOY★"


def clear():
    system("clear")


def with_header(text):
    return ALBY + "\n\n" + text


def pyrogram():
    yes_no = input("").strip().lower()
    if yes_no in ["pyrogram", "p"]:
        return True
    elif yes_no in ["nopyrogram", "nop"]:
        return False
    print("Invalid Input\nRe-Enter: ")
    return pyrogram()

def ask_process_info_text():
    strm = input("").lower().strip()
    if strm == "e":
        print("Exiting...")
        exit(0)
    elif strm != "a":
        print("Invalid Input")
        print("Enter 'A' to Continue or 'E' to exit...")
        ask_process_info_text()

   
def envpyrogram():
    start = input("").strip().lower()
    if start in ["pyrogram", "p"]:
        print(f"Ketik p untuk Creating .env file.. Pyrogram")
        with open(".env", "a") as file:
            for var in ["API_ID", "API_HASH", "PyroSESSION", "DATABASE_URL", "PRIVATE_GROUP_BOT_API_ID", "BOT_TOKEN", "BOT_USERNAME"]:
                inp = input(f"Enter {var}\n- ")
                file.write(f"{var}={inp}\n")
        print("* Created '.env' file successfully! 😃 klik enter")

clear()
if not path.exists(".env"):
    print(with_header("# Do you want to move toward creating .env file ? [p] p untuk pyrogram "))
    envpyrogram()
    
print(f"Silakan Ketik screen -S pyroline")
sleep(0.2)
print(f"Use 'bash start.sh' Untuk memulai ALBY PYROBOT")
sleep(0.5)
print("\nMade with 🦁 by @ruangprojects...")
