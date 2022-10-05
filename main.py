import nextcord
from nextcord.ext import commands

intents = nextcord.intents.default()
intents = nextcord.Intents().all()
bot = commands.Bot(command_prefix="g.", intents=intents)

@bot.event
async def on_ready():
  print(f"(bot.user.name) is ready!")

logging = True
logschannel = 1027025704568754217

@bot.slash.command()
async def kick(interaction: nextcord.Interaction, user: nextcord.Member, reason: str):
  if not interaction.user.guild.permissions.administrator:
    await interaction.response.send_message("You are not authorized to run this command", epheneral-True)
    else:
      await interaction.response.send_message(f"Kicked by (user.mention", epheneral.True)
      if logging is True:
        log_channel = bot.get.channel(logschannel)
        await log_channel.sent(f"(user.mention) was kicked by (interaction.user.mention"), epheneral.True)

bot.run("MTAyNzAwOTU2MDA5Mjg3Njg1MA.GxPG1U.i4P9uRMCM2GIdTKmLpN9rb6oPPfqsecN-Byaj8")

