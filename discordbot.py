from discord.ext import commands
import discord
import os
import traceback
# 接続に必要なオブジェクトを生成
client = discord.Client()
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@client.event
async def on_reaction_add(reaction,user):
	if reaction.emoji=="📧":
		embed = discord.Embed(description=reaction.message.content)
		embed.set_author(name=reaction.message.author.display_name,icon_url=reaction.message.author.avatar_url)
		# ファイルがある場合
		if reaction.message.attachments:
			for attachment in reaction.message.attachments:
				# Attachmentの拡張子がpng, jpg, jpegのどれかだった場合
				if attachment.url.endswith(("png", "jpg", "jpeg","JPG")):
					embed.set_image(url=attachment.url)
		await user.send(embed=embed)
		# await user.send(reaction.message.content)

client.run(TOKEN)
