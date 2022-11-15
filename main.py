import nextcord
from nextcord.ext import commands
from server_code import server_code

intents = nextcord.Intents.default()
intents = nextcord.Intents().all()
bot = commands.Bot(command_prefix="g.", intents=intents)

@bot.event
async def on_ready():
  print(f"{bot.user.name} is operational!")

logging = True
logschannel = ("#copy id from channel")

@bot.slash_command()
async def kick(interaction: nextcord.Interaction, user: nextcord.Member, reason: str):
  if not interaction.user.guild_permissions.administrator:
    await interaction.response.send_message("You are not authorized to run this command.")
  else:
      await interaction.response.send_message(f"Kicked by {interaction.user.mention}")
      if logging is True:
        log_channel = bot.get_channel(logschannel)
        await log_channel.send(f"{user.mention} was kicked by {interaction.user.mention} for {reason}")
        await user.kick(reason=reason)

@bot.slash_command()
async def ban(interaction: nextcord.Interaction, user: nextcord.Member, reason: str):
    if not interaction.user.guild_permissions.administrator:
       await interaction.response.send_message("You are not authorized to run this command")
    else:
      await interaction.response.send_message(f"Banned by {interaction.user.mention}")
      if logging is True:
        log_channel = bot.get_channel(logschannel)
        await log_channel.send(f"{user.mention} was banned by {interaction.user.mention} for {reason}")
        await user.ban(reason=reason)

@bot.slash_command()
async def unban(interaction: nextcord.Interaction, user: nextcord.Member, reason: str):
  if not interaction.user.guild_permissions.administrator:
    await interaction.response.send_message("You are not authorized to run this command.")
  else:
      await interaction.guild.unban(nextcord.Object(id=user.id), reason=reason)
      if logging is True:
         log_channel = bot.get_channel(logschannel)
         await log_channel.send(f"{user.mention} was unbanned by {interaction.user.mention}")
         await user.unban(reason=reason)

server_code()
bot.run("TOKEN")
